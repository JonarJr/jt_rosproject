# jt_rosproject
Final ROS Project
Jonas Tjahjadi
11/26/2017
Autonomous Robotics Lab
ROS Programming Project

Purpose: This is a culminating project that finishes up

How to Use:
Basics:
Firstly, make sure that you have an Ubuntu system that has installed ROS Kinetic. Next, make sure that you have your environment variables configured for your terminal
(usually put it in bash). Lastly, make sure you have your catkin workspace created, and note that there are no external dependencies for this project so you do not have to
install anything else.

Using the package:
Download and put my whole ros_programming_assignment package in your catkin_ws/src. It comes with a launch file, so all you have to do is run a catkin_make in your root folder and:
	roslaunch ros_programming_assignment jt_rosproject.launch
and you will be prompted by the console for a command. You can test the functionality by running:
	roslaunch turtlebot3_gazebo turtlebot3_world.launch
	rostopic list
	rosmsg show (any message that is unfamiliar to you)
	rostopic echo /cmd_vel (and in the console terminal, enter any command)

Settings:
Turn has been the only implemented command for proof of concept (since the important part is understanding ROS basic concepts). In the future, more commands may be implemented
by creating a better Fake_NLP node and then sending different goal types (using possibly a header) to the action. Room and modularity has encouraged that.  
Lastly, you may notice that my project turns a robot at 1 degree per second (which is really slow), and that if you do any decimals it's not so precise. 
I have acknowledged that, so in my action server, you are allowed to increase the rate by adjusting the increment_value and sleep_value just at the top. For accurate updates, though, 
you will have to fix the math behind the feedback.movement_progress so it's sending you the right information. (current_movement must also be changed with respect to your degrees/second rate)
