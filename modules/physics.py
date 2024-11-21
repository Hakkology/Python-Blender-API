import bpy
import bmesh

from selection import select, mode, selection_mode
from sel import sel

def setup_rigidbody_world():
    """
    Sets up a rigid body world with gravity and adds a partial spherical ground plane.
    """
    # RigidBody World add
    # if not bpy.context.scene.rigidbody_world:
    #     bpy.ops.rigidbody.world_add()

    bpy.context.scene.gravity = (0, 0, -9.81)  

def create_partial_spherical_ground():
    """
    Creates a partial spherical ground plane as a rigid body.
    """
    bpy.ops.mesh.primitive_uv_sphere_add(radius=6, location=(0, 0, 0))
    sphere = bpy.context.object
    
    # Select the sphere and edit
    select(sphere.name)
    mode('EDIT')
    selection_mode('VERT')

    # Remove below portion
    bm = bmesh.from_edit_mesh(bpy.context.object.data)
    for vert in bm.verts:
        if vert.co.z > 1:
            vert.select = True
    bmesh.update_edit_mesh(bpy.context.object.data)
    
    bpy.ops.mesh.delete(type='VERT')
    mode('OBJECT')
    sel.scale((0.75, 0.75, 1))  

    bpy.context.view_layer.objects.active = sphere
    bpy.ops.object.modifier_add(type='COLLISION')

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
    bpy.context.view_layer.objects.active = obj
    if "Softbody" not in [m.name for m in obj.modifiers]:
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.modifier_add(type='SOFT_BODY')

    softbody = obj.modifiers["Softbody"]

    if settings is None:
        settings = {
            "friction": 0.5,          # Sürtünmeyi düşürdük
            "use_goal": False,
            "use_self_collision": True,
            "use_stiff_quads": True,
            "pull": 0.9,
            "push": 0.9,
            "damping": 0.1,           # Damping değerini 0.0 yaptık
            "shear": 1.0,
            "bend": 1.0,
            "mass": 2.0,              # Kütleyi artırdık
            "gravity": 1.0,
            "ball_size": 1.8,
            "ball_stiff": 1.0,
        }

    softbody.settings.friction = settings["friction"]
    softbody.settings.mass = settings["mass"]
    softbody.settings.use_goal = settings["use_goal"]
    softbody.settings.use_self_collision = settings["use_self_collision"]
    softbody.settings.use_stiff_quads = settings["use_stiff_quads"]
    softbody.settings.pull = settings["pull"]
    softbody.settings.push = settings["push"]
    softbody.settings.damping = settings["damping"]
    softbody.settings.shear = settings["shear"]
    softbody.settings.bend = settings["bend"]
    softbody.settings.gravity = settings["gravity"]
    softbody.settings.ball_size = settings["ball_size"]
    softbody.settings.ball_stiff = settings["ball_stiff"]

    # Solver ayarları
    softbody.settings.step_min = 10
    softbody.settings.step_max = 50
    softbody.settings.error_threshold = 0.01