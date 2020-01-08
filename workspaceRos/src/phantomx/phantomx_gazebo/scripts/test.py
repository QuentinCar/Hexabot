#!/usr/bin/env python

import rospy
from phantomx_gazebo.phantomx import PhantomX

from sensor_msgs.msg import LaserScan


def _callback_scan(msg):
    ranges = msg.ranges

def follow_wall(ranges):
    d_mur = ranges[90]
    d_consigne = 0.8
    z = K*(d_consigne - d _mur)
    return z


if __name__ == '__main__':
    rospy.init_node('follow_wall')
    robot = PhantomX()
    rospy.sleep(1)

    rospy.Subscriber('/scan', LaserScan, _callback_scan)

    while not rospy.is_shutdown():
        z = follow_wall(ranges)
        robot.set_walk_velocity(1, 0, z)
        rospy.sleep()




# sens trigo départ devant.
# suivi de mur a gauche
# topic : /scan
# ranges[90] -> 