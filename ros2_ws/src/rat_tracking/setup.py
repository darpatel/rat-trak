from setuptools import find_packages, setup

package_name = 'rat_tracking'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'opencv-python', 'rclpy'],
    zip_safe=True,
    maintainer='pullen65',
    maintainer_email='pullen65@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rat_tracker = rat_tracking.rat_tracker:main',
        ],
    },
)
