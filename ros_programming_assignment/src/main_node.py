#!/usr/bin/env python

#Created by Jonas Tjahjadi on 11/26/2017 as part of the ROS Programming Assignment

#imports
import rospy
import actionlib
from std_msgs.msg import String, Float32
from ros_programming_assignment.srv import FakeNLP
from ros_programming_assignment.msg import TwisterAction, TwisterGoal, TwisterResult, TwisterFeedback

class MainNode():
	#CONSTRUCTOR
	def __init__(self, name):
		#initialize subscriber, service client, and action client
		self.sub = rospy.Subscriber('/demo/command', String, self.ui_callback)
		self.float_processor = rospy.ServiceProxy('fake_nlp', FakeNLP)
		self.client = actionlib.SimpleActionClient('twister', TwisterAction)

	#subscriber callback which also calls a service and an action
	def ui_callback(self, msg):
		print "USER ENTERED: " + msg.data

		###SERVICE CALL###
		#send string to service and get the float value back
		rospy.wait_for_service('fake_nlp')
		#declare the service proxy
		float_data = self.float_processor(msg.data)
		print "Processed string and received '" + str(float_data.count) + "' from FakeNLP service."
		
		###ACTION CALL###
		#send goal created by to action, declaring client
		self.client.wait_for_server()
		goal = TwisterGoal()
		goal.movement = float_data.count
		self.client.send_goal(goal, feedback_cb=self.feedback_cb)
	
		###FINISH AND DISPLAY RESULTS###
		self.client.wait_for_result()
		self.display_results()

	#feedback callback function, what to do with the data
	def feedback_cb(self, feedback):
		print('[Feedback] Current movement: %f'%(feedback.movement_progress))
		print('[Feedback] Movement remaining: %f'%(feedback.movement_remaining))
		print

	#display results
	def display_results(self):
		print('[Result] State: %d'%(self.client.get_state()))
		print('[Result] Status: %s'%(self.client.get_goal_status_text()))
		print('[Result] Movement Total: %f'%(self.client.get_result().movement_progress))
		print('[Result] Updates sent: %d'%(self.client.get_result().updates_sent))
		print "Please enter a command for the TurtleBot3 below: (Ctrl-C and ENTER to exit) "

#initialize node and create instance of main node
if __name__ == '__main__':
	rospy.init_node('MainNode')
	MainNode('/demo/command')
	rospy.spin()
