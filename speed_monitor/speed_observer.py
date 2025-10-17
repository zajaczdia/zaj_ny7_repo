import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class SpeedObserver(Node):
    def __init__(self):
        super().__init__('speed_observer')
        self.subscription = self.create_subscription(Float32, 'speed_data', self.listener_callback, 10)
        self.alert_publisher = self.create_publisher(String, 'alert', 10)
        self.speed_limit = 90.0  # km/h
        self.get_logger().info('SpeedObserver node elindult.')

    def listener_callback(self, msg):
        speed = msg.data
        self.get_logger().info(f'Beérkező sebesség: {speed:.1f} km/h')

        if speed > self.speed_limit:
            alert_msg = String()
            alert_msg.data = f'SEBESSÉGTÚLLÉPÉS! {speed:.1f} km/h'
            self.alert_publisher.publish(alert_msg)
            self.get_logger().warn(alert_msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = SpeedObserver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
