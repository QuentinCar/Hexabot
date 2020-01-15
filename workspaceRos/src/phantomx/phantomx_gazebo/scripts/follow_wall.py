#!/usr/bin/env python

import rospy
import numpy
from phantomx_gazebo.phantomx import PhantomX
from sensor_msgs.msg import LaserScan


class Follow_wall():
    def __init__(self, KP = 0.5, KI = 0.1):
        rospy.Subscriber('/scan', LaserScan, self._callback_scan)
        self.ranges = []
        self.scan_data = []
        self.KP = KP
        self.KI = KI
        self.time = float(rospy.Time.to_sec(rospy.Time.now()))


    def _callback_scan(self, msg):  
    	self.scan_data = [msg.header.stamp, msg.ranges] 
    	self.now = float(rospy.Time.to_sec(rospy.Time.now()))
        # self.ranges = msg.ranges
        # self.time = msg.header.stamp

    def follow_wall(self):
    	ranges = self.scan_data[1]
        d_wall = numpy.mean(ranges[70:95])
        d_desired = 1.2

        print("d_mur : ", d_mur)

        delta_t = (self.now - self.time)
        self.time = self.now
        P = d_wall - d_desired
        I = (d_wall - d_desired)*delta_t
        z = self.KI*I + self.KP*P
        sat = 0.5
        if z > sat :
            z = sat
        if z < -sat :
            z = -sat

        print("z : ",z)
        return z


if __name__ == '__main__':
    rospy.init_node('follow_wall')
    robot = PhantomX()
    follow = Follow_wall()
    rospy.sleep(1)


    while not rospy.is_shutdown():
        z = follow.follow_wall()
        robot.set_walk_velocity(0.5, 0, z)
        rospy.sleep(0.1)
