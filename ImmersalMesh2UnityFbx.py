import bpy
import sys
import math
from pathlib import Path

print("Reset Objects")
# reset objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(True)

file_path = sys.argv[3]
file = Path(file_path)
print('filePath: '+file_path)
suffix = file.suffix
print("Import from " + file_path)
if suffix == ".ply":
    # import ply
    bpy.ops.import_mesh.ply(filepath=file_path)
    # rotate
    selected = bpy.context.selected_objects[0]
    atai = 2*math.pi/360*90
    selected.rotation_euler.x += atai
elif suffix == ".glb":
    # import glb
    bpy.ops.import_scene.gltf(filepath=file_path)
else:
    print("file format is invalid")

# export fbx
exportFilePath = file.with_suffix(".fbx").as_posix()
print("Export to " + exportFilePath)
bpy.ops.export_scene.fbx(filepath=exportFilePath,  embed_textures=True, path_mode='COPY', object_types={'ARMATURE','MESH'})