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
    
def select_corner_edges(self, obj, angle_threshold=1.57):
    """
    Selects edges of the given object that have a face angle greater than or equal to the specified threshold (default 90 degrees).
    :param obj: The object whose edges will be selected.
    :param angle_threshold: The angle in radians to select edges (default is 1.57 radians, which is 90 degrees).
    """
    if obj and obj.type == 'MESH':
        bpy.context.view_layer.objects.active = obj  # Make sure the given object is active
        bpy.ops.object.mode_set(mode='EDIT')  # Switch to EDIT mode
        bpy.ops.mesh.select_all(action="DESELECT")  # Deselect all
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        bm.edges.ensure_lookup_table()
        bm.select_mode = {'EDGE'}  # Select edges
        
        # Loop through edges and select those with an angle above the threshold
        for e in bm.edges:
            if e.calc_face_angle_signed() >= angle_threshold:  # Check the angle
                e.select = True

        bmesh.update_edit_mesh(me)  # Update the mesh after selection
        bpy.ops.object.mode_set(mode='OBJECT')  # Return to OBJECT mode
