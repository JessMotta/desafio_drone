#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Point
from sensor_msgs.msg import Range


def callback0(data): 
   global range_f	
   rospy.loginfo(rospy.get_caller_id() + 'I heard front: %s', data.range)
   range_f =(data.range)

   if range_f>=1:
      
      ponto.x = 0.01
      ponto.y = 0
      ponto.z = 0 

      pub.publish(ponto)
      #rate.sleep()
        

#--------------------------------------------------------------------------

sensor_f=rospy.Subscriber('range_f', Range, callback0)
#sensor_d=rospy.Subscriber('range_d', Range, callback1)
#sensor_e=rospy.Subscriber('range_e', Range, callback2)
#sensor_t=rospy.Subscriber('range_t', Range, callback3)

    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

rospy.init_node('resolver')	
#def talker():
pub = rospy.Publisher('chatter', Point, queue_size=10)    
rate = rospy.Rate(10) # 10h
ponto = Point()

rospy.spin()
#--------------------------------------------------------------------------

