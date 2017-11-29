#!/usr/bin/env python

#Created by Jonas Tjahjadi on 11/26/2017 as part of the ROS Programming Assignment

#imports
import rospy
from std_msgs.msg import String

#initialize node, ongoing asker and feeder for the main_node
rospy.init_node('ConsoleNode')
print "Please enter a command for the TurtleBot3: (Ctrl-C and ENTER to exit)"
#indicate that it will have a publishing behavior
consolePub = rospy.Publisher('/demo/command', String, queue_size = 1)

#while node is running ask for user input so that it can be processed by main_node
while not rospy.is_shutdown():
	msg = String()
	msg.data = raw_input()
	consolePub.publish(msg.data)
