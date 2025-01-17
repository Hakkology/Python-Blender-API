import bpy
import os
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

    def cylinder(objName, radius=0.5, depth=1):
        bpy.ops.mesh.primitive_cylinder_add(
            radius=radius,
            depth=depth,
            location=(0, 0, 0)
        )
        act.rename(objName)
    
    def plane(objName, size=10):
        bpy.ops.mesh.primitive_plane_add(size=size, location=(0, 0, 0))
        act.rename(objName)
        return bpy.context.active_object
    
    def mesh_plane(objName, texture_path=None):
        """Creates a mesh plane with optional texture"""
        bpy.ops.mesh.primitive_plane_add(size=2)
        plane = bpy.context.active_object
        act.rename(objName)

        if texture_path and os.path.exists(texture_path):
            # Create new material
            mat = bpy.data.materials.new(name=f"Material_{objName}")
            mat.use_nodes = True
            nodes = mat.node_tree.nodes
            links = mat.node_tree.links
            
            # Clear default nodes
            nodes.clear()
            
            # Create nodes
            principled_bsdf = nodes.new('ShaderNodeBsdfPrincipled')
            output = nodes.new('ShaderNodeOutputMaterial')
            tex_image = nodes.new('ShaderNodeTexImage')
            
            # Load image
            tex_image.image = bpy.data.images.load(texture_path)
            
            # Link nodes
            links.new(tex_image.outputs['Color'], principled_bsdf.inputs['Base Color'])
            links.new(principled_bsdf.outputs['BSDF'], output.inputs['Surface'])
            
            # Assign material
            if plane.data.materials:
                plane.data.materials[0] = mat
            else:
                plane.data.materials.append(mat)

        return plane