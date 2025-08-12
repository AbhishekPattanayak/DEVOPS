# When nothing is passed as the argument default value is passed in the parameters

def call_prod(a, b=2): #Default values are passed in the parameters incase no value is defined.
    print(a*b)
    return a *b

call_prod(1,3)  #Function is called but the arguments isnt passed, still the code worked fine. 


#Non default argument should come first 