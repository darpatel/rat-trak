from setuptools import find_packages, setup

package_name = 'motor_control_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='drshnptl',
    maintainer_email='drshnptl24@gmail.com',
    description='Package to control motor using PWM and ROS 2 node',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pwm_controller = motor_control_pkg.pwm_controller:main'
        ],
    },
)
