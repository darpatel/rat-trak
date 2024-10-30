import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rat-trak/rat-trak/ros2_ws/install/image_pub'
