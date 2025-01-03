import bpy
import math
import random
import bmesh
from modules.selection import mode 
from modules.sel import sel  
from modules.calc import lerp
def makeMaterial(name, diffuse=(1, 1, 1, 1), metallic=0.0, specular=0.8, roughness=0.2):
    """
    This function defines a new material with a given name.

    If the diffuse value is not provided, it defaults to diffuse = (1, 1, 1, 1) (R, G, B, alpha)
    If the specular value is not provided, it defaults to 0.8
    If the metallic value is not provided, it defaults to 0.0
    If the roughness value is not provided, it defaults to 0.2 
    """
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.specular_intensity = specular
    mat.metallic = metallic
    mat.roughness = roughness
    return mat

def setMaterial(ob, mat):
    """
    This function assigns a material to an object.
    """
    if ob.data.materials:
        ob.data.materials[0] = mat
    else:
        ob.data.materials.append(mat)

def setSmooth(obj, level=None, smooth=True):
    """
    This function sets an object to have smooth shading and optionally adds a subsurf modifier.
    """
    if level:
        # Add subsurf modifier
        modifier = obj.modifiers.new(name='Subsurf', type='SUBSURF')
        modifier.levels = level
        modifier.render_levels = level

    # Set smooth shading
    mesh = obj.data
    for p in mesh.polygons:
        p.use_smooth = smooth

# GPT TEST, ADDING NODES, INVALID.
def makeStripedMaterial(name, stripe_count=12):
    """
    Creates a material with stripes and assigns it to the given object.
    :param name: The name of the material.
    :param stripe_count: The number of stripes around the sphere.
    """
    # Create a new material
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    nodes.clear()

    # Create necessary nodes
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    principled_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    tex_coord_node = nodes.new(type='ShaderNodeTexCoord')
    separate_xyz_node = nodes.new(type='ShaderNodeSeparateXYZ')
    math_node = nodes.new(type='ShaderNodeMath')
    color_ramp_node = nodes.new(type='ShaderNodeValToRGB')

    # Set up the nodes

    # Texture Coordinates -> Separate XYZ
    links.new(tex_coord_node.outputs['Generated'], separate_xyz_node.inputs['Vector'])

    # Separate XYZ Z -> Math Node (Modulo)
    links.new(separate_xyz_node.outputs['Z'], math_node.inputs[0])

    # Set Math Node to modulo operation to create angular divisions
    math_node.operation = 'MODULO'
    math_node.inputs[1].default_value = 2 * 3.14159265 / stripe_count  # Divide circle into equal parts

    # Math Node -> Color Ramp
    links.new(math_node.outputs['Value'], color_ramp_node.inputs['Fac'])

    # Color Ramp -> Principled BSDF Base Color
    links.new(color_ramp_node.outputs['Color'], principled_node.inputs['Base Color'])

    # Principled BSDF -> Material Output
    links.new(principled_node.outputs['BSDF'], output_node.inputs['Surface'])

    # Set up the color ramp with the required number of stripes
    color_ramp = color_ramp_node.color_ramp
    color_ramp.interpolation = 'CONSTANT'

    # Adjust existing elements
    color_ramp.elements[0].position = 0.0
    color_ramp.elements[0].color = (random.random(), random.random(), random.random(), 1)

    color_ramp.elements[1].position = 1.0
    color_ramp.elements[1].color = (random.random(), random.random(), random.random(), 1)

    # Remove extra elements if any (usually there are only 2 initially)
    while len(color_ramp.elements) > 2:
        color_ramp.elements.remove(color_ramp.elements[-1])

    # Add additional elements
    for i in range(1, stripe_count):
        position = i / stripe_count
        element = color_ramp.elements.new(position)
        element.color = (random.random(), random.random(), random.random(), 1)

    return mat


def assignMaterialsToSphere(sphere_obj, stripe_count):
    # Create materials
    materials = []
    for i in range(stripe_count):
        mat = bpy.data.materials.new(name=f"StripeMaterial_{i}")
        mat.diffuse_color = (random.random(), random.random(), random.random(), 1)
        materials.append(mat)
        sphere_obj.data.materials.append(mat)

    # Set to edit mode
    bpy.context.view_layer.objects.active = sphere_obj
    bpy.ops.object.mode_set(mode='EDIT')

    # Initialize bmesh for edit mode operations
    bm = bmesh.from_edit_mesh(sphere_obj.data)
    for face in bm.faces:
        # Calculate the angle of the face normal in spherical coordinates
        normal = face.normal.normalized()
        theta = math.atan2(normal.y, normal.x)  
        phi = math.acos(normal.z)  

        # Skip painting the top and bottom
        if phi < 0.2 or phi > (math.pi - 0.2):
            continue  

        # Map angle to stripe index
        index = int((theta + math.pi) / (2 * math.pi) * stripe_count) % stripe_count
        face.material_index = index

    # Update and return to object mode
    bmesh.update_edit_mesh(sphere_obj.data)
    bpy.ops.object.mode_set(mode='OBJECT')

def create_pastel_color(mix_factor):
    """Mix colour with white"""
    base_color = [random.random() for _ in range(3)]
    white = [1, 1, 1]
    
    pastel = [lerp(base, 1, mix_factor) for base in base_color]
    return (*pastel, 1)  