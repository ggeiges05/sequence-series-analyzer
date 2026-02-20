import math

#User Input -> Stored Dataset List
def user_Input():
    a = []
    current = ""
    userInput=input("Enter Dataset: ")
    for x in userInput:
        if x != " " and x != ",":
            current += x
        else:
                if current != "":
                    a.append(float(current))
                    current = ""
    if current != "":
        a.append(float(current))

    return a

#Arithmetic Sequence Test: 

def is_Arithmetic(a):

    if len(a) < 2:
         return False,None

    d = a[1]-a[0]

    for i in range(2, len(a)):
        diff = a[i] - a[i-1]
        if not math.isclose(diff,d):
            return False, None
        
    return True,d

#Geometric Sequence Test:
def is_Geometric(a):

    if len(a) < 2:
         return False,None
    
    if a[0] == 0:
         return False,None

    r = a[1]/a[0]

    for i in range(2, len(a)):
        prevA = a[i-1]
        curr = a[i]
        diff = curr/prevA
        if prevA == 0:
             return False,None
        if not math.isclose(diff,r):
             return False,None
        
    return True,r

#Find n term for (An):
def get_n():
    while(True):
        try:
            n = int(input("Assuming the model continues, what value are you trying to find?: "))
        except ValueError:
            print("Needs to be an integer")
            continue
        if(n < 1):
            print("Must be a positive integer >= 1")
            continue
        break
    return n

#Compute the Nth term (An) then find partial sum (Sn):
#Nth term (An) for Arithmatic Sequence:
def arith_Nth_Term(a1,d,n):
    return a1 + (n-1)*d
#Arithmatic Partial Sum:
def arith_Partial_Sum(a1,d,n):
    return (n/2)*((2*a1) + (n-1) * d)
#Nth term (An) for Geometric Sequence:
def geo_Nth_Term(a1,r,n):
    return a1 * r**(n-1)
#Geometric Partial Sum:
def geo_Partial_Sum(a1,r,n):
    if(r == 1):
        return n * a1
    return a1*((1-r**n)/(1-r))


#Main
def main():
    #Get dataset from user input
    terms = user_Input()
    #Display dataset
    print(terms)
    #Run arithmatic test
    is_Arith , d = is_Arithmetic(terms)
    #Run Geometric Test
    is_Geo, r = is_Geometric(terms)
    #Run get_n from user input
    n = get_n()
    if is_Arith and is_Geo:
        print("Sequence is both Arithmetic and Geometric")
        print(f"Arithmatic a_{n} = {arith_Nth_Term(terms[0], d, n)}")
        print(f"Geometric a_{n} = {geo_Nth_Term(terms[0], r, n)}")
        print(f"Airthmatic S_{n} = {arith_Partial_Sum(terms[0], d, n)}")
        print(f"Geometric S_{n} = {geo_Partial_Sum(terms[0], r, n)}")
    elif is_Arith:
        print("Sequence is Arithmetic")
        print(f"a_{n} = {arith_Nth_Term(terms[0], d, n)}")
        print(f"S_{n} = {arith_Partial_Sum(terms[0], d, n)}")
    elif is_Geo:
        print("Sequence is Geometric")
        print(f"a_{n} = {geo_Nth_Term(terms[0], r, n)}")
        print(f"S_{n} = {geo_Partial_Sum(terms[0], r, n)}")
    else:
        print("This dataset cannot be used to compute nth term or partial sum.")


if __name__ == "__main__":
    main()