
from linear_solver import pywraplp  
from tools import SolVal, ObjVal
from non_convex_tricks import maximax
def main():
    bounds = []
    s = pywraplp.Solver('',pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    a = [[2],[-2]]
    b = [3,-12]
    x = s.NumVar(2,5,'x')
    z,l = maximax(s,a,[x],b) 
    rc = s.Solve()
    print 'x = ',SolVal(x)
    print 'z = ',SolVal(z)
    print '\delta = ', SolVal(l)
main()
