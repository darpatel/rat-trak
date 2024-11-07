import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Float32
from cv_bridge import CvBridge
import cv2

class RatTracker(Node):
    def __init__(self):
        super().__init__('rat_tracker')
        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            10
        )
        self.publisher_ = self.create_publisher(Float32, 'pwm_duty_cycle', 10)
        self.bridge = CvBridge()

        # Define grid sections (e.g., top, center, bottom) in pixels
        self.frame_height = 480  # Assuming 640x480 resolution from publisher
        self.top_grid = self.frame_height // 3
        self.bottom_grid = 2 * self.frame_height // 3

        # Motor control parameters
        self.duty_cycle = 0.6  # Increased for smooth, responsive movement
        self.motor_engaged_duty_cycle = 0.05  # Minimal engagement when in center grid

    def image_callback(self, msg):
        # Convert ROS image message to OpenCV format
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # Detect rat's position (you may need to adapt this method)
        rat_position_y = self.detect_rat(cv_image)

        # Determine motor direction based on rat's position in the frame
        if rat_position_y is not None:
            if rat_position_y < self.top_grid:
                # Rat in top grid; move motor counterclockwise
                self.publish_motor_command(-self.duty_cycle)
            elif rat_position_y > self.bottom_grid:
                # Rat in bottom grid; move motor clockwise
                self.publish_motor_command(self.duty_cycle)
            else:
                # Rat in center grid; engage motor slightly to reduce delay
                self.publish_motor_command(self.motor_engaged_duty_cycle)

    def detect_rat(self, frame):
        """
        Detect the rat's vertical position in the frame.
        Modify this function based on the detection method (e.g., color or contour).
        Returns the y-coordinate of the rat's position or None if not found.
        """
        # Convert to grayscale and apply thresholding for simple movement detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            # Assume the largest contour is the rat (adjust as needed)
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            rat_y = y + h // 2  # Center y-coordinate of the rat
            return rat_y
        return None

    def publish_motor_command(self, duty_cycle):
        """
        Publishes the PWM duty cycle for motor control.
        Positive for clockwise, negative for counterclockwise, minimal engagement when centered.
        """
        msg = Float32()
        msg.data = duty_cycle
        self.publisher_.publish(msg)
        direction = "Counterclockwise" if duty_cycle < 0 else "Clockwise" if duty_cycle > 0 else "Engaged, not moving"
        self.get_logger().info(f'Moving motor: {direction}, Duty Cycle: {abs(duty_cycle) * 100}%')

def main(args=None):
    rclpy.init(args=args)
    rat_tracker = RatTracker()
    rclpy.spin(rat_tracker)
    rat_tracker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
