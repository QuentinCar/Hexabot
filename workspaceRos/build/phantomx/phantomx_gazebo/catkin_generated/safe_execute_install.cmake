execute_process(COMMAND "/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/build/phantomx/phantomx_gazebo/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/cyril/Documents/uv5.8/Hexabot/workspaceRos/build/phantomx/phantomx_gazebo/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
