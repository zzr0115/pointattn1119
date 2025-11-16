from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='chamfer_3D',
    version='0.0.0',
    ext_modules=[
        CUDAExtension('chamfer_3D', [
            'chamfer_cuda.cpp',
            'chamfer3D.cu',
        ],
        extra_link_args=[
            '-Wl,-rpath,$ORIGIN/torch/lib',  # Relative path to torch/lib in venv
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    },
    # install_requires=['torch>=2.0.0'],
    py_modules=['dist_chamfer_3D'],
)