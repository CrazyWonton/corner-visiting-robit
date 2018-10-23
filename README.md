# corner-visiting-robit
ROS package to have turtlebot visit corners and identify doors from a provided map

Assignment:
http://www.cs.binghamton.edu/~szhang/teaching/18fall/assignments/assign4.pdf

References:
C++ ref http://wiki.ros.org/navigation/Tutorials/SendingSimpleGoals
Python ref http://www.hotblackrobotics.com/en/blog/2018/01/29/action-client-py/
Basically what I have to do http://www.hotblackrobotics.com/en/blog/2018/01/29/seq-goals-py/

Plan:
Mapping done via teleop prior to autonomous navigation.
Publish goal messages of type geometry_msgs/PoseStamped to /move_base_simple/goal

Algorithm:
  List<PoseStamped> goals
  goals.add(corner1)
  goals.add(corner2)
  goals.add(corner3)
  goals.add(corner4)
  
  foreach(corner in goals)
    Publish(move_base_simple.goal,corner)
    while(goal is not reached){}
    goals.remove(0)
