import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

class TargetPublisher(Node):
    def __init__(self):
        super().__init__('target_publisher')
        self.publisher_ = self.create_publisher(Int8, '/target', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int8()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    target_publisher = TargetPublisher()
    rclpy.spin(target_publisher)
    target_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()