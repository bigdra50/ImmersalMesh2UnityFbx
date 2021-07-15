import bpy
import sys
import math
from pathlib import Path

print("Reset Objects")
# reset objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(True)

print("Import from " + sys.argv[3])
# import ply
bpy.ops.import_mesh.ply(filepath=sys.argv[3])

# rotate
selected = bpy.context.selected_objects[0]
atai = 2*math.pi/360*90
selected.rotation_euler.x += atai
    
# export fbx
file = Path(sys.argv[3])
exportFilePath = file.with_suffix(".fbx").as_posix()
print("Export to " + exportFilePath)
bpy.ops.export_scene.fbx(filepath=exportFilePath)

#immersal_ply_to_fbx("D://Data//3DObjects//DeskMapData//22781-Desk20210521-dense.ply")