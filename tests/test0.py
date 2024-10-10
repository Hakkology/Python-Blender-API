import bpy

def test0():    
    # Yeni bir küp ekleyelim
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))

    # Küpün boyutlarını ayarlayalım
    bpy.context.active_object.scale = (2, 1, 2)
