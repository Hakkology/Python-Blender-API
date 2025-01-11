import bpy
import math

def add_wind(location=(0, 0, 0), strength=1.0, noise=0.0, seed=1):
    bpy.ops.object.effector_add(type='WIND', location=location)
    wind = bpy.context.active_object
    
    field = wind.field
    field.strength = strength
    field.noise = noise
    field.seed = seed
    field.use_absorption = False
    
    # Falloff ayarları
    field.falloff_type = 'SPHERE'
    field.falloff_power = 0.1  # Çok yavaş güç azalması
    field.use_max_distance = True
    field.use_min_distance = True
    field.distance_min = 0.0
    field.distance_max = 50.0  # Çok daha geniş etki alanı
    
    return wind

def add_turbulence(location=(0, 0, 0), strength=5.0, size=1.0, noise=0.0):
    bpy.ops.object.effector_add(type='TURBULENCE', location=location)
    turbulence = bpy.context.active_object
    
    field = turbulence.field
    field.strength = strength
    field.size = size
    field.noise = noise
    field.use_absorption = False
    
    # Falloff ayarları
    field.falloff_type = 'SPHERE'
    field.falloff_power = 0.1  # Çok yavaş güç azalması
    field.use_max_distance = True
    field.use_min_distance = True
    field.distance_min = 0.0
    field.distance_max = 50.0  # Çok daha geniş etki alanı
    
    return turbulence

def animate_force_field(field, frames=250):
    """
    Animates a force field's strength continuously
    """
    initial_strength = field.field.strength
    
    # Her frame için sürekli animasyon
    for frame in range(frames):
        # Sürekli dalgalanma için birden fazla sinüs dalgasını birleştir
        wave1 = 0.1 * math.sin(2 * math.pi * frame / 60)  # Yavaş dalga
        wave2 = 0.05 * math.sin(2 * math.pi * frame / 30)  # Hızlı dalga
        variation = wave1 + wave2
        
        new_strength = initial_strength * (0.9 + variation)
        
        # Keyframe ekle
        field.field.strength = new_strength
        field.field.keyframe_insert(data_path="strength", frame=frame)
    
    # Son frame'den sonra da devam etmesi için son değeri tekrarla
    field.field.strength = initial_strength
    field.field.keyframe_insert(data_path="strength", frame=frames)
    
    # Döngüsel animasyon için
    if field.animation_data and field.animation_data.action:
        field.animation_data.action.use_cyclic = True
        
        # Smooth interpolation
        for fcurve in field.animation_data.action.fcurves:
            fcurve.modifiers.new('CYCLES')
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'BEZIER'
                keyframe.handle_left_type = 'AUTO'
                keyframe.handle_right_type = 'AUTO'