length=2909
width=3968
height=3272
mass=727
a=pow(10,9)
b=pow(10,4)
volume=length*width*height
if((volume>=a or length>=b or width>=b or height>=b or mass>=b) and  (mass>=100)):
    print("Both")
elif(volume>=a or length>=b or width>=b or height>=b or mass>=b):
    print("Bulky")
elif not((volume>=a or length>=b or width>=b or height>=b or mass>=b) and (mass>=100)):
    print("Neither")
elif((volume>=a or length>=b or width>=b or height>=b or mass>=b) and not(mass>=100)):
    print("Bulky")
elif(not(volume>=a or length>=b or width>=b or height>=b or mass>=b) and (mass>=100)):
    print("Heavy")