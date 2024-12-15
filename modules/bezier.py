import bpy
import math
from mathutils import Vector

class BezierCurve:
    def __init__(self, name="BezierCurve"):
        # Create the curve data
        self.curve_data = bpy.data.curves.new(name=name, type='CURVE')
        self.curve_data.dimensions = '3D'
        
        # Create the object
        self.curve_object = bpy.data.objects.new(name, self.curve_data)
        bpy.context.scene.collection.objects.link(self.curve_object)
        
        # Create the spline
        self.spline = self.curve_data.splines.new('BEZIER')
        
    def set_control_points(self, points):
        """Set control points for the bezier curve"""
        # Resize spline if needed
        point_count = len(points)
        if len(self.spline.bezier_points) != point_count:
            self.spline.bezier_points.add(point_count - 1)
            
        # Set points
        for i, point in enumerate(points):
            self.spline.bezier_points[i].co = point
            self.spline.bezier_points[i].handle_left_type = 'AUTO'
            self.spline.bezier_points[i].handle_right_type = 'AUTO'
            
    def get_point_at(self, t):
        """Get point on curve at parameter t (0 to 1)"""
        # Evaluate curve at parameter t
        return self.curve_object.evaluated_get(bpy.context.evaluated_depsgraph_get()).to_curve().splines[0].evaluate(t)