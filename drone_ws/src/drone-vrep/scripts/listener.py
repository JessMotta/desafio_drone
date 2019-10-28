#!/usr/bin/env python


import rospy
from sensor_msgs.msg import Range

## print the range of the sensors: f,d,e and t
def callback0(data): 
   global range_f	
   rospy.loginfo(rospy.get_caller_id() + 'I heard front: %s', data.range)
   range_f =(data.range)
  
def callback1(data):
   global range_d 
   rospy.loginfo(rospy.get_caller_id() + 'I heard right: %s', data.range)
   range_d =(data.range) 

def callback2(data):
   global range_e 
   rospy.loginfo(rospy.get_caller_id() + 'I heard left: %s', data.range)
   range_e =(data.range) 

def callback3(data): 
   global range_t
   rospy.loginfo(rospy.get_caller_id() + 'I heard back: %s', data.range)
   range_t =(data.range) 


def listener():
   	
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener')
    global range_f	

## LEITURA DOS SENSORES ##
    sensor_f=rospy.Subscriber('range_f', Range, callback0)
    sensor_d=rospy.Subscriber('range_d', Range, callback1)
    sensor_e=rospy.Subscriber('range_e', Range, callback2)
    sensor_t=rospy.Subscriber('range_t', Range, callback3)



  #rospy.Subscriber('scan', Range, callback)
   # range_f = Range()
    #range_f.header.stamp = current_time
    #range_f.radiation_type = 'INFRARED=1'
    #range_f.field_of_view = 0
    #range_f.min_range = 0.0
    #range_f.max_range = 1.4
    #range_f.range = []

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
     listener()
