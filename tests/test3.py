import bpy

from math import sin
from create import create
from sel import sel

def test3():
    for i in range(50):
        create.cube('PerfectCube_')
        x, y, z = 0, i, sin(i)
        sel.translate((x, y, z))