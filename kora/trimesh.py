import os
os.system("pip install trimesh")
from trimesh import Trimesh, PointCloud, Scene, voxel, unitize, tol, load, \
                    load_mesh, load_path, load_remote, primitives, \
                    transform_points, available_formats


# auto display itself, no need to call show()
Trimesh._repr_html_ = lambda self: self.show().data