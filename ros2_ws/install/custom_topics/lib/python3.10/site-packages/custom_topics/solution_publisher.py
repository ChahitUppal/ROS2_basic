# solution_publisher.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8MultiArray, Int8

class SolutionPublisher(Node):
    def __init__(self):
        super().__init__('solution_publisher')
        self.input_subscription = self.create_subscription(
            Int8MultiArray,
            '/input',
            self.input_callback,
            10)
        self.target_subscription = self.create_subscription(
            Int8,
            '/target',
            self.target_callback,
            10)

        self.input_array = []
        self.target_value = None

    def input_callback(self, msg):
        self.input_array = msg.data
        self.check_solution()

    def target_callback(self, msg):
        self.target_value = msg.data
        self.check_solution()

    def check_solution(self):
        if self.input_array and self.target_value is not None:
            for i in range(len(self.input_array)):
                for j in range(i + 1, len(self.input_array)):
                    if self.input_array[i] + self.input_array[j] == self.target_value:
                        # Publish the solution
                        solution_msg = Int8MultiArray()
                        solution_msg.data = [i, j]
                        self.get_logger().info(f'Solution found: indices {i} and {j}')
                        self.publish_solution(solution_msg)
                        return  # Exit after finding the first solution

    def publish_solution(self, solution_msg):
        # Create a publisher for the solution
        solution_publisher = self.create_publisher(Int8MultiArray, '/solution', 10)
        solution_publisher.publish(solution_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SolutionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()