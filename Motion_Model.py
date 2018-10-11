# SI UNITS
import math


# This is wrong right now, we need to add history into x, y, and rho


class Motion_Model
	


	wheelRad = 0.1             # m    
	vehDamping = 1             # N*s/m
	vehMass = 10               # Kg
	vehWidth = 0.2			   # m
	wheelBase = 0.3            # m
	Cg = 0.2                   # m
	deg2rad = 0.01745329251    # rad/deg
	rad2deg = 57.2957795131    # deg/rad
	Ts = 0.01                  # s

	def __init__ (self):
		self.x = 0
		self.y = 0
		self.rho = 0
		self.v0 = 0         
		self.s0 = 0  

	def move(torque, theta):
		s = distance(torque)
		r = turn_radius(theta)
		rho = turn_angle(s, r)
		y = val_y(r, rho)
		x = val_x(r, rho)
		return [x, y, rho * self.rad2deg]

	def distance(self, torque):
		Fw = torque / self.wheelRad
		F_total = Fw - (self.v0 * self.vehDamping)
		s_ddot = (1 / self.vehMass) * F_total
		s_dot = s_ddot * Ts + v0
		s = s_dot * Ts + s0 
		v0 = s_dot
		return s

	def turn_radius(self, theta):
		a = self.wheelBase * math.tan(math.pi - self.deg2rad*theta) + self.vehWidth / 2
		b = self.wheelBase - self.Cg
		r = math.sqrt(a * a + b * b)
		return r

	def turn_angle(s, r):
		rho = s / r
		return rho

	def val_y(r, rho):
		y = r * math.sin(rho)
		return y

	def val_x(r, rho):
		x = r * (1 - math.cos(rho))
		return x
