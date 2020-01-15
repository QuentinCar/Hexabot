#!/usr/bin/env python

import rospy
from phantomx_gazebo.phantomx import PhantomX


if __name__ == '__main__':
    rospy.init_node('follow_wall')
    robot = PhantomX()
    rospy.sleep(1)

    while not rospy.is_shutdown():
        z = robot.follow_wall()
        robot.set_walk_velocity(0.6, 0, z)
        rospy.sleep(0.1)
