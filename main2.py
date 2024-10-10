import bpy

tk = bpy.data.texts['bco602tk.py'].as_module()

# Create a cube
tk.create.cube('PerfectCube')
# Differential transformations combine
tk.sel.translate(0, 1, 2)
tk.sel.scale((1, 1, 2))
tk.sel.scale((0.5, 1, 1))
tk.sel.rotate_x(3.1415 / 8)
tk.sel.rotate_x(3.1415 / 7)
tk.sel.rotate_z(3.1415 / 4)

# Create a cone
tk.create.cone('PointyCone')
# Declarative transformations overwrite
tk.act.location('PointyCone', (-2, 2.5, 0))
tk.spec.scale('PointyCone', (1.5, 2.5, 2))

# Create a sphere
tk.create.sphere('SmoothSphere')
# Declarative transformations overwrite
tk.act.location('SmoothSphere', (2, 0, 0))
tk.act.rotation((0, 0, 3.1415 / 3))
tk.act.scale((1, 3, 1))
