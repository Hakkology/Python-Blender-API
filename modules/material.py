import bpy
import random

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


def makeMaterialWithStripes(obj, stripe_count=12):
    """
    Creates a material with stripes and assigns it to the given object.
    :param obj: The object to which the material will be assigned.
    :param stripe_count: The number of stripes around the sphere.
    """
    # Create a new material
    mat = bpy.data.materials.new(name="StripedMaterial")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes
    nodes.clear()

    # Create necessary nodes
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    principled_node = nodes.new(type='ShaderNodeBsdfPrincipled')
    texture_coord_node = nodes.new(type='ShaderNodeTexCoord')
    mapping_node = nodes.new(type='ShaderNodeMapping')
    wave_node = nodes.new(type='ShaderNodeTexWave')
    color_ramp_node = nodes.new(type='ShaderNodeValToRGB')

    # Set up the nodes

    # Texture Coordinates -> Mapping
    links.new(texture_coord_node.outputs['Object'], mapping_node.inputs['Vector'])

    # Mapping -> Wave Texture
    links.new(mapping_node.outputs['Vector'], wave_node.inputs['Vector'])

    # Wave Texture -> Color Ramp
    links.new(wave_node.outputs['Color'], color_ramp_node.inputs['Fac'])

    # Color Ramp -> Principled BSDF
    links.new(color_ramp_node.outputs['Color'], principled_node.inputs['Base Color'])

    # Principled BSDF -> Material Output
    links.new(principled_node.outputs['BSDF'], output_node.inputs['Surface'])

    # Set Wave Texture settings
    wave_node.wave_type = 'BANDS'
    wave_node.bands_direction = 'Z'  # Stripes around Z-axis

    # Correctly set the scale input
    wave_node.inputs['Scale'].default_value = stripe_count / 2  # Adjust scale to match stripe count

    # Adjust mapping node if needed
    mapping_node.inputs['Rotation'].default_value[2] = 0  # Rotate if needed

    # Set up the color ramp with the required number of stripes
    color_ramp = color_ramp_node.color_ramp
    color_ramp.interpolation = 'CONSTANT'

    # Clear existing elements
    # color_ramp.elements.clear()

    # Add stripe colors
    for i in range(stripe_count + 1):  # +1 because we need n+1 elements for n stripes
        position = i / stripe_count
        element = color_ramp.elements.new(position)
        # Assign a random color
        element.color = (random.random(), random.random(), random.random(), 1)

    # Assign the material to the object
    if obj.data.materials:
        # Assign to first material slot
        obj.data.materials[0] = mat
    else:
        # No material assigned yet
        obj.data.materials.append(mat)