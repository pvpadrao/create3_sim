from launch import LaunchDescription
from launch.substitutions import FindExecutable
from launch.actions import ExecuteProcess

def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(
    ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " action send_goal ",
            "/dock ",
            "irobot_create_msgs/action/Dock ",
            '"{}"',
        ]],
        shell=True
    )
)

    return ld