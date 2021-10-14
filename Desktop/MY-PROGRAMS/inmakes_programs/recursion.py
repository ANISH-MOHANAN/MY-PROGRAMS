def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
result=factorial(5)
print(result)

#fcatorial(5)=5*(5-1)*(4-1)*(3-1)*(2-1)=5*4*3*2*1=120