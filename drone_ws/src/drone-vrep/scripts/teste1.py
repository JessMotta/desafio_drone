#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Point
from sensor_msgs.msg import Range


class droneMove:

	def __init__(self):
	    self.sub_f = rospy.Subscriber('range_f', Range, self.callback0)
	    self.sub_d = rospy.Subscriber('range_d', Range, self.callback1)	
	    self.sub_e = rospy.Subscriber('range_e', Range, self.callback2)
	   # self.sub_t = rospy.Subscriber('range_t', Range, self.callback3)
	    self.pub = rospy.Publisher('chatter', Point, queue_size=10)

	def callback0(self, data): ## go foward
		self.rangeValorf = data.range
		print(self.rangeValorf)
		pontof = Point()
		if (self.rangeValorf > 1):
			pontof.x = 0.01
			pontof.y = 0.00
			self.pub.publish(pontof)
		else:
			pontof.x = 0.00
			pontof.y = 0.00
			self.pub.publish(pontof)
			

	def callback1(self, data): ## go to the right
		self.rangeValord = data.range
		print(self.rangeValord)
		pontod = Point()
		if (self.rangeValorf<=1 and self.rangeValord >= self.rangeValore):
			pontod.x = 0.00			
			pontod.y = -0.01
			self.pub.publish(pontod)
		#else:
		#	pontod.y = 0.00
		#	self.pub.publish(pontod)

	def callback2(self, data): ## go to the left
		self.rangeValore = data.range
		print(self.rangeValore)
		pontoe = Point()
		if (self.rangeValorf<=1 and self.rangeValord<self.rangeValord):
			pontoe.x = 0.00			
			pontoe.y = 0.01
			self.pub.publish(pontoe)
		#

		#	pontoe.y = 0.00
		#	self.pub.publish(pontoe)

	#def callback3(self, data): ## go back
	#	self.rangeValort = data.range
	#	print(self.rangeValort)
	#	pontot = Point()
	#	if (0.6<=self.rangeValorf<=1 and self.rangeValord == self.rangeValore and self.rangeValort>1):
	#		pontot.y = 0.00			
	#		pontot.x = -0.01
	#		self.pub.publish(pontot)
		#else:
		#	pontot.x = 0.00
		#	self.pub.publish(pontot)


if __name__ == "__main__":
	rospy.init_node('resolver')
	droneMove()
	rospy.spin()




