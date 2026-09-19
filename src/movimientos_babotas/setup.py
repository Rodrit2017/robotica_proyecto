import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'movimientos_babotas' # Cambia a 'lab3' si estás trabajando en otro paquete

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Inclusión de carpetas para URDF, configuraciones, launch y mallas
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.stl'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='toxiro',
    maintainer_email='rodrigo.saavedra@utec.edu.pe',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Ejemplo de cómo registrar un nodo cuando lo crees:
            # 'nombre_ejecutable = movimientos_babotas.nombre_script:main',
        ],
    },
)