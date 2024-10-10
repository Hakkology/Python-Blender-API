import bpy 
from math import sin 
import random

from create import create
from sel import sel

def test5():
    # Küpleri saklamak için liste
    cubes = []  

    for i in range(50): 
        # Küp oluştur
        create.cube('PerfectCube_' + str(i))  

        # Koordinatları ayarla
        x, y, z = 0, i, sin(i)  
        sel.translate((x, y, z)) 

        # Küpü listeye ekle
        cube = bpy.context.object  
        cubes.append(cube)

        # Her yüzey için farklı renkler oluştur
        for j in range(6):  # Küpün 6 yüzeyi var
            mat = bpy.data.materials.new(name=f"Material_{i}_{j}")
            color = (random.random(), random.random(), random.random(), 1)  # Rastgele renk
            mat.diffuse_color = color
            
            # Malzemeyi yüzeye ata
            cube.data.materials.append(mat)
            cube.data.polygons[j].material_index = j  # Her yüzeye farklı malzeme ata

    # İlk animasyonu ayarla
    for i, cube in enumerate(cubes):
        # Yukarı hareket
        cube.keyframe_insert(data_path="location", frame=1)  # Başlangıç konumu
        cube.location.z = 2  # Yukarıda
        cube.keyframe_insert(data_path="location", frame=50 + i * 10)  # Yukarı çıkış

        # Aşağı hareket
        cube.location.z = 0  # Aşağıda
        cube.keyframe_insert(data_path="location", frame=100 + i * 10)  # Aşağı iniş

    # Sürekli hareket
    for frame in range(0, 1000):
        for i, cube in enumerate(cubes):
            # Her küp için sinüs dalgası ile sürekli yukarı ve aşağı hareket
            cube.location.z = 2 * sin((frame / 20) + (i * 0.2))  # Sürekli dalga hareketi
            
            # İleri doğru hareket
            cube.location.y += 0.01  # Her karede y ekseninde hafif ileri git
            cube.keyframe_insert(data_path="location", frame=frame)