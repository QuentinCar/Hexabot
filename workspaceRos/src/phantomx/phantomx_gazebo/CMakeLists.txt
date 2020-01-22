cmake_minimum_required(VERSION 2.8.3)
project(phantomx_gazebo)

# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED COMPONENTS 
  rospy
  std_msgs
  geometry_msgs
  sensor_msgs
  gazebo_ros  
  message_generation
  roscpp
  visualization_msgs
)

find_package(Boost REQUIRED COMPONENTS system)
find_package(gazebo REQUIRED)

catkin_python_setup()

add_message_files(
	FILES
	Fissures.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  )

catkin_package(
  CATKIN_DEPENDS
    message_runtime 
    sensor_msgs
    gazebo_ros 
    hector_gazebo_plugins
  DEPENDS 
    gazebo
)


add_executable(marker_display src/phantomx_gazebo/marker_display.cpp)

target_link_libraries(marker_display ${catkin_LIBRARIES})