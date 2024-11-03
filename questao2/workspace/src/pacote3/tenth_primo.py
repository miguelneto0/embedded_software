import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from pacote3.action import FindNthPrime
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSReliabilityPolicy
import math

class PrimeActionServer(Node):
    def __init__(self):
        super().__init__('prime_action_server')
        self.action_server = ActionServer(
            self,
            FindNthPrime,
            'find_nth_prime',
            self.execute_callback,
            goal_callback=self.handle_goal,
            cancel_callback=self.handle_cancel
        )
        self.get_logger().info('Prime action server started!')

    def handle_goal(self, goal_handle):
        self.get_logger().info(f'Received request to find the {goal_handle.request.n}th prime number.')
        return goal_handle.accept()

    def handle_cancel(self, goal_handle):
        self.get_logger().info('Cancel request received.')
        return goal_handle.cancel()

    def execute_callback(self, goal_handle):
        n = goal_handle.request.n
        primes_found = []
        candidate = 2  # Start from the first prime number

        while len(primes_found) < n:
            if self.is_prime(candidate):
                primes_found.append(candidate)
                
                # Feedback: envia o primo atual e a contagem
                feedback_msg = FindNthPrime.Feedback()
                feedback_msg.current_prime = candidate
                feedback_msg.current_count = len(primes_found)
                goal_handle.publish_feedback(feedback_msg)
                self.get_logger().info(f'Found prime {candidate} - Count: {len(primes_found)}')

            candidate += 1
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal was canceled.')
                return FindNthPrime.Result()

        # Resposta final com o número primo encontrado
        goal_handle.succeed()
        result = FindNthPrime.Result()
        result.result = primes_found[-1]
        self.get_logger().info(f'The {n}th prime number is {primes_found[-1]}.')
        return result

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

def main(args=None):
    rclpy.init(args=args)
    node = PrimeActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()