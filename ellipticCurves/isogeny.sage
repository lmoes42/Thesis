A = 1
B = 2
Abar = -27 * A
Bbar = 4 * A + 27 * B

E = EllipticCurve([0,A,1,-2*B * A, B^2])
print(E)

Ebar = EllipticCurve([0,Abar,1,-2*Bbar * Abar, Bbar^2])
print(Ebar)

def Phi(X, Y, P):
    x, y = P[0], P[1]
    A = 2 * y^2 + 2 * X * Y^2 - x^3 - 2/3 * X * x^2
    xi = 3/(x^2) * A

    B = -4 * X * Y * x + 8 * X * Y^2 - x^3
    eta = 27 * y / (x^3)
    return (xi, eta)

plot(E + Ebar)
