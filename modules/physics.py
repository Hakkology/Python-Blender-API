import bpy
import bmesh

from selection import select, mode, selection_mode
from sel import sel

def setup_rigidbody_world(gravity=(0, 0, -9.81)):
    """
    Sets up a rigid body world with gravity and adds a partial spherical ground plane.
    """
    # RigidBody World add
    if not bpy.context.scene.rigidbody_world:
        bpy.ops.rigidbody.world_add()

    bpy.context.scene.gravity = gravity  

def create_partial_spherical_ground():
    bpy.ops.mesh.primitive_uv_sphere_add(radius=6, location=(0, 0, 0))
    sphere = bpy.context.object
    
    # Select the sphere and edit
    select(sphere.name)
    mode('EDIT')
    selection_mode('VERT')

    # Remove above portion
    bm = bmesh.from_edit_mesh(bpy.context.object.data)
    for vert in bm.verts:
        if vert.co.z > 1:
            vert.select = True
    bmesh.update_edit_mesh(bpy.context.object.data)
    
    bpy.ops.mesh.delete(type='VERT')
    mode('OBJECT')
    sel.scale((0.75, 0.75, 1))

    # Collision ayarları
    bpy.context.view_layer.objects.active = sphere
    bpy.ops.object.modifier_add(type='COLLISION')
    sphere.collision.damping = 0.6
    sphere.collision.use_culling = False
    sphere.collision.thickness_outer = 0.2
    sphere.collision.thickness_inner = 0.2

    # Passive rigidbody ekle
    bpy.ops.rigidbody.object_add()
    sphere.rigid_body.type = 'PASSIVE'
    sphere.rigid_body.collision_shape = 'MESH'
    sphere.rigid_body.friction = 0.8
    sphere.rigid_body.restitution = 0.5
    sphere.rigid_body.use_margin = True
    sphere.rigid_body.collision_margin = 0.2

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

def add_softbody_modifier(obj):
    bpy.context.view_layer.objects.active = obj
    if "Softbody" not in [m.name for m in obj.modifiers]:
        bpy.ops.object.modifier_add(type='SOFT_BODY')

    # Önce collision ekleyelim
    bpy.ops.object.modifier_add(type='COLLISION')
    obj.collision.damping = 0.8
    obj.collision.use_culling = False
    obj.collision.thickness_outer = 0.02
    obj.collision.thickness_inner = 0.02

    softbody = obj.modifiers["Softbody"]
    
    softbody.settings.pull = 0.9
    softbody.settings.push = 0.9
    softbody.settings.damping = 0.05
    softbody.settings.plastic = 1  # Integer değer olarak düzeltildi
    
    # Self collision ayarları
    softbody.settings.use_self_collision = True
    softbody.settings.collision_collection = bpy.context.scene.collection
    softbody.settings.ball_size = 0.5
    softbody.settings.ball_stiff = 0.95
    
    # Collision ayarları
    softbody.settings.use_edges = True
    softbody.settings.use_face_collision = True
    softbody.settings.collision_type = 'MANUAL'
    
    # Solver ayarları
    softbody.settings.step_min = 5
    softbody.settings.step_max = 50
    softbody.settings.error_threshold = 0.01
    softbody.settings.use_estimate_matrix = True
    
    # Cache ayarları
    softbody.point_cache.frame_start = 1
    softbody.point_cache.frame_end = 120