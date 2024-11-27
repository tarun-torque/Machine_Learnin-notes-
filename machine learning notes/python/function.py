# functions are block thant can be re-used in program

# factorial
def findFact(num):
    fact = 1
    i = 0
    while num>=1:
      fact = fact*num 
      i=1
      num = num-i 
    return fact

print(findFact(0))   
                