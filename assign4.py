#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
import sys
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

class GoToPose():
    def __init__(self):

        self.goal_sent = False
    
        # What to do if shut down (e.g. Ctrl-C or failure)
        rospy.on_shutdown(self.shutdown)
    
        # Tell the action client that we want to spin a thread by default
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Wait for the action server to come up")
    
        # Allow up to 5 seconds for the action server to come up
        self.move_base.wait_for_server(rospy.Duration(5))

    def goto(self, pos, quat):

        # Send a goal
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000), Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))
    
        # Start moving
        self.move_base.send_goal(goal)
    
        # Allow TurtleBot up to 60 seconds to complete task
        success = self.move_base.wait_for_result(rospy.Duration(60)) 
    
        state = self.move_base.get_state()
        result = False
    
        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
        else:
            self.move_base.cancel_goal()
    
            self.goal_sent = False
            return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':
	try:
		rospy.init_node('nav_test', anonymous=False)
		navigator = GoToPose()

		# Customize the following values so they are appropriate for your location
		position3 = {'x': 7.5, 'y' : 0}
	    	position1 = {'x': 1.9, 'y' : .3}
	    	position2 = {'x': 6.9, 'y' : -1.9}
	    	position4 = {'x': 8, 'y' : 3}
		quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}
	    


		success = navigator.goto(position1, quaternion)
		success = navigator.goto(position2, quaternion)
		success = navigator.goto(position3, quaternion)
		success = navigator.goto(position4, quaternion)

				
	except rospy.ROSInterruptException:
		rospy.loginfo("Ctrl-C caught. Quitting")
	
