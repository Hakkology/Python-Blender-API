import bpy
import random
import math
from modules.create import create
from modules.act import act
from modules.sel import sel
from modules.selection import select
from modules.det import add_bevel
from modules.light import create_directional_light

def lerp(start, end, factor):
    """Lerp function"""
    return start + factor * (end - start) # basic lerp function

def create_pastel_color():
    """Mix colour with white"""
    base_color = [random.random() for _ in range(3)]
    white = [1, 1, 1]
    mix_factor = 0.6  # for pastel colouring
    
    pastel = [lerp(base, 1, mix_factor) for base in base_color]
    return (*pastel, 1)  


def homework3():
    cubes = []
    cube_data = {}

    # lights
    create_directional_light(
        location=(0, 0, 10),
        rotation=(math.radians(45), math.radians(45), math.radians(270)),
        energy=1000,
        color=(1, 1, 1)
    )

    # 20x20 grid of cubes
    for x in range(20):
        for y in range(20):
            cube_name = f'AnimatedCube_{x}_{y}'
            create.cube(cube_name)

            cube = select(cube_name)
            add_bevel(cube)
            
            # random height
            initial_z = random.uniform(0, 0.5)
            movement_range = random.uniform(0.25, 0.5)
            sel.translate((x * 1.1, y * 1.1, initial_z))
            
            act.scale((2, 2, 2))
            
            # random colour
            mat = bpy.data.materials.new(name=f"Color_{x}_{y}")
            mat.diffuse_color = create_pastel_color()
            
            cube = bpy.context.active_object
            if cube.data.materials:
                cube.data.materials[0] = mat
            else:
                cube.data.materials.append(mat)
            
            # add to list
            cubes.append(cube)
            cube_data[cube] = {
                'initial_z': initial_z,
                'movement_range': movement_range,
                'phase_offset': random.uniform(0, 2 * math.pi)
            }

    # Animate all frames
    for frame in range(0, 250):
        bpy.context.scene.frame_set(frame)
        
        for cube in cubes:
            data = cube_data[cube]
            # sin wave for movement
            cube.location.z = data['initial_z'] + (data['movement_range'] * 
                math.sin((frame / 10) + data['phase_offset']))  # 10 frames per cycle
            cube.keyframe_insert(data_path="location", frame=frame)
            
            # smooth interpolation
            if cube.animation_data and cube.animation_data.action:
                for fcurve in cube.animation_data.action.fcurves:
                    for keyframe in fcurve.keyframe_points:
                        keyframe.interpolation = 'BEZIER'
                        keyframe.handle_left_type = 'AUTO_CLAMPED'
                        keyframe.handle_right_type = 'AUTO_CLAMPED'