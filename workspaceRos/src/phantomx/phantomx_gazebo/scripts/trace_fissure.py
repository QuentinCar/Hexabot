#!/usr/bin/env python

# Import required Python code.
import roslib
roslib.load_manifest('node_example')
import rospy

def Callback(data):
    rospy.loginfo(rospy.get_name() + " I heard %s", data.message)

def trace_fissure():
    topic = rospy.get_param('~topic', 'chatter')
    rospy.Subscriber(topic, PoseStamped, Callback)
	rate = float(rospy.get_param('~rate', '1.0'))
    
    while not rospy.is_shutdown():
		rospy.sleep(1/rate)

if __name__ == '__main__':
    rospy.init_node('trace_fissure', anonymous = True)
    trace_fissure()
