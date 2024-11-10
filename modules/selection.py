import bpy
import bmesh

def select(objName):
    """
    Selects an object by its name, sets it as the active object, and returns it.
    """
    bpy.ops.object.select_all(action='DESELECT')
    obj = bpy.data.objects[objName]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    return obj

def activate(objName):
    """
    Activates an object by its name.
    """
    bpy.context.view_layer.objects.active = bpy.data.objects[objName]

def mode(mode_name):
    """
    Sets the object mode. Enters edit mode with no vertices selected,
    or enters object mode without additional processes.
    """
    bpy.ops.object.mode_set(mode=mode_name)
    if mode_name == "EDIT":
        bpy.ops.mesh.select_all(action="DESELECT")

def selection_mode(type):
    """
    Sets the selection mode (e.g., VERTEX, EDGE, FACE).
    """
    bpy.ops.mesh.select_mode(type=type)

def select_all():
    """
    Selects all objects in the scene.
    """
    bpy.ops.object.select_all(action='SELECT')

def coords(objName, space='GLOBAL'):
    """
    Fetches the coordinates of vertices in an object, in either global or local space.
    """
    obj = bpy.data.objects[objName]
    if obj.mode == 'EDIT':
        v = bmesh.from_edit_mesh(obj.data).verts
    elif obj.mode == 'OBJECT':
        v = obj.data.vertices
    if space == 'GLOBAL':
        return [(obj.matrix_world @ vert.co).to_tuple() for vert in v]
    elif space == 'LOCAL':
        return [vert.co.to_tuple() for vert in v]
