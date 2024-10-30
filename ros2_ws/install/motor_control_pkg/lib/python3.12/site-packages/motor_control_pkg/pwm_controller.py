import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class PWMController(Node):
    def __init__(self):
        super().__init__('pwm_controller')
        self.publisher_ = self.create_publisher(Float32, 'pwm_duty_cycle', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.publish_duty_cycle)
        self.duty_cycle = 0.5  # 50% duty cycle

    def publish_duty_cycle(self):
        msg = Float32()
        msg.data = self.duty_cycle
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing Duty Cycle: {msg.data * 100}%')

def main(args=None):
    rclpy.init(args=args)
    pwm_controller = PWMController()
    rclpy.spin(pwm_controller)
    pwm_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
