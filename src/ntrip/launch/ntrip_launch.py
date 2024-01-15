import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        Node(
            package='ntrip',
            executable='ntrip',
            name='ntrip_client',
            output='screen',
            parameters=[
                {'ip': '3.143.243.81'},  # Change to the IP address of Your NTRIP service
                {'port': 2101},  # Change to your port number
                {'user': 'cmrdv'},  # Change to your username
                {'passwd': 'cmrdv'},  # Change to your password
                {'mountpoint': 'CMRDV'},  # Change to your mountpoint
                {'report_interval': 1} # the report interval to the NTRIP Caster, default is 1 sec
            ]
        ),
    ])
    
