from math import sin, cos, exp, pi
import sys
from Methods import newton,  bisection, secant


def get_input():
    """Get f, df, a, b, x0, x1 from command line"""
    from scitools.std import StringFunction
    try:
        f = StringFunction(sys.argv[1])
        df = StringFunction(sys.argv[2])
        a = float(sys.argv[3])
        b = float(sys.argv[4])
        x0 = float(sys.argv[5])
        x1 = float(sys.argv[6])
    except IndexError:
        print ('Usage %s: f df a b x0 x1' % sys.argv[0])
        sys.exit(1)
    return f, df, a, b, x0, x1

if __name__ == '__main__':
    f, a, b, x0, x1 = get_input()
    x, iter = bisection(f, a, b)
    newton(f, x0)
    secant(f, a, b)
    print('Found root x=%g in %d iterations' % (x, iter))