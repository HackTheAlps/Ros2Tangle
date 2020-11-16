#! /usr/bin/env python

import rospy
import requests
import json
from sensor_msgs.msg import JointState
from intera_core_msgs.msg import RobotAssemblyState
from rospy_message_converter import json_message_converter
from std_msgs.msg import String
import datapublisher

class Ros2Streams(object):
    def __init__(self):
        url = rospy.get_param('~url')
        device_id = rospy.get_param('~device_id')
        self.datapub = datapublisher.DataPublisher(url, device_id)
        rospy.Subscriber("/robot/joint_states", JointState, self.send_jointstate_to_tangle, queue_size=1)
        rospy.Subscriber("/robot/state", RobotAssemblyState, self.send_state_to_tangle, queue_size=1)
   
    def send_jointstate_to_tangle(self, msg):
        self.datapub.send_message_to_tangle('joint_states', msg)

    def send_state_to_tangle(self, msg):
        self.datapub.send_message_to_tangle('state', msg)

if __name__ == '__main__':
    try:
        rospy.init_node('ros2tangle', anonymous=False)
        Ros2Streams()
        rospy.spin()
    except rospy.ROSInterruptException: pass










