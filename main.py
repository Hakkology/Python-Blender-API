import sys
import os
import math
import subprocess
import bpy

# Add the directory containing your scripts to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import custom modules
from create import create
from sel import sel
from act import act
from spec import spec
from delete import delete, delete_all

# Set the path for the Blender file to the project directory
project_directory = os.path.dirname(os.path.abspath(__file__))
blend_file_path = os.path.join(project_directory, ".output.blend")

# Ensure the directory exists
os.makedirs(project_directory, exist_ok=True)

# Create a cube
create.cube('PerfectCube')
cube = bpy.data.objects['PerfectCube']

# Differential transformations combine
sel.translate((0, 1, 2))
sel.scale((1, 1, 2))
sel.scale((0.5, 1, 1))
sel.rotate_x(math.pi / 8)
sel.rotate_y(math.pi / 7)
sel.rotate_z(math.pi / 3)

# Create a cone
create.cone('PointyCone')
cone = bpy.data.objects['PointyCone']
act.location((-2, -2, 0))
spec.scale('PointyCone', (1.5, 2.5, 2))

# Create a Sphere
create.sphere('SmoothSphere')
sphere = bpy.data.objects['SmoothSphere']
spec.location('SmoothSphere', (2, 0, 0))
act.rotation((0, 0, math.pi / 3))
act.scale((1, 3, 1))

# Ensure the scene is updated
bpy.context.view_layer.update()

# Save the modified scene to the project directory
bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)

# Open the saved file in a new Blender instance
subprocess.Popen(['blender', blend_file_path])
