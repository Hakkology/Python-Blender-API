import sys
import os
import math
import subprocess
import bpy

# Add the directory containing your scripts to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import custom modules
from test0 import test0
from test1 import test1  
from test2 import test2
from test3 import test3
from test4 import test4
from delete import delete, delete_all

# Set the path for the Blender file to the project directory
project_directory = os.path.dirname(os.path.abspath(__file__))
blend_file_path = os.path.join(project_directory, ".output.blend")

# Ensure the directory exists
os.makedirs(project_directory, exist_ok=True)

delete_all()
# test0()
# test1()
# test2()
# test3()
test4()

# Ensure the scene is updated
bpy.context.view_layer.update()

# Save the modified scene to the project directory
bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)

# Open the saved file in a new Blender instance
subprocess.Popen(['blender', blend_file_path])