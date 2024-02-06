import rclpy as rp
from rclpy.node import Node

from geometry_msgs.msg import Pose, Twist


class control(Node):

    def __init__(self):
        super().__init__('mobile_control')
        self.subscription = self.create_subscription(Twist, "/turtle1/pose", self.deisred_vel_callback, 10)

        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        timer_period = 0.5 #500ms
        self.timer = self.create_timer(timer_period, self.timer_callback)

    
    def deisred_vel_callback(self, msg):
        self.d_qb0 = msg.angular.z #desired base angular velocity
        self.d_qb1 = msg.linear.x #desired base linear velocity

    def wheel_control(self):
        r = 0.1 #wheel radius
        w = 0.1 #distance between the two wheel

        self.wheel_r = self.d_qb0 * w / 2 / r + self.d_qb1 / r
        self.heel_l = self.d_qb1 * 2 / r - self.wheel_r

    # def timer_callback(self):
        
def main(args=None):
    rp.init(args=args)

    turtlesim_publisher = control()
    rp.spin(turtlesim_publisher)

    turtlesim_publisher.destroy_node()
    rp.shutdown()


