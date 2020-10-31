from os import system
system('pip install sympy')
import sympy as sy

# I have defined the symbol t for you to use in the SymPy expressions you will write below
t = sy.Symbol("t")

# Your expression to determine the denominator goes here 
denom = 

# Your expression to determine an expression for the posterior probability density goes here
posterior =

# You shouldn't need to adjust anything from here 
print("The posterior probability density function for the parameter given the first result was positive is")
print( posterior )
graph = sy.plot( posterior, xlim=[0,1], ylim=[0,4], xlabel="t", ylabel="P(p=t|T_1=1)")
graph.save("mybayes.png")
