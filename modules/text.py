import bpy
from modules.selection import select
from modules.material import assignColorMaterial
from modules.physics import add_rigidbody
def create_3d_text(text, location=(0,0,0), size=1.0, extrude=0.6):
    """
    create 3d text
    """
    # Metin datası oluştur
    text_data = bpy.data.curves.new(name="Text", type='FONT')
    text_data.body = text
    
    # Metin objesi oluştur
    text_obj = bpy.data.objects.new(name=f"Text_{text}", object_data=text_data)
    bpy.context.scene.collection.objects.link(text_obj)
    
    # Metni aktif yap
    select(text_obj.name)
    
    # Metin ayarları
    text_data.size = size
    text_data.extrude = extrude  # 3D derinlik
    text_data.align_x = 'CENTER'  # Yatay ortalama
    text_data.align_y = 'CENTER'  # Dikey ortalama
    
    # Konumlandırma
    text_obj.location = location
    
    # Kırmızı materyal ekle
    assignColorMaterial(
        text_obj,
        f"TextMaterial_{text}",
        color=(1, 0, 0, 1),  # Kırmızı
        metallic=0.5,
        roughness=0.6
    )
    
    return text_obj