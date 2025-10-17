import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SpeedGenerator(Node):
    def __init__(self):
        super().__init__('speed_generator')
        self.publisher_ = self.create_publisher(Float32, 'speed_data', 10)
        timer_period = 0.5  # másodperc
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('SpeedGenerator node elindult.')

    def timer_callback(self):
        speed = random.uniform(0, 130)  # km/h
        msg = Float32()
        msg.data = speed
        self.publisher_.publish(msg)
        self.get_logger().info(f'Szimulált sebesség: {speed:.1f} km/h')


def main(args=None):
    rclpy.init(args=args)
    node = SpeedGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
