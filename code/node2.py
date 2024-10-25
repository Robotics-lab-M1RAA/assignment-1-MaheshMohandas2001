#!/usr/bin/env python    
import rospy 
from std_msgs.msg import String 
def printer(msg):
    
    
    rospy.loginfo(msg) 
def M1RAA(): 
    rospy.init_node('M1RAA 2024')  
    pub1 = rospy.Publisher('welcome', String, queue_size=10)
    pub2 = rospy.Publisher('hello_college', String, queue_size=10) 
    rospy.Subscriber("hello_class", String, printer) 
    rate = rospy.Rate(10) 
    
    while not rospy.is_shutdown(): 
        msg1 = String() 
        msg2 = String() 
        msg1.data = "Hello mahesh welcome!" 
        msg2.data = "Hello CET!" 
        pub1.publish(msg1) 
        pub2.publish(msg2)
        rate.sleep() 
if __name__=='__main__': 
    try:
        M1RAA()
        
    except rospy.ROSInterruptException: 
        
     pass