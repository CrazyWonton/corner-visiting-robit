#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

class goal_control():
    def __init__(self):
        rospy.on_shutdown(self.shutdown)
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.move_base.wait_for_server(rospy.Duration(10))

    def move(self, pos, quat):
        target = MoveBaseGoal()
        target.target_pose.header.frame_id = 'map'
        target.target_pose.header.stamp = rospy.Time.now()
        target.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000), Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))
        self.move_base.send_goal(target)
        self.move_base.wait_for_result(rospy.Duration(100))

    def shutdown(self):
        self.move_base.cancel_goal()
        
if __name__ == '__main__':
		rospy.init_node('navigation_tarczali', anonymous=False)
		goalControl = goal_control()

		position3 = {'x': 7.5, 'y' : 0}
		position1 = {'x': 1.9, 'y' : .3}
		position2 = {'x': 6.9, 'y' : -1.9}
		position4 = {'x': 8, 'y' : 3}
		quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}

		goalControl.move(position1, quaternion)
		goalControl.move(position2, quaternion)
		goalControl.move(position3, quaternion)
		goalControl.move(position4, quaternion)
