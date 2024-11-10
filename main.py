import sys
import os
import subprocess
import bpy

# Get the project directory
project_directory = os.path.dirname(os.path.abspath(__file__))

# List of directories to add to the Python path
directories_to_add = [
    project_directory,
    os.path.join(project_directory, 'modules'),
    os.path.join(project_directory, 'tests')
]

# Add each directory to the Python path if not already added
for directory in directories_to_add:
    if directory not in sys.path:
        sys.path.append(directory)

blender_scripts_path = bpy.utils.script_path_user() 
if blender_scripts_path and blender_scripts_path not in sys.path:
    sys.path.append(blender_scripts_path)

blend_file_path = os.path.join(project_directory, "scene/.output.blend")

# Import custom modules
from test0 import test0
from test1 import test1
from test2 import test2
from test3 import test3
from test4 import test4
from test5 import test5
from test6 import test6
from test7 import test7
from delete import delete, delete_all

# Ensure the directory exists
os.makedirs(project_directory, exist_ok=True)

delete_all()
# test0()
# test1()
# test2()
# test3()
# test4()
# test5()
# test6()
test7();

# Ensure the scene is updated
bpy.context.view_layer.update()
bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)

# Open the saved file in a new Blender instance
subprocess.Popen(['blender', blend_file_path])