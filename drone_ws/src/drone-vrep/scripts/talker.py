#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Point

def talker():
    rospy.init_node('talker')
    
    pub = rospy.Publisher('chatter', Point, queue_size=10)    
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        ponto = Point()
        ponto.x = 0.01
        ponto.y = 0
        ponto.z = 0 

        pub.publish(ponto)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
