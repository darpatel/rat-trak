# image_pub/publisher_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from rclpy.qos import qos_profile_sensor_data


class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'image_raw', qos_profile_sensor_data)
        self.fps = 60
        self.timer = self.create_timer(1.0 / self.fps, self.timer_callback)
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)  # Adjust the index for your camera
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.cap.set(cv2.CAP_PROP_FPS, 10)  # Or another value that matches your processing power

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the image to ROS Image message and publish
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing image frame')

    def destroy_node(self):
        super().destroy_node()
        self.cap.release()  # Ensure the camera is released on shutdown

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
