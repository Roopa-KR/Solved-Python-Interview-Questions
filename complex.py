import cmath
x=complex(input("Enter a complex number: "))
print(abs(x))#returns the magnitude of a complex number
print(cmath.phase(x))#returns the phase of a complex number in radians
print(cmath.polar(x))#returns the polar coordinates of a complex number as a tuple