#!/usr/bin/env python3

import rospy
import math as m

from geometry_msgs.msg import Twist


class Turtle(object):

    def __init__(self):
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        self.angels = 0
        self.rate = rospy.Rate(10)
        

    def turtle_forward(self, side, x_v):
        turtle_twist = Twist()
        turtle_twist.linear.x = x_v
        
        t0 = rospy.Time.now().to_sec()
        current_dist = 0
        
        while(current_dist < side):
            self.pub.publish(turtle_twist)            
            t1 = rospy.Time.now().to_sec()
            current_dist = x_v*(t1-t0)
  
        turtle_twist.linear.x = 0.0
        self.pub.publish(turtle_twist)

        
    def turtle_rotate(self, angle, ang_v):
        turtle_twist = Twist()
        turtle_twist.angular.z = ang_v
        t0 = rospy.Time.now().to_sec()
        current_ang = 0
        
        while(current_ang < angle): 
            self.pub.publish(turtle_twist)
            t1 = rospy.Time.now().to_sec()
            current_ang = ang_v*(t1-t0)

        turtle_twist.angular.z = 0.0
        self.pub.publish(turtle_twist)

        
    def square(self, sq_side, x_v, ang_v):
        # ANG_TIME = m.radians(90)/ang_v
        SQUARE_ANGLE = m.radians(90)
        # rate = rospy.Rate(1/ANG_TIME)

        while not rospy.is_shutdown():
            
            self.turtle_forward(sq_side, x_v)
            self.turtle_rotate(SQUARE_ANGLE, ang_v)

if __name__ == '__main__':
    try:
        sq_side = float(input('Введите длину стороны квадрата:'))
        x_v = float(input('Введите скорость движения черепахи:'))
        ang_v = float(input('Введите скорость поворота черепахи:'))
        rospy.init_node('Turtle_p')
        turtle = Turtle()
        turtle.square(sq_side, x_v, ang_v)


    except rospy.ROSInterruptException:
        pass
    

# !/usr/bin/env python3

# import rospy
# from geometry_msgs.msg import Twist
# import math

# def paramet_angl(angl):
#     turn_angle = math.radians(angl)
#     return turn_angle


# def speed_paramet(vel, linvel=0, angvel=0):
#     vel.linear.x = linvel
#     vel.angular.z = angvel
#     return vel


# def move_tertle(line_vel,ang_vel):
#     rospy.init_node('turtmove', anonymous=True)
#     pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
#     rate = rospy.Rate(1)
#     vel = Twist()
#     ang_vel = paramet_angl(ang_vel)

#     while not rospy.is_shutdown():
#         pub.publish(speed_paramet(vel, linvel = line_vel))
#         rate.sleep()
#         pub.publish(speed_paramet(vel, angvel = ang_vel))
#         rate.sleep()


# if __name__ == '__main__':
#     move_tertle(4,90)
        
            