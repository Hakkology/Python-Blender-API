import bpy
from sel import sel  # sel sınıfını import ediyoruz

# Delete an object by name
def delete(objName):
    obj = bpy.data.objects.get(objName)
    if obj:
        sel.select_object(obj)
        bpy.ops.object.delete(use_global=False)

# Delete all objects
def delete_all():
    if len(bpy.data.objects) != 0:
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
