# image_pub/publisher_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'image_raw', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # Publishes at 10 Hz
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)  # Adjust the index for your camera

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
