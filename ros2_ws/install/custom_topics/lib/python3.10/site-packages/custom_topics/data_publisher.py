# data_publisher.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8MultiArray, Int8
import random

class DataPublisher(Node):
    def __init__(self):
        super().__init__('data_publisher')
        
        # Generate random data once
        self.input_array = [random.randint(1, 20) for _ in range(5)]
        
        # Ensure there's always a solution
        index1, index2 = random.sample(range(5), 2)  # Pick two distinct indices
        self.target_value = self.input_array[index1] + self.input_array[index2]

        self.input_publisher = self.create_publisher(Int8MultiArray, '/input', 10)
        self.target_publisher = self.create_publisher(Int8, '/target', 10)
        self.timer = self.create_timer(1.0, self.publish_data)  # Publish at 1 Hz

    def publish_data(self):
        # Publish input array
        input_msg = Int8MultiArray()
        input_msg.data = self.input_array
        self.input_publisher.publish(input_msg)
        self.get_logger().info(f'Published input: {self.input_array}')

        # Publish target
        target_msg = Int8()
        target_msg.data = self.target_value
        self.target_publisher.publish(target_msg)
        self.get_logger().info(f'Published target: {self.target_value}')

def main(args=None):
    rclpy.init(args=args)
    node = DataPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()