cmake_minimum_required(VERSION 2.8.3)
project(ros2tangle)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

#add_message_files(
# FILES
#)

#generate_messages(
#  DEPENDENCIES
#  std_msgs
#)

catkin_package(
  CATKIN_DEPENDS 
  message_runtime
)

catkin_package(
  LIBRARIES ros2tangle
  CATKIN_DEPENDS roscpp rospy std_msgs
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)

