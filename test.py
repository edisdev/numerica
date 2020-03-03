import numerica as n

from numerica import f, c
from numerica import diff_backward

fn1 = f([1, -6, 5]) # (x^2 - 6x + 5)^1
fn2 = f([1, -6.5, 13.5, -9]) # (1x^3 - 6.5x^2 + 13.5x - 9)^1
fn3 = f([1, -4, -4, 15]) # f = x^3 - 4x^2 - 4x + 15
fn4 = f([1, 0, -20, 16]) # x^3 - 20x + 16
fn5 = f([1, -2, -3]) # x^2 - 2x - 3

# nonlinear.iterative.basic
gx = f([1, 0]) # g(x) = x
hx1 = f([2, 3], 1/2) # h(x) = (2x + 3)^(1/2)
hx2 = c(f([3, 0]), f([1, -2], -1)) # h(x) = (3 / (x - 2))
hx3 = c(f([1/2, 0]), f([1, 0, -3])) # h(x) = (x^2 - 3) / 2

# Tests
def t(a, b, name):
  if (type(a) == int or type(a) == float): a = round(a, 1)
  if (type(b) == int or type(b) == float): b = round(b, 1)

  if (a != b):
    print('[error] ' + name + ' expected: (' + str(b) + ') got: (' + str(a) + ')')
  else:
    print('[ok] '+name)

# Nonlinear
t(n.graph(fn=fn1, dx=1, epsilon=0.001, x=0), 1, 'nonlinear.bracketing.graph.1')
t(n.graph(fn=fn1, dx=1, epsilon=0.001, x=2), 5, 'nonlinear.bracketing.graph.2')

t(n.bisection(fn=fn2, epsilon=0.001, a=0, b=1.75), 1.5, 'nonlinear.bracketing.bisection.1')
t(n.bisection(fn=fn2, epsilon=0.001, a=1.75, b=2.5), 2, 'nonlinear.bracketing.bisection.2')
t(n.bisection(fn=fn2, epsilon=0.001, a=2.5, b=6), 3, 'nonlinear.bracketing.bisection.3')

t(n.regulafalsi(fn=fn2, epsilon=0.001, a=0, b=1.75), 1.5, 'nonlinear.bracketing.regulafalsi.1')
t(n.regulafalsi(fn=fn2, epsilon=0.001, a=1.75, b=2.5), 2, 'nonlinear.bracketing.regulafalsi.2')
t(n.regulafalsi(fn=fn2, epsilon=0.001, a=2.5, b=6), 3, 'nonlinear.bracketing.regulafalsi.3')

t(n.basic(gx, hx1, epsilon=0.005, x=4), 3, 'nonlinear.iterative.basic.1')
t(n.basic(gx, hx2, epsilon=0.005, x=4), -1, 'nonlinear.iterative.basic.2')
t(n.basic(gx, hx3, epsilon=0.005, x=4), None, 'nonlinear.iterative.basic.3')

t(n.newtonraphson(fn3, epsilon=0.00005, x=-2.5), -2, 'nonlinear.iterative.newtonraphson.1')

t(n.secant(fn4, epsilon=0.02, x0=3, x1=5), 4, 'nonlinear.iterative.secant.1')

# Differentiation
t(n.diff_backward(fn5, 2), 2, 'differentiation.backward.1')
t(n.diff_backward(fn5, 5), 8, 'differentiation.backward.2')