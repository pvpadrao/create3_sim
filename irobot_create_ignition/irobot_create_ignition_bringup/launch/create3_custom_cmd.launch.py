from launch import LaunchDescription
from launch.substitutions import FindExecutable
from launch.actions import ExecuteProcess
from time import sleep

def generate_launch_description():
    ld = LaunchDescription()


    undock=ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " action send_goal ",
            "/undock ",
            "irobot_create_msgs/action/UnDock ",
            '"{}"',
        ]],
        shell=True
        )
    
    dock=ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " action send_goal ",
            "/dock ",
            "irobot_create_msgs/action/Dock ",
            '"{}"',
        ]],
        shell=True
        )
    
    move_forward=ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " action send_goal ",
            "/drive_distance ",
            "irobot_create_msgs/action/DriveDistance ",
            '"{distance: 0.5,max_translation_speed: 1.0}"',
        ]],
        shell=True
        )
    

    move_fwd=ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " topic pub ",
            "/cmd_vel ",
            "geometry_msgs/msg/Twist ",
            '"{linear: {x: -1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"',
        ]],
        shell=True
        )
    
    stop=ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " topic pub ",
            "/cmd_vel ",
            "geometry_msgs/msg/Twist ",
            '"{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"',
        ]],
        shell=True
        )
    
    

    rotate_ccw=ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " action send_goal ",
            "/rotate_angle ",
            "irobot_create_msgs/action/RotateAngle ",
            '"{angle: 1.57,max_rotation_speed: 0.5}"',
        ]],
        shell=True
        )
    
    rotate_cw=ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            " action send_goal ",
            "/rotate_angle ",
            "irobot_create_msgs/action/RotateAngle ",
            '"{angle: -1.57,max_rotation_speed: 0.5}"',
        ]],
        shell=True
        )


    #ld.add_action(undock)
    #sleep(5)
    
    ld.add_action(move_fwd)
    #sleep(3)
    #ld.add_action(stop)
    return ld