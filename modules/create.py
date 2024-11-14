import bpy
from act import act  # act sınıfını kullanmak için import ediyoruz

class create:
    """Function Class for CREATING Objects"""

    def cube(objName):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))
        act.rename(objName)

    def sphere(objName):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 0))
        act.rename(objName)

    def cone(objName):
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0, 0, 0))
        act.rename(objName)

    def subdividedcube(objName, cuts=4, smoothness=0):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))
        act.subdivide(cuts=cuts, smoothness=smoothness)
        act.rename(objName)
