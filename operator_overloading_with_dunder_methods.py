import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
        
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
        
    def __mul__(self, other):
        return Complex(self.real * other.real - (self.imaginary * other.imaginary), 
                       self.real * other.imaginary + (self.imaginary * other.real))

    def __truediv__(self, other):
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        num__times_complex_conj_denom = Complex(a,b) * Complex(c, -1*d)
        denominator = (Complex(c,d) * Complex(c, -1*d)).real # c**2 + d**2
        return Complex(num__times_complex_conj_denom.real/denominator, 
                       num__times_complex_conj_denom.imaginary/denominator)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')