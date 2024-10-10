import bpy
import math
from create import create
from sel import sel
from act import act
from spec import spec

def test1():
    """Create objects and perform transformations in the Blender scene."""

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
