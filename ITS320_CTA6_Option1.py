# Module 6 Critical Thinking
# Robert T. Lancaster
# ITS320_CTA6_Option1.py
# Option #1: Working with Python Classes

import math

# define class
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)
    
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)
    
    def __mul__(self, no):
        real = (self.real * no.real - self.imaginary * no.imaginary)
        imaginary = (self.real * no.imaginary + self.imaginary * no.real)
        return Complex(real, imaginary)

    def __truediv__(self, no):
        c_square = no.real * no.real
        d_square = no.imaginary * no.imaginary
        denom = c_square + d_square
        real = (self.real * no.real + self.imaginary * no.imaginary) / (denom)
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / (denom)
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt( ( self.real * self.real + self.imaginary * self.imaginary) )
        return Complex(real, 0)

    def __str__(self):
        real = "%.2f" % self.real
        imaginary = "%.2f" % self.imaginary
        if (self.imaginary)>= 0:
            result = (str(real) + '+' + str(imaginary) + 'i')
        else:
            result = (str(real) + '' + str(imaginary) + 'i')
        return result

#define main()
def main() :
    print('\n')	
    C = map(float, input('Enter \'complex\' number (real and imaginary numbers separated by a space, Ex. 2 1) >> ').split())
    D = map(float, input('Enter \'complex\' number (real and imaginary numbers separated by a space, Ex. 5 6) >> ').split())
    x = Complex(* C)
    y = Complex(* D)
    print('\n')
    print('\n'.join(map(str, [x.__add__(y), x.__sub__(y), x.__mul__(y), x.__truediv__(y), x.mod(), y.mod()])) )
    print('\n')

if __name__== "__main__":
  main()
