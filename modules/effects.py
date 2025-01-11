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
    field.z_direction = 'BOTH'
    field.flow = 1.0
    field.use_max_distance = False  # Mesafe sınırını kaldırıyoruz
    
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
    field.falloff_type = 'SPHERE'  # TUBE yerine SPHERE kullanalım
    field.z_direction = 'BOTH'     # Her iki yönde de etki
    field.flow = 1.0               # Akış gücü
    field.use_max_distance = False
    
    return turbulence

def animate_force_field(field, frames=250):
    initial_strength = field.field.strength
    
    # Kademeli başlangıç için
    ramp_frames = 50  # İlk 50 frame'de kademeli artış
    
    for frame in range(frames):
        # Başlangıç rampası
        ramp_factor = min(frame / ramp_frames, 1.0)
        
        # Normal dalgalanma
        wave1 = 0.1 * math.sin(2 * math.pi * frame / 60)
        wave2 = 0.05 * math.sin(2 * math.pi * frame / 30)
        variation = wave1 + wave2
        
        # Gücü hesapla (ramp faktörü ile çarparak)
        new_strength = initial_strength * (1.0 + variation)  # Keep strength constant after ramp-up
        
        field.field.strength = new_strength
        field.field.keyframe_insert(data_path="strength", frame=frame)
    
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