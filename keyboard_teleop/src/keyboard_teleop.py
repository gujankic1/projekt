#!/usr/bin/env python

import rospy
try:
	import pygame
	from pygame.locals import *
	HAVE_PYGAME=True
except ImportError:
	HAVE_PYGAME=False
import numpy as np
from sensor_msgs.msg import JointState
from std_msgs.msg import Header


def talker():
	rospy.init_node('keyboard_teleop')
	pub = rospy.Publisher('joint_states', JointState, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	if HAVE_PYGAME:
		pygame.init()

		screen = pygame.display.set_mode((630,600))
		pygame.display.set_caption('Human arm D-H coordinates')
		myFont = pygame.font.SysFont('Arial',20)
		clock = pygame.time.Clock()

		joints = np.zeros(10)

		limits_l = np.zeros(10)
		limits_u = np.zeros(10)

		change_speed=0.05

		white=(255,255,255)
		green=(144,238,144)
		red=(205,92,92)

		limits_l[0] = -3        # basepos_q1
		limits_l[1] = -3        # basepos_q2
		limits_l[2] = 0         # bodyaxis_q3
		limits_l[3] = -1.57     # shoulder_q4
		limits_l[4] = -1.57     # shoulder_q5
		limits_l[5] = -2.041    # shoulder_q6
		limits_l[6] = -2.355    # elbow_q7
		limits_l[7] = -1.57     # wrist_q8
		limits_l[8] = -1.57     # wrist_q9
		limits_l[9] = -0.785    # finger_moving_joint

		limits_u[0] = 3         # basepos_q1
		limits_u[1] = 3         # basepos_q2
		limits_u[2] = 6.28      # bodyaxis_q3
		limits_u[3] = 1.57      # shoulder_q4
		limits_u[4] = 1.57      # shoulder_q5
		limits_u[5] = 0.785     # shoulder_q6
		limits_u[6] = 0         # elbow_q7
		limits_u[7] = 1.57      # wrist_q8
		limits_u[8] = 1.57      # wrist_q9
		limits_u[9] = 0         # finger_moving_joint


	hello_str = JointState()
	hello_str.header = Header()
	hello_str.header.stamp = rospy.Time.now()
	hello_str.name = ['basepos_q1', 'basepos_q2', 'bodyaxis_q3', 'shoulder_q4','shoulder_q5', 'shoulder_q6', 'elbow_q7', 'wrist_q8', 'wrist_q9', 'finger_moving_joint']
	hello_str.position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	hello_str.velocity = []
	hello_str.effort = []
	while True and not rospy.is_shutdown():
		hello_str.header.stamp = rospy.Time.now()
		if HAVE_PYGAME:
			pygame.event.pump()
			keys = pygame.key.get_pressed()
			# basepos_q1
			if keys[K_a]:
				if joints[0] <= limits_l[0]:
				    joints[0] = limits_l[0]
				else:
				    joints[0] -= change_speed

			if keys[K_q]:
				if joints[0] >= limits_u[0]:
				    joints[0] = limits_u[0]
				else:
				    joints[0] += change_speed

			# basepos_q2
			if keys[K_s]:
				if joints[1] <= limits_l[1]:
				    joints[1] = limits_l[1]
				else:
				    joints[1] -= change_speed

			if keys[K_w]:
				if joints[1] >= limits_u[1]:
				    joints[1] = limits_u[1]
				else:
				    joints[1] += change_speed

			# bodyaxis_q3
			if keys[K_d]:
				if joints[2] <= limits_l[2]:
				    joints[2] = limits_l[2]
				else:
				    joints[2] -= change_speed

			if keys[K_e]:
				if joints[2] >= limits_u[2]:
				    joints[2] = limits_u[2]
				else:
				    joints[2] += change_speed

			# shoulder_q4
			if keys[K_f]:
				if joints[3] <= limits_l[3]:
				    joints[3] = limits_l[3]
				else:
				    joints[3] -= change_speed

			if keys[K_r]:
				if joints[3] >= limits_u[3]:
				    joints[3] = limits_u[3]
				else:
				    joints[3] += change_speed

			# shoulder_q5
			if keys[K_g]:
				if joints[4] <= limits_l[4]:
				    joints[4] = limits_l[4]
				else:
				    joints[4] -= change_speed

			if keys[K_t]:
				if joints[4] >= limits_u[4]:
				    joints[4] = limits_u[4]
				else:
				    joints[4] += change_speed

			# shoulder_q6
			if keys[K_h]:
				if joints[5] <= limits_l[5]:
				    joints[5] = limits_l[5]
				else:
				    joints[5] -= change_speed

			if keys[K_z]:
				if joints[5] >= limits_u[5]:
				    joints[5] = limits_u[5]
				else:
				    joints[5] += change_speed

			# elbow_q7
			if keys[K_j]:
				if joints[6] <= limits_l[6]:
				    joints[6] = limits_l[6]
				else:
				    joints[6] -= change_speed

			if keys[K_u]:
				if joints[6] >= limits_u[6]:
				    joints[6] = limits_u[6]
				else:
				    joints[6] += change_speed

			# wrist_q8
			if keys[K_k]:
				if joints[7] <= limits_l[7]:
				    joints[7] = limits_l[7]
				else:
				    joints[7] -= change_speed

			if keys[K_i]:
				if joints[7] >= limits_u[7]:
				    joints[7] = limits_u[7]
				else:
				    joints[7] += change_speed

			# wrist_q9
			if keys[K_l]:
				if joints[8] <= limits_l[8]:
				    joints[8] = limits_l[8]
				else:
				    joints[8] -= change_speed

			if keys[K_o]:
				if joints[8] >= limits_u[8]:
				    joints[8] = limits_u[8]
				else:
				    joints[8] += change_speed

			# finger_moving_joint
			if keys[K_DOWN]:
				if joints[9] <= limits_l[9]:
				    joints[9] = limits_l[9]
				else:
				    joints[9] -= change_speed

			if keys[K_UP]:
				if joints[9] >= limits_u[9]:
				    joints[9] = limits_u[9]
				else:
				    joints[9] += change_speed

			if keys[K_ESCAPE]:
				break

			#print(joints)

			text_q1 = myFont.render('q1 = %.3f [m]'%joints[0], True, white)
			text_q1_desc = myFont.render('Base position Z_0', True, green)
			text_q2 = myFont.render('q2 = %.3f [m]' % joints[1], True, white)
			text_q2_desc = myFont.render('Base position X_0', True, green)
			text_q3 = myFont.render('q3 = %.3f [rad]' % joints[2], True, white)
			text_q3_desc = myFont.render('Vertical body axis rotation', True, green)
			text_q4 = myFont.render('q4 = %.3f [rad]' % joints[3], True, white)
			text_q4_desc = myFont.render('Shoulder rotation', True, green)
			text_q5 = myFont.render('q5 = %.3f [rad]' % joints[4], True, white)
			text_q5_desc = myFont.render('Shoulder vertical flexion', True, green)
			text_q6 = myFont.render('q6 = %.3f [rad]' % joints[5], True, white)
			text_q6_desc = myFont.render('Shoulder horizontal flexion', True, green)
			text_q7 = myFont.render('q7 = %.3f [rad]' % joints[6], True, white)
			text_q7_desc = myFont.render('Elbow flexion', True, green)
			text_q8 = myFont.render('q8 = %.3f [rad]' % joints[7], True, white)
			text_q8_desc = myFont.render('Wrist rotation', True, green)
			text_q9 = myFont.render('q9 = %.3f [rad]' % joints[8], True, white)
			text_q9_desc = myFont.render('Wrist flexion', True, green)
			text_q10 = myFont.render('q10 = %.3f [rad]' % joints[9], True, white)
			text_q10_desc = myFont.render('Finger closure', True, green)
			text_esc= myFont.render('Press [ESC] to quit', True, red)


			screen.fill((0, 0, 0))

			screen.blit(text_esc, (200,10))

			screen.blit(text_q1_desc, (50, 50))
			screen.blit(text_q1, (50, 100))
			screen.blit(text_q2_desc, (50, 150))
			screen.blit(text_q2, (50, 200))
			screen.blit(text_q3_desc, (50, 250))
			screen.blit(text_q3, (50, 300))
			screen.blit(text_q4_desc, (50, 350))
			screen.blit(text_q4, (50, 400))
			screen.blit(text_q5_desc, (50, 450))
			screen.blit(text_q5, (50, 500))


			screen.blit(text_q6_desc, (350, 50))
			screen.blit(text_q6, (350, 100))
			screen.blit(text_q7_desc, (350, 150))
			screen.blit(text_q7, (350, 200))
			screen.blit(text_q8_desc, (350, 250))
			screen.blit(text_q8, (350, 300))
			screen.blit(text_q9_desc, (350, 350))
			screen.blit(text_q9, (350, 400))
			screen.blit(text_q10_desc, (350, 450))
			screen.blit(text_q10, (350, 500))



			pygame.display.update()

			hello_str.position = [joints[0], joints[1], joints[2], joints[3], joints[4], joints[5], joints[6], joints[7], joints[8], joints[9]]


		pub.publish(hello_str)
		rate.sleep()


		


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


