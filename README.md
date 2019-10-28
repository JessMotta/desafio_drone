# desafio_drone
Quadcopter programming by autonomous navigation with V-REP and ROS withou path planning in a random maze.



By: Jessica Motta
jessicalimamotta@gmail.com
Last Update: 10-27-2019
=============================================================


Objectives:
==========================================
    1. Make work the enviroments ROS and V-REP, together 
    2. Make the quadcopter flying in the randon maze avoiding the obstacles
    3. And made the quadcopter find the black box


V-REP SOFTWARE:

![Captura de tela de 2019-10-27 22-44-51](https://user-images.githubusercontent.com/30941796/67646292-2c51e880-f90c-11e9-9006-50e65036dd5b.png)





For initialization its required:
==========================================
    1. Linux OS
    2. ROS Melodic
    3. V-REP PRO EDU

All these softwares are free.


Let us start now:
============================================
    1. Open the folder: drone_ws in a terminal and type "catkin_make"
    2. Open one terminal and type "roscore"
    3. Than open V-REP in a terminal 
    4. Open the scene
    5. Start the simulation
    6. Open other terminal and type "rqt" -- this will show you the nodes in ROS
    7. Go back to the first terminal and type "cd src/drone-vrep/scripts/"
    8. Than type "sudo chmod +x teste1.py"
    9. Go back to the folder: drone_ws using command: "cd ../../../"
   10. Than type:"source devel/setup.bash" than type "rosrun drone-vrep resolver.py"


==============================================

The quadcopter has four proximity sensors to avoid obstacles: front, right, left and back to the quadcopter and two above him to identify the box in the maze.
 
 
ROS NODES:

In this image its possible to see all the nodes to publish and subscribe and the comunication between V-REP and ROS.


![Captura de tela de 2019-10-27 22-46-04](https://user-images.githubusercontent.com/30941796/67646398-b0a46b80-f90c-11e9-9103-2e5394c3513f.png)

 The /resolver its the node to read the range sensors and send the quadcopter to move.
 
 
 
 ===========================================
 
 
 For improve this work:
	For a better control recommend to use PID control or hybrid PID- Fuzzy control because this drone it's using proporcional control only and it isn't the better solution. 
  And insert better logic with the ranges of the sensors.
		 
