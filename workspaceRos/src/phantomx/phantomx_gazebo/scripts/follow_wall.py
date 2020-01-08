#!/usr/bin/env python

import rospy
from phantomx_gazebo.phantomx import PhantomX

from sensor_msgs.msg import LaserScan


class Follow_wall():
    def __init__(self, K = 1):
        rospy.Subscriber('/scan', LaserScan, self._callback_scan)
        self.ranges = []
        self.K = K


    def _callback_scan(self, msg):
        
        self.ranges = msg.ranges

    def follow_wall(self):
        d_mur = self.ranges[90]
        d_consigne = 0.8
        z = self.K*(d_mur - d_consigne)
        if z > 1 :
            z = 1
        if z < -1 :
            z = -1
        return z


if __name__ == '__main__':
    rospy.init_node('follow_wall')
    robot = PhantomX()
    follow = Follow_wall()
    rospy.sleep(1)


    while not rospy.is_shutdown():
        z = follow.follow_wall()
        robot.set_walk_velocity(0.5, 0, z)
        print(z)
        rospy.sleep(0.1)
