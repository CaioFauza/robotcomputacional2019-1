#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import UInt8

v = 0.1  # Velocidade linear
w = 0.4 # Velocidade angular
d = 0
andando = False

def sensor(dado):
    global d
    d = dado.data


if __name__ == "__main__":
    rospy.init_node("atividade1")
    velocidade = rospy.Publisher("cmd_vel", Twist, queue_size=3)
    recebe_bump = rospy.Subscriber("/bumper", UInt8, sensor)

    try:
        while not rospy.is_shutdown():
            while not andando:
                velocidade.publish(Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0)))
                rospy.sleep(1.0) 

                if d == 2:
                    print("Batida, back")
                    velocidade.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))) 
                    velocidade.publish(Twist(Vector3(-0.1, 0, 0), Vector3(0, 0, 0.35)))
                    rospy.sleep(3.0)
                    velocidade.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, 0)))
                    rospy.sleep(1.0)
                    d = None

                if d == 1:
                    print("Batida, back")
                    velocidade.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, 0)))
                    velocidade.publish(Twist(Vector3(-0.1, 0, 0), Vector3(0, 0, -0.35)))
                    rospy.sleep(3.0)
                    velocidade.publish(Twist(Vector3(0, 0, 0), Vector3(0, 0, 0)))
                    rospy.sleep(1.0)
                    d = None

                if d == 3:
                    print("Batida, run")
                    velocidade.publish(Twist(Vector3(0.4, 0, 0), Vector3(0, 0, 0)))
                    rospy.sleep(2.0)
                    d = None

                if d == 4:
                    print("Batida, run")
                    velocidade.publish(Twist(Vector3(0.4, 0, 0), Vector3(0, 0, 0)))
                    rospy.sleep(2.0)
                    d = None
                    



           
    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")
