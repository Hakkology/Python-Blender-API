def get_number_pattern(number):
    patterns = {
        0: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        1: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,0,0,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        2: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,1,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        3: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        4: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        5: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        6: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        7: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,1,1,1,0,0],
            [0,0,0,0,1,1,1,0,0,0],
            [0,0,0,1,1,1,0,0,0,0],
            [0,0,1,1,1,0,0,0,0,0],
            [0,1,1,1,0,0,0,0,0,0],
            [0,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        8: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],
        9: [
            [0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,0,0,0,0,0,1,1,1,0],
            [0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    }
    return patterns.get(number, None)[::-1]

def move_cylinder(cylinder, is_raised, start_frame, end_frame, low_pos=0.5, high_pos=2.0):
    """
    Animates a cylinder's vertical movement
    """
    # Başlangıç pozisyonu
    cylinder.location.z = low_pos
    cylinder.keyframe_insert(data_path="location", frame=start_frame)
    
    # Hedef pozisyon
    target_z = high_pos if is_raised else low_pos
    cylinder.location.z = target_z
    cylinder.keyframe_insert(data_path="location", frame=end_frame)
    
    # Smooth interpolation
    if cylinder.animation_data and cylinder.animation_data.action:
        for fcurve in cylinder.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'BEZIER'
                keyframe.handle_left_type = 'AUTO_CLAMPED'
                keyframe.handle_right_type = 'AUTO_CLAMPED'

def animate_falling_text(text_obj, start_frame=1, end_frame=250, start_z=15, end_z=5):
    """
    Animates text falling with gravity-like motion
    """
    # Starting position keyframe
    text_obj.location.z = start_z
    text_obj.keyframe_insert(data_path="location", frame=start_frame)
    
    # Final position keyframe
    text_obj.location.z = end_z
    text_obj.keyframe_insert(data_path="location", frame=end_frame)
    
    # Add smooth easing
    if text_obj.animation_data and text_obj.animation_data.action:
        for fcurve in text_obj.animation_data.action.fcurves:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'SINE'
                keyframe.easing = 'EASE_OUT'