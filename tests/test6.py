import bpy
from math import sin, cos

def test6():
    # Generate 100 y values
    n = 100
    # Number of vertices
    verts = []
    # n vertices
    edges = []
    # n-1 edges
    yVals = [y*0.18 for y in range(0, n)]
    zVals = [z*0.01 for z in range(0, n)]
    # Iterate over y values and generate 3D vertex coordinates
    for i, y in enumerate( yVals ):
        
        verts.append(( cos( y ), sin( y ), zVals[i]))
        # Set (x,y,z) vertex coordinate
        if i < n - 1:
        # Set edge vertices => this vertex and the next
            edges.append(( i, i+1 ))
    # Generate a new mesh
    mesh = bpy.data.meshes.new( 'helix' )
    # Create mesh
    mesh.from_pydata( verts, edges, () )
    # Generate an object to contain an instance of this mesh 'mesh'
    ob = bpy.data.objects.new( 'helix', mesh )
    # Link this virtual object to an acutal scene (the active or 'context' scene)
    bpy.context.collection.objects.link(ob)
    ob.select_set(True)