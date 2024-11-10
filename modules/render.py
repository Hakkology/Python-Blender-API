import bpy
import os

def bake_simulation_cache_to_disk(frame_start=1, frame_end=120):
    """
    Enables cache to disk for rigid body simulations to bake the simulation without keyframes.
    :param frame_start: Starting frame of the simulation.
    :param frame_end: Ending frame of the simulation.
    """
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end

    # Access rigid body world settings
    if bpy.context.scene.rigidbody_world:
        bpy.context.scene.rigidbody_world.point_cache.frame_start = frame_start
        bpy.context.scene.rigidbody_world.point_cache.frame_end = frame_end
        bpy.context.scene.rigidbody_world.point_cache.use_disk_cache = True
        bpy.context.scene.rigidbody_world.point_cache.name = "RigidBodyCache"

        # Bake the simulation
        bpy.ops.ptcache.bake_all(bake=True)
        print(f"Baked rigid body simulation to disk cache from frame {frame_start} to {frame_end}.")
    else:
        print("No rigid body world found in the scene.")

def render_to_folder(render_name='render', res_x=800, res_y=800, res_percentage=100, engine='BLENDER_EEVEE', animation=False, frame_end=None):
    """
    Renders the scene to a specified folder with the given settings.
    """
    scn = bpy.context.scene
    scn.render.engine = engine
    scn.render.resolution_x = res_x
    scn.render.resolution_y = res_y
    scn.render.resolution_percentage = res_percentage
    if frame_end:
        scn.frame_end = frame_end

    project_directory = os.path.dirname(os.path.abspath(__file__))
    render_folder_path = os.path.join(project_directory, 'scene')
    
    if not os.path.exists(render_folder_path):
        os.makedirs(render_folder_path)

    if animation:
        scn.render.image_settings.file_format = 'FFMPEG'
        scn.render.ffmpeg.format = 'MPEG4'
        scn.render.ffmpeg.codec = 'H264'
        scn.render.ffmpeg.constant_rate_factor = 'HIGH'
        scn.render.ffmpeg.ffmpeg_preset = 'GOOD'
        scn.render.filepath = os.path.join(render_folder_path, render_name + '.mp4')
        bpy.ops.render.render('INVOKE_DEFAULT', animation=True)
        print(f"Animation rendered to {os.path.join(render_folder_path, render_name + '.mp4')}")
    else:
        scn.render.image_settings.file_format = 'PNG'
        scn.render.filepath = os.path.join(render_folder_path, render_name + '.png')
        bpy.ops.render.render('INVOKE_DEFAULT', write_still=True)
        print(f"{render_name}.png is rendered to {render_folder_path}")