"""
            ##    Finite Difference Method   ##

    This code finds the solution of the wave equation with Finite Difference Method.

"""
#          Importing libraries            #
import numpy as np
import matplotlib.pyplot as plt


L = 20
alpha = 999
h = 0.1
s = 0.9
k = h*(s**0.5)



def phi_function(x,L,alpha):
    """
    Returns Phi function value for aken x,L and alpha
    """
    if x == 0 or x == L:
        return 0
    return np.exp(-alpha * (x - 0.5*L)**2)

def u_function(x,t):
    """
        Returns u function value for aken x,t and alpha
    """
    return 0.5*(phi_function(x+t,L,alpha)+phi_function(x-t,L,alpha))

def exact_solution(L,t,h,alpha):
    """"
    Returns list of U values with range for exact solution formula given.
    """
    u_list = []
    for x in np.arange(0,L,h):
        u = 0.5 * (phi_function(x + t , L , alpha) + phi_function(x - t, L , alpha))
        u_list.append(u)
    return u_list,np.arange(0,L,h)


def numeric_solution():
    """"
    Returns list of U values for numeric solution.
    """
    dummy = 60*k
    u_unitial = [u_function(np.arange(0,L+h,h)[0],0)]
    u_list_numeric = [u_function(np.arange(0,L+h,h)[0],dummy)]

    for x in range(1,len(np.arange(0,L+h,h))-1):

        u_list_numeric.append(u_function(np.arange(0,L+h,h)[x],dummy))
        u_unitial.append(u_function(np.arange(0,L+h,h)[x],0))

    u_list_numeric.append(u_function(np.arange(0,L+h,h)[-1],dummy))

    return u_list_numeric

# Driver Code
if __name__ == "__main__":
    vals = exact_solution(20,0,0.1,1) # Solution values for imitial condition
    u_list_numeric = numeric_solution()  # Solution values for Numeric condition

    # Plot Part
    plt.plot(vals[1],vals[0],label="Inıtıal Condition")
    plt.plot(np.arange(0,L+h,h),u_list_numeric,label="Numerical Solution")
    plt.legend()
    plt.title("X vs U Graph for Wave Equation")
    plt.xlabel("X")
    plt.ylabel("U")
    plt.show()

