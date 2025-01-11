import bpy
import math

def add_camera(location=(0, 5, 10), rotation=(math.radians(40), 0, math.radians(180))):
    bpy.ops.object.camera_add(location=location, rotation=rotation)
    bpy.context.scene.camera = bpy.context.object 

def add_camera_for_mesh(mesh, distance=100, height=10, perspective=True):
    """
    Adds a camera that exactly frames the mesh, nothing more.
    """
    # Get mesh dimensions and location
    mesh_dimensions = mesh.dimensions
    mesh_location = mesh.location
    
    # Calculate the camera position
    camera = create_camera(
        location=(mesh_location.x, mesh_location.y - distance, mesh_location.z + height),
        rotation=(math.radians(90), 0, 0)
    )
    
    if perspective:
        camera.data.type = 'PERSP'
        
        # Calculate FOV to exactly match mesh height
        mesh_height = mesh_dimensions.y  # Y dimension after 90 degree rotation
        fov = 2 * math.atan((mesh_height / 2) / distance)
        
        # Set camera properties
        camera.data.lens_unit = 'FOV'
        camera.data.angle = fov
        
        # Lock camera to view only the mesh
        camera.data.sensor_fit = 'VERTICAL'
        camera.data.sensor_height = mesh_height
    
    return camera

# for camera return
def create_camera(name="Camera", location=(0, 0, 10), rotation=(0, 0, 0)):
    """Create a camera and return it"""
    bpy.ops.object.camera_add(location=location, rotation=rotation)
    camera = bpy.context.active_object
    camera.name = name
    return camera

def follow_path(camera, curve, target_point=(0, 0, 0), frames=250):
    """Make camera follow a path while looking at a target"""
    # Add follow path constraint
    follow = camera.constraints.new(type='FOLLOW_PATH')
    follow.target = curve.curve_object
    follow.use_curve_follow = True
    follow.forward_axis = 'FORWARD_X'
    follow.up_axis = 'UP_Z'
    
    # Create target empty and add track to constraint
    target = create_target(target_point)
    track = camera.constraints.new(type='TRACK_TO')
    track.target = target
    track.track_axis = 'TRACK_NEGATIVE_Z'
    track.up_axis = 'UP_Y'
    
    # Set up path animation
    curve.curve_data.use_path = True
    curve.curve_data.path_duration = frames
    
    # Animate offset
    follow.offset = 0
    follow.keyframe_insert(data_path="offset", frame=1)
    follow.offset = 100
    follow.keyframe_insert(data_path="offset", frame=frames)
    
    # cyclic animation ?
    if camera.animation_data and camera.animation_data.action:
        for fc in camera.animation_data.action.fcurves:
            fc.modifiers.new(type='CYCLES')
    
    return camera

# set grid mid target
def create_target(location):
    """Create an empty object as camera target"""
    empty = bpy.data.objects.new("CameraTarget", None)
    empty.location = location
    bpy.context.scene.collection.objects.link(empty)
    return empty