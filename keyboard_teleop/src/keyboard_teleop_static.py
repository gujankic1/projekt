#!/usr/bin/env python

import rospy
import pygame
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    rospy.init_node('keyboard_teleop')
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['basepos_q1', 'basepos_q2', 'bodyaxis_q3', 'shoulder_q4','shoulder_q5', 'shoulder_q6', 'elbow_q7', 'wrist_q8', 'wrist_q9', 'finger_moving_joint']
    hello_str.position = [1, -2, 1.75, 1, 0.7, 0.12, -1, 0.3, 0.6, -0.1]
    hello_str.velocity = []
    hello_str.effort = []
    while not rospy.is_shutdown():
      hello_str.header.stamp = rospy.Time.now()
      pub.publish(hello_str)
      rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



