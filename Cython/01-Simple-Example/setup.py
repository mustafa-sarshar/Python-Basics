from distutils.core import setup
from Cython.Build import cythonize
from pathlib import Path

filename_cython_module = "cython_code.pyx"
file_address = Path(Path.cwd(), filename_cython_module)

if __name__ == "__main__":
    setup(ext_modules=cythonize(str(file_address)))

# Run the file via: $ python setup.py build_ext --inplace