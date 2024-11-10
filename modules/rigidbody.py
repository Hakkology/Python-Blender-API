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
    sel.scale((1.5, 1.5, 1))  

    # Rigidbody settings
    bpy.ops.rigidbody.object_add()
    sphere.rigid_body.type = 'PASSIVE'
    sphere.rigid_body.collision_shape = 'MESH'
    sphere.rigid_body.mesh_source = 'BASE'

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
