import bpy
import os

def import_obj(file_path, obj_name):
    # Dosyanın var olup olmadığını kontrol et
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # OBJ dosyasını içe aktar
        bpy.ops.wm.obj_import(filepath=file_path)
        
        # İçe aktarılan nesneyi yeniden adlandır
        if bpy.context.selected_objects:
            obj = bpy.context.selected_objects[0]
            obj.name = obj_name
            return obj
    except Exception as e:
        print(f"Error importing OBJ file: {str(e)}")
        return None
    
    return None