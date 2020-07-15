# making_stars like that.




temp = n/2

if  temp < 1:
    print("* ")
elif temp >= 1:
    for i in range(0,n):
        print("* "*round(1.00001*(temp)))
        print(" *"*int(temp))
