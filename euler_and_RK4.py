
"""
            ##   Eulers and Fourth-Order RK Method   ##

    This code finds the solution of the ODE with Eulers and Fourth-Order RK Method.

"""
#          Importing libraries            #
import numpy as np


y1 = 2
y2 = 4

def ODE_1(x,y1,y2) :
    """
        Returns the first function used to estimate its solution.
    """
    return np.array([
        -2*y1 + 4*np.exp(-x),
        -y1*(y2**2)/3
    ])


def RK4_Method(y_1,y_2, h,alpha = 0.5):
    """
        Solves te equation for given initial values y1, y2 and step size h.
        Returns the y1 and y2  values as arrays.    
    """

    n = int(1/h)
    y1s_2, y2s_2 = [], []

    for i in range(0, n):

        k1 = h * ODE_1(h*i, y_1 , y_2)
        k2 = h * ODE_1(h*i, y_1 + alpha * k1[0], y_2 + alpha * k1[1])        
        k3 = h * ODE_1(h*i, y_1 + alpha * k2[0], y_2 + alpha * k2[1])
        k4 = h * ODE_1(h*i, y_1 + k3[0], y_2 + k3[1])      
       
        k = (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)      

        y_1,y_2 = y_1 + k[0],y_2 + k[1]
        y1s_2.append(y_1)
        y2s_2.append(y_2)
    return y1s_2, y2s_2



def Eulers_Method(y1,y2,h):
    """
        Solves te equation for given initial values y1, y2 and step size h.
        Returns the y1 and y2  values as arrays.    
    """
    
    y1s = [y1]
    y2s = [y2]
    n = int(1/h)
    for i in range(n):
        y1, y2 = y1 + h*ODE_1(h*i,y1,y2)[0], y2 + h*ODE_1(h*i,y1,y2)[1]
        
        y1s.append(y1)
        y2s.append(y2)
    return y1s, y2s


# Driver Code
if __name__ == "__main__":
    
    y1 = 2
    y2 = 4
    h = 0.2
    y1s,y2s = Eulers_Method(y1,y2,h)

    print("Eulers Method Results")
    print("\n",10*"#","\n")
    for i in range(len(y1s)):
        print("For",i,"th step solution  for y1 = ",y1s[i],", for y2 = ",y2s[i])
    print("\n",10*"#","\n")

    y1s_2,y2s_2 = RK4_Method(y1,y2,h)
    print("RK4 Method Results")
    for i in range(len(y1s_2)):
        print("For",i+1,"th step solution  for y1 = ",y1s_2[i-1],", for y2 = ",y2s_2[i])
    print("\n",10*"#","\n")
