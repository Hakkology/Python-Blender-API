import bpy

def setup_rigidbody_world():
    """
    Sets up a rigid body world with gravity and adds a ground plane.
    """
    # RigidBody World ekle
    if not bpy.context.scene.rigidbody_world:
        bpy.ops.rigidbody.world_add()

    # Yerçekimini doğrudan sahne üzerinde etkinleştir
    bpy.context.scene.gravity = (0, 0, -9.81)  # Standart yerçekimi değeri

    # Zemin oluştur ve pasif bir RigidBody olarak ayarla
    bpy.ops.mesh.primitive_plane_add(size=50, location=(0, 0, 0))  # Daha büyük bir zemin
    bpy.ops.rigidbody.object_add()
    bpy.context.object.rigid_body.type = 'PASSIVE'
    bpy.context.object.rigid_body.collision_shape = 'MESH'
    bpy.context.object.rigid_body.mesh_source = 'BASE'

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
    obj.rigid_body.restitution = 0.9
