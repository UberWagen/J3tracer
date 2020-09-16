#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub  = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('simple_publisher', anonymous=True) 
    rate = rospy.Rate(10)
    counter = 0
    
    while not rospy.is_shutdown():
        count_str = "Publishing %d"%counter
        counter += 1
        rospy.loginfo(count_str)
        pub.publish(count_str)
        rate.sleep()

if __name__ == "__main__":
    try: 
        publisher()
    except rospy.ROSInterruptException:
        pass          