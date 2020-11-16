# Ros2Tangle - Robot
A robot produces different data. In this example following ros topics are send to IOTA streams:
- /robot/state
- /robot/joint_states

You can list all available ros topics by executing
```bash
~/ros_ws$ rostopic list
```
and add topics you also want to publish to IOTA streams (by modifying ros2streams.py)

## Prerequisite
- ROS Workstation: is setup based on following instructions: [Link](https://sdk.rethinkrobotics.com/intera/Workstation_Setup#Install_ROS)\
All steps except *SETUP RVIZ* is needed
- Gazebo as the simulation environment: [Link](https://sdk.rethinkrobotics.com/intera/Gazebo_Tutorial)

## Usage
Set your device_id and your tangle gateway address in the launch file ros2tangle.launch

Navigate to the ros workspace folder 
```bash
cd ~/ros_ws 
```

Build your project
```bash
~/ros_ws$ catkin_make
```

Set the local ROS environment variables by executing following command 
```bash
~/ros_ws$ ./intera.sh sim
```

In the next step the the launch file is executed. This starts the pick-and-place demo and the ros2streams node
```bash
~/ros_ws$ roslaunch ros2tangle ros2tangle.launch
```

You should now see the Gazebo window where you see the robot that is trying to pick and place a red cube. 

![sawyer-gazebo-image](https://github.com/HackTheAlps/Ros2Tangle/blob/main/robot/Sawyer_Gazebo.jpg?raw=true)
