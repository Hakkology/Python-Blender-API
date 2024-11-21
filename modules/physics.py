import bpy
import bmesh

from selection import select, mode, selection_mode
from sel import sel

def setup_rigidbody_world():
    """
    Sets up a rigid body world with gravity and adds a partial spherical ground plane.
    """
    # RigidBody World add
    if not bpy.context.scene.rigidbody_world:
        bpy.ops.rigidbody.world_add()

    bpy.context.scene.gravity = (0, 0, -9.81)  

def create_partial_spherical_ground():
    """
    Creates a partial spherical ground plane with proper thickness and collision settings.
    """
    # Step 1: Add a UV sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=6, location=(0, 0, 0))
    sphere = bpy.context.object

    # Step 2: Enter Edit Mode to modify the sphere
    bpy.context.view_layer.objects.active = sphere
    bpy.ops.object.mode_set(mode='EDIT')

    # Use BMesh to remove the top part of the sphere
    bm = bmesh.from_edit_mesh(sphere.data)
    to_delete = [v for v in bm.verts if v.co.z > 1]  # Delete vertices above Z > 1
    bmesh.ops.delete(bm, geom=to_delete, context='VERTS')
    bmesh.update_edit_mesh(sphere.data)

    bpy.ops.object.mode_set(mode='OBJECT')  # Exit Edit Mode

    # Step 3: Apply a Solidify Modifier to add thickness
    solidify_modifier = sphere.modifiers.new(name="Solidify", type='SOLIDIFY')
    solidify_modifier.thickness = 0.5  # Add thickness
    bpy.context.view_layer.objects.active = sphere
    bpy.ops.object.modifier_apply(modifier="Solidify")  # Apply modifier

    # Step 4: Scale the object
    sphere.scale = (1.5, 1.5, 1)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # Step 5: Add Rigidbody settings
    bpy.ops.rigidbody.object_add()
    sphere.rigid_body.type = 'PASSIVE'
    sphere.rigid_body.collision_shape = 'MESH'
    sphere.rigid_body.mesh_source = 'BASE'
    sphere.rigid_body.collision_margin = 0.01  # Reduce margin for better precision

    print("Partial spherical ground created with thickness and proper collision settings.")
    return sphere


def add_rigidbody(obj, body_type='ACTIVE'):
    """
    Adds a rigidbody to the specified object.
    :param obj: The Blender object to which the rigidbody will be added.
    :param body_type: Type of rigidbody ('ACTIVE' for dynamic, 'PASSIVE' for static).
    """
    # Ensure the object is active and has a rigid body
    bpy.context.view_layer.objects.active = obj
    bpy.ops.rigidbody.object_add()
    
    # Set rigid body type
    obj.rigid_body.type = body_type
    obj.rigid_body.restitution = 0.9  # Bounciness ayarı

def add_softbody_modifier(obj, settings=None):
    """
    Adds a Softbody modifier to the given object with specified settings,
    including Collision settings for interaction with other objects.
    :param obj: The object to which the Softbody modifier will be added.
    :param settings: A dictionary containing the Softbody settings.
    """
    if obj is None or obj.type != 'MESH':
        print(f"Error: Object '{obj.name}' must be a mesh.")
        return
    
    # Ensure the object is active
    bpy.context.view_layer.objects.active = obj

    # Add Softbody modifier
    if "Softbody" not in [m.name for m in obj.modifiers]:
        bpy.ops.object.mode_set(mode='OBJECT')  # Ensure in OBJECT mode
        bpy.ops.object.modifier_add(type='SOFT_BODY')

    # Apply Softbody settings
    softbody = obj.modifiers["Softbody"]
    if settings:
        softbody.settings.friction = settings.get("friction", 0.1)
        softbody.settings.use_goal = settings.get("use_goal", False)
        softbody.settings.use_self_collision = settings.get("use_self_collision", True)
        softbody.settings.use_stiff_quads = settings.get("use_stiff_quads", True)
        softbody.settings.pull = settings.get("pull", 0.8)
        softbody.settings.push = settings.get("push", 0.8)
        softbody.settings.damping = settings.get("damping", 0.8)
        softbody.settings.shear = settings.get("shear", 0.8)
        softbody.settings.bend = settings.get("bend", 0.7)
    else:
        print("Warning: No custom settings provided. Using default values.")
    bpy.ops.object.modifier_add(type='COLLISION')