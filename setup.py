from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'speed_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    #data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zajaczdia',
    maintainer_email='zajaczdiana@gmail.com',
    description='Kisbeadandó: Speed Monitor',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'speed_generator = speed_monitor.speed_generator:main',
            'speed_generator = speed_monitor.speed_generator:main',
        ],
    },
)
