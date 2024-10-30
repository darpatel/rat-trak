# image_viewer/viewer_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        # Convert the ROS Image message to OpenCV format
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # Display the image in a window
        cv2.imshow("Image Viewer", cv_image)
        cv2.waitKey(1)  # Add a short delay to display the image

def main(args=None):
    rclpy.init(args=args)
    image_viewer = ImageViewer()
    rclpy.spin(image_viewer)
    image_viewer.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()  # Close OpenCV windows on shutdown

if __name__ == '__main__':
    main()
