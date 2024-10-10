import bpy

from random import randint
from math import radians
from act import act
from create import create
from sel import sel

def test4():
    # Generate 5 random numbers in a list
    data = [randint(1, 5) for _ in range(5)]
    # Add text object
    sumdata = sum(data)
    for i in range(len(data)):
        # Set cube physical height as proportion of this random number from the total X 10
        cubeHeight = (data[i] / sumdata ) * 10
        # Create a cube
        create.cube('DataCube_')
        # Differential transformations combine
        sel.translate((i * 1.1, 0, cubeHeight/2))
        act.dimension(( 1, 1, cubeHeight))
        
        bpy.ops.object.text_add(location = ( i * 1.1, 1.5, 0 ))
        # Rotate text by 90 degrees along Z axis
        bpy.context.object.rotation_euler.z = radians(180)
        # Add depth to the text
        bpy.context.object.data.extrude = 0.05
        # Add a nice bevel effect to smooth the text's edges
        bpy.context.object.data.bevel_depth = 0.01
        # Set the text to be the current data
        bpy.context.object.data.body = str(data[i])