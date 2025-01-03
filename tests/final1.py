import bpy
import math
from modules.create import create
from modules.sel import sel
from modules.material import assignColorMaterial
from modules.keyframe import get_number_pattern, move_cylinder
from modules.camera import add_camera

grid_size = 10
spacing = 1

def final1():
    cylinders = []
    cylinder_matrix = [[None for _ in range(grid_size)] for _ in range(grid_size)]

    grid_center_x = (grid_size * spacing) / 2 - spacing/2
    grid_center_y = (grid_size * spacing) / 2 - spacing/2

    add_camera(
        location=(grid_center_x, grid_center_y - 10, 10),  
        rotation=(math.radians(45), 0, math.radians(180))  
    )

    for x in range(grid_size):
            for y in range(grid_size):
                # Cylinder options
                cylinder_name = f'Cylinder_{x}_{y}'
                create.cylinder(cylinder_name)
                sel.translate((x * spacing, y * spacing, 0.5))
                
                # Add Cylinder to list
                cylinder = bpy.context.active_object
                cylinders.append(cylinder)
                cylinder_matrix[x][y] = cylinder
                
                # Assign white material
                assignColorMaterial(cylinder, f'CylinderMaterial_{x}_{y}', color=(1, 1, 1, 1))
        
    # Create and position plane
    plane = create.plane('CoverPlane', size=grid_size * spacing +1)
    sel.translate((
        (grid_size * spacing) / 2 - spacing/2,  # x ekseni merkezi
        (grid_size * spacing) / 2 - spacing/2,  # y ekseni merkezi
        1.1  # z ekseni yüksekliği
    ))
    assignColorMaterial(plane, 'PlaneMaterial', color=(0, 0, 0, 1))

    frame_per_number = 25  # Her rakam için 25 frame
    
    for number in range(10):
        pattern = get_number_pattern(number)
        if pattern:
            start_frame = number * frame_per_number + 1
            end_frame = start_frame + frame_per_number - 1
            
            for x in range(grid_size):
                for y in range(grid_size):
                    cylinder = cylinder_matrix[x][y]
                    is_raised = pattern[y][x] == 1
                    move_cylinder(cylinder, is_raised, start_frame, end_frame)