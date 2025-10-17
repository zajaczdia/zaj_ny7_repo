from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='speed_monitor',
            executable='speed_generator',
            name='speed_generator'
        ),
        Node(
            package='speed_monitor',
            executable='speed_observer',
            name='speed_observer'
        )
    ])
