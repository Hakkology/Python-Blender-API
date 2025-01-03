import os
import subprocess
import bpy
import sys

render_mode = True

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
from tests.test0 import test0
from tests.test1 import test1
from tests.test2 import test2
from tests.test3 import test3
from tests.test4 import test4
from tests.test5 import test5
from tests.test6 import test6
from tests.homework1 import homework1
from tests.homework2 import homework2
from tests.homework3 import homework3
from tests.final1 import final1
from tests.final2 import final2
from modules.delete import delete_all
from modules.render import render_to_folder, bake_simulation_cache_to_disk

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
# homework1()
# homework2()
# homework3()
final1()
# final2()

# Render if render_mode is True
if render_mode:
    bake_simulation_cache_to_disk(frame_start=1, frame_end=250)
    render_to_folder(render_name='BCO602_Final1', res_x=768, res_y=768, engine='BLENDER_EEVEE', animation=True)

# Ensure the scene is updated
bpy.context.view_layer.update()
bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)

# Open the saved file in a new Blender instance
subprocess.Popen(['blender', blend_file_path])
