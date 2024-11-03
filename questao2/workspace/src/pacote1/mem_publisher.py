import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil  # Biblioteca para informações de sistema

class MemPublisher(Node):
    def __init__(self):
        super().__init__('mem_publisher')
        self.publisher_ = self.create_publisher(String, 'memory_info', 10)
        self.timer = self.create_timer(1.0, self.publish_memory_info)

    def publish_memory_info(self):
        memory = psutil.virtual_memory()
        memory_info = f'Total: {memory.total / (1024 ** 3):.2f} GB, Used: {memory.percent}%'
        msg = String()
        msg.data = memory_info
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = MemPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
