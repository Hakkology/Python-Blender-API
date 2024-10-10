import bpy

from random import randint
from create import create
from sel import sel

def test2():
    """Generate 50 cubes in random locations using the Blender scene."""
    for i in range(50):
        # Create a cube with a unique name
        cube_name = f'PerfectCube_{i}'
        create.cube(cube_name)

        # Generate random coordinates
        x, y, z = (randint(-10, 10), randint(-10, 10), randint(-10, 10))

        # Translate the cube to a random location
        sel.translate((x, y, z))

    # Ensure the scene is updated
    bpy.context.view_layer.update()