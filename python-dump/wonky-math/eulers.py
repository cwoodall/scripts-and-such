# eulers.py
# Developer: Christopher J. Woodall <chris.j.woodall at gmail.com>
# License: MIT License
# Date: Sept 13, 2011
# Version: 1
#
# A little function to print out tables for functions calculated using Euler's
# method.

#
# Recursive way to compute a table of eulers method
# (Only prints table returns nothing)
#
# @var y float initial y value
# @var t float initial t value
# @var dt float increments in which to increase dt
# @var t_lim float upper limit for time on graph
# @var fn lambda function to pass y and t into in form F(t,y)
#
# @return nil
def print_eulers(y, t, dt, t_lim, fn):
	if (t >= t_lim):
		print "%10.2f | %4.2f" % (y,t)
	else:
		print "%10.2f | %4.2f" % (y,t)
		# Recursion
		return print_eulers((y + dt*fn(t,y)), t+dt, dt, t_lim, fn)

def eulers( initial, t_max, dt, fn ):
	if (initial[-1][0] >= t_max):
		return initial
	else:
		in_prime = initial[-1][1] + dt*fn(initial[-1][0], initial[-1][1])
		return [initial, eulers(in_prime, t_max, dt, fn)]

# predefined function for Example 2
def ex2(t,y):
	return y**2 - 4*t


print "Example 1: dy/dt = 2y + 1\n"
print "%10s | %-10s" % ("y", "t")
print_eulers(3, 0.0, 0.5, 3, lambda t, y: 2*y + 1)


print "--------------------------------------------"

print eulers([(0,3)], 3, .5, lambda t, y: 2*y+1)

# Print out the table heading for Example 2
print "Example 2: dy/dt = y^2 - 4t\n"
print "%10s | %-10s" % ("y", "t")
# Run Euler's method on ex3 with starting conditions:
# y = 0.5, t = 0.0 and using: dt = .25 and with an upper t limit of 2
print_eulers(0.5, 0.0, .25, 2, ex2)
