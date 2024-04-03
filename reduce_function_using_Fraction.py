from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda prod_frac, x: Fraction(prod_frac.numerator*x.numerator, 
                                                      prod_frac.denominator*x.denominator), 
                                                      fracs, 
                                                      Fraction(1, 1)))
    return t.numerator, t.denominator

def product2(fracs):
    product2 = Fraction(1, 1)
    for frac in fracs:
        product2 = Fraction(product2.numerator * frac.numerator, product2.denominator * frac.denominator)
    return product2.numerator, product2.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)