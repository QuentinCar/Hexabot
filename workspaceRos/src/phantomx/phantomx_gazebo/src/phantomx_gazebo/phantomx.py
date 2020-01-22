import rospy
import cv2
import math
import time
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from phantomx_gazebo.msg import Fissures


class PhantomX:
    """Client ROS class for manipulating PhantomX in Gazebo"""

    def __init__(self, ns='/phantomx/', KP = 0.5, KI = 0.1):
        self.ns = ns
        self.joints = None
        self.angles = None

        self._sub_joints = rospy.Subscriber(
            ns + 'joint_states', JointState, self._cb_joints, queue_size=1)
        rospy.loginfo('Waiting for joints to be populated...')
        while not rospy.is_shutdown():
            if self.joints is not None:
                break
            rospy.sleep(0.1)
            rospy.loginfo('Waiting for joints to be populated...')
        rospy.loginfo('Joints populated')

        rospy.loginfo('Creating joint command publishers')
        self._pub_joints = {}
        for j in self.joints:
            p = rospy.Publisher(
                ns + j + '_position_controller/command', Float64, queue_size=1)
            self._pub_joints[j] = p
            
        self._pub_cmd_vel = rospy.Publisher(ns + 'cmd_vel', Twist, queue_size=1)
        self._pub_coord_fissures = rospy.Publisher(ns + 'fissures_coord', Fissures, queue_size=1)    
        self._bridge = CvBridge()
        self._image_sub = rospy.Subscriber("/hexabot/camera/image_raw", Image, self.camera_callback)

        rospy.Subscriber('/scan', LaserScan, self._callback_scan)
        self.scan_data = []
        self.KP = KP
        self.KI = KI
        self.time = float(rospy.Time.to_sec(rospy.Time.now()))



    def set_walk_velocity(self, x, y, t):
        msg = Twist()
        msg.linear.x = x
        msg.linear.y = y
        msg.angular.z = t
        self._pub_cmd_vel.publish(msg)
        
    def camera_callback(self, data):
        rospy.loginfo("Ok")
        cv_image = self._bridge.imgmsg_to_cv2(data, "bgr8")
        cv_edges = cv2.Canny(cv_image,6,16)
        if cv_edges !=[]:
            rospy.loginfo(cv_edges)
            ranges = self.scan_data[1]
            distance = np.mean(ranges[60:90])
            horizontal_fov = 0.616
            pixel_size = 2*distance*math.tan(horizontal_fov/2)/cv_edges.shape[1]
            coords = np.argwhere(cv_edges>0)*pixel_size
            msg = Fissures()
            msg.x = coords[:,0]
            msg.y = -distance
            msg.z = coords[:,1]
            self._pub_coord_fissures.publish(msg)
        

    def _callback_scan(self, msg):  
        self.scan_data = [msg.header.stamp, msg.ranges] 
        self.now = float(rospy.Time.to_sec(rospy.Time.now()))


    def _cb_joints(self, msg):
        if self.joints is None:
            self.joints = msg.name
        self.angles = msg.position

    def get_angles(self):
        if self.joints is None:
            return None
        if self.angles is None:
            return None
        return dict(zip(self.joints, self.angles))

    def set_angles(self, angles):
        for j, v in angles.items():
            if j not in self.joints:
                rospy.logerror('Invalid joint name "' + j + '"')
                continue
            self._pub_joints[j].publish(v)

    def set_angles_slow(self, stop_angles, delay=2):
        start_angles = self.get_angles()
        start = time.time()
        stop = start + delay
        r = rospy.Rate(100)
        while not rospy.is_shutdown():
            t = time.time()
            if t > stop:
                break
            ratio = (t - start) / delay
            angles = interpolate(stop_angles, start_angles, ratio)
            self.set_angles(angles)
            r.sleep()
            

    def follow_wall(self):
        ranges = self.scan_data[1]
        val1, val2 = np.mean(ranges[60:90]), np.mean(ranges[270:300])
        e = val1 - val2

        delta_t = (self.now - self.time)
        self.time = self.now

        P = e
        I = e*delta_t
        z = self.KI*I + self.KP*P

        saturation = 0.4
        # z = (z > saturation)*saturation + (z < -saturation)*(-saturation) + ((z <= saturation) and (z >= -saturation))*z
        z = min(max(z, -saturation), saturation)
        return z


def interpolate(anglesa, anglesb, coefa):
    z = {}
    joints = anglesa.keys()
    for j in joints:
        z[j] = anglesa[j] * coefa + anglesb[j] * (1 - coefa)
    return z


def get_distance(anglesa, anglesb):
    d = 0
    joints = anglesa.keys()
    if len(joints) == 0:
        return 0
    for j in joints:
        d += abs(anglesb[j] - anglesa[j])
    d /= len(joints)
    return d
