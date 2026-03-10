# ======================================================
# Practice Problems: Complex Numbers, Vectors, and Matrices
# Students should try each problem by hand first,
# then run the Python check.
# ======================================================

import cmath
import math

print("\n---------------------------------------------------")
print("PRACTICE 1: Real vs Imaginary Numbers")
print("---------------------------------------------------")
print("Try by hand first:")
print("1) sqrt(81)")
print("2) sqrt(-81)")

print("\nPython check:")
print("sqrt(81)  =", math.sqrt(81))
print("sqrt(-81) =", cmath.sqrt(-81))


print("\n---------------------------------------------------")
print("PRACTICE 2: Powers of j")
print("---------------------------------------------------")
print("Try by hand first:")
print("1) j^9")
print("2) j^14")
print("3) j^31")

def power_of_j(n):
    r = n % 4
    if r == 0:
        return 1
    elif r == 1:
        return 1j
    elif r == 2:
        return -1
    else:
        return -1j

print("\nPython check:")
print("j^9  =", power_of_j(9))
print("j^14 =", power_of_j(14))
print("j^31 =", power_of_j(31))


print("\n---------------------------------------------------")
print("PRACTICE 3: Complex Addition")
print("---------------------------------------------------")
print("Try by hand first:")
print("(5 + 2j) + (3 - 7j)")
print("(1 + 6j) + (4 + 2j)")

z1 = 5 + 2j
z2 = 3 - 7j
z3 = 1 + 6j
z4 = 4 + 2j

print("\nPython check:")
print("(5 + 2j) + (3 - 7j) =", z1 + z2)
print("(1 + 6j) + (4 + 2j) =", z3 + z4)


print("\n---------------------------------------------------")
print("PRACTICE 4: Complex Subtraction")
print("---------------------------------------------------")
print("Try by hand first:")
print("(8 + 6j) - (4 - 3j)")
print("(10 - 2j) - (7 + 5j)")

z1 = 8 + 6j
z2 = 4 - 3j
z3 = 10 - 2j
z4 = 7 + 5j

print("\nPython check:")
print("(8 + 6j) - (4 - 3j) =", z1 - z2)
print("(10 - 2j) - (7 + 5j) =", z3 - z4)


print("\n---------------------------------------------------")
print("PRACTICE 5: Complex Multiplication")
print("---------------------------------------------------")
print("Try by hand first:")
print("(3 + 2j)(1 - 4j)")
print("(2 - 5j)(3 + j)")

z1 = 3 + 2j
z2 = 1 - 4j
z3 = 2 - 5j
z4 = 3 + 1j

print("\nPython check:")
print("(3 + 2j)(1 - 4j) =", z1 * z2)
print("(2 - 5j)(3 + j) =", z3 * z4)


print("\n---------------------------------------------------")
print("PRACTICE 6: Conjugates")
print("---------------------------------------------------")
print("Try by hand first:")
print("Find the conjugate of 6 - 8j")
print("Find the conjugate of 4 + 11j")

z1 = 6 - 8j
z2 = 4 + 11j

print("\nPython check:")
print("conjugate of", z1, "=", z1.conjugate())
print("conjugate of", z2, "=", z2.conjugate())


print("\n---------------------------------------------------")
print("PRACTICE 7: Complex Division")
print("---------------------------------------------------")
print("Try by hand first:")
print("(6 + 3j) / (2 - j)")
print("(5 - 4j) / (1 + 2j)")

z1 = 6 + 3j
z2 = 2 - 1j
z3 = 5 - 4j
z4 = 1 + 2j

ans1 = z1 / z2
ans2 = z3 / z4

print("\nPython check:")
print("(6 + 3j) / (2 - j) =", complex(round(ans1.real, 4), round(ans1.imag, 4)))
print("(5 - 4j) / (1 + 2j) =", complex(round(ans2.real, 4), round(ans2.imag, 4)))


print("\n---------------------------------------------------")
print("PRACTICE 8: Magnitude")
print("---------------------------------------------------")
print("Try by hand first:")
print("|7 + 24j|")
print("|8 - 6j|")

z1 = 7 + 24j
z2 = 8 - 6j

print("\nPython check:")
print("|7 + 24j| =", round(abs(z1), 4))
print("|8 - 6j| =", round(abs(z2), 4))


print("\n---------------------------------------------------")
print("PRACTICE 9: Phase / Angle")
print("---------------------------------------------------")
print("Try by hand first:")
print("Find the angle of 1 + 1j")
print("Find the angle of 3 + 3j")

z1 = 1 + 1j
z2 = 3 + 3j

angle1_rad = cmath.phase(z1)
angle1_deg = math.degrees(angle1_rad)

angle2_rad = cmath.phase(z2)
angle2_deg = math.degrees(angle2_rad)

print("\nPython check:")
print("For z = 1 + 1j:")
print("Radians =", round(angle1_rad, 4))
print("Degrees =", round(angle1_deg, 4))

print("For z = 3 + 3j:")
print("Radians =", round(angle2_rad, 4))
print("Degrees =", round(angle2_deg, 4))


print("\n---------------------------------------------------")
print("PRACTICE 10: Rectangular to Polar")
print("---------------------------------------------------")
print("Try by hand first:")
print("Convert 2 + 2j to polar form")
print("Convert 3 + 4j to polar form")

z1 = 2 + 2j
z2 = 3 + 4j

r1, theta1 = cmath.polar(z1)
r2, theta2 = cmath.polar(z2)

print("\nPython check:")
print("z = 2 + 2j -> r =", round(r1, 4), ", theta (degrees) =", round(math.degrees(theta1), 4))
print("z = 3 + 4j -> r =", round(r2, 4), ", theta (degrees) =", round(math.degrees(theta2), 4))


print("\n---------------------------------------------------")
print("PRACTICE 11: Polar to Rectangular")
print("---------------------------------------------------")
print("Try by hand first:")
print("Convert r = 2, theta = 45 degrees to rectangular form")
print("Convert r = 5, theta = 30 degrees to rectangular form")

r1 = 2
theta1_deg = 45
theta1_rad = math.radians(theta1_deg)

r2 = 5
theta2_deg = 30
theta2_rad = math.radians(theta2_deg)

z1 = cmath.rect(r1, theta1_rad)
z2 = cmath.rect(r2, theta2_rad)

print("\nPython check:")
print("r = 2, theta = 45° ->", complex(round(z1.real, 4), round(z1.imag, 4)))
print("r = 5, theta = 30° ->", complex(round(z2.real, 4), round(z2.imag, 4)))


print("\n---------------------------------------------------")
print("PRACTICE 12: Quadratic Formula with Complex Roots")
print("---------------------------------------------------")
print("Try by hand first:")
print("Solve x^2 + 6x + 13 = 0")
print("Solve x^2 + 2x + 5 = 0")

# Problem 1
a = 1
b = 6
c = 13
disc = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(disc)) / (2*a)
root2 = (-b - cmath.sqrt(disc)) / (2*a)

# Problem 2
a2 = 1
b2 = 2
c2 = 5
disc2 = b2**2 - 4*a2*c2
root3 = (-b2 + cmath.sqrt(disc2)) / (2*a2)
root4 = (-b2 - cmath.sqrt(disc2)) / (2*a2)

print("\nPython check:")
print("x^2 + 6x + 13 = 0 -> roots:",
      complex(round(root1.real, 4), round(root1.imag, 4)),
      "and",
      complex(round(root2.real, 4), round(root2.imag, 4)))
print("x^2 + 2x + 5 = 0 -> roots:",
      complex(round(root3.real, 4), round(root3.imag, 4)),
      "and",
      complex(round(root4.real, 4), round(root4.imag, 4)))


print("\n---------------------------------------------------")
print("PRACTICE 13: Vector Addition")
print("---------------------------------------------------")
print("Try by hand first:")
print("[4, 7] + [3, -2]")
print("[1, 5] + [-6, 4]")

def add_vectors(a, b):
    return [a[0] + b[0], a[1] + b[1]]

v1 = [4, 7]
w1 = [3, -2]
v2 = [1, 5]
w2 = [-6, 4]

print("\nPython check:")
print("[4, 7] + [3, -2] =", add_vectors(v1, w1))
print("[1, 5] + [-6, 4] =", add_vectors(v2, w2))


print("\n--------------------------------------------------")
print("PRACTICE 14: Vector Subtraction")
print("---------------------------------------------------")
print("Try by hand first:")
print("[9, 5] - [2, 8]")
print("[6, -1] - [3, 7]")

def subtract_vectors(a, b):
    return [a[0] - b[0], a[1] - b[1]]

v1 = [9, 5]
w1 = [2, 8]
v2 = [6, -1]
w2 = [3, 7]

print("\nPython check:")
print("[9, 5] - [2, 8] =", subtract_vectors(v1, w1))
print("[6, -1] - [3, 7] =", subtract_vectors(v2, w2))


print("\n--------------------------------------------------")
print("PRACTICE 15: Dot Product")
print("---------------------------------------------------")
print("Try by hand first:")
print("[5, 3] · [2, 7]")
print("[4, -1] · [6, 2]")

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1]

v1 = [5, 3]
w1 = [2, 7]
v2 = [4, -1]
w2 = [6, 2]

print("\nPython check:")
print("[5, 3] · [2, 7] =", dot_product(v1, w1))
print("[4, -1] · [6, 2] =", dot_product(v2, w2))


print("\n--------------------------------------------------")
print("PRACTICE 16: 2x2 Matrices")
print("---------------------------------------------------")
print("Try by hand first:")
print("Identify the size and entries of these matrices:")
print("[[1, 2], [3, 4]]")
print("[[2, 3j], [1-1j, 4]]")

real_matrix = [[1, 2], [3, 4]]
complex_matrix = [[2, 3j], [1 - 1j, 4]]

print("\nPython check:")
print("Real matrix =", real_matrix)
print("Complex matrix =", complex_matrix)


print("\n--------------------------------------------------")
print("PRACTICE 17: Matrix-Vector Multiplication")
print("---------------------------------------------------")
print("Try by hand first:")
print("A = [[2,1],[4,3]], x = [5,2]")
print("Find Ax")

def mat_vec(M, vect):
    return [M[0][0] * vect[0] + M[0][1] * vect[1],
            M[1][0] * vect[0] + M[1][1] * vect[1]]

A = [[2, 1],
     [4, 3]]
x = [5, 2]

print("\nPython check:")
print("Ax =", mat_vec(A, x))


print("\n--------------------------------------------------")
print("PRACTICE 18: Determinant")
print("---------------------------------------------------")
print("Try by hand first:")
print("Find det([[6,2],[3,5]])")
print("Find det([[4,7],[2,5]])")

def det2(M):
    a, b = M[0]
    c, d = M[1]
    return a * d - b * c

A1 = [[6, 2],
      [3, 5]]

A2 = [[4, 7],
      [2, 5]]

print("\nPython check:")
print("det([[6,2],[3,5]]) =", det2(A1))
print("det([[4,7],[2,5]]) =", det2(A2))


print("\n==================================================")
print("PRACTICE 19: Matrix Addition")
print("==================================================")
print("Try by hand first:")
print("Add A = [[1,2],[3,4]] and B = [[5,6],[7,8]]")

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

C = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("\nPython check:")
print("A + B =", C)


print("\n==================================================")
print("PRACTICE 20: Inverse of a 2x2 Matrix")
print("==================================================")
print("Try by hand first:")
print("Find the inverse of [[4,1],[2,3]]")

def inverse_2x2(M):
    det = det2(M)
    if det == 0:
        return None
    a, b = M[0]
    c, d = M[1]
    return [[d/det, -b/det],
            [-c/det, a/det]]

A = [[4, 1],
     [2, 3]]

A_inv = inverse_2x2(A)

print("\nPython check:")
print("A^(-1) =", [[round(val, 4) for val in row] for row in A_inv])


print("\n==================================================")
print("PRACTICE 21: 2x2 Systems of Equations")
print("==================================================")
print("Try by hand first:")
print("1) 2x + y = 11")
print("   x + 3y = 13")
print("")
print("2) 3x + 2y = 16")
print("   x + 4y = 14")

# Problem 1
A1 = [[2, 1],
      [1, 3]]
b1 = [11, 13]

A1_inv = inverse_2x2(A1)
sol1 = mat_vec(A1_inv, b1)
sol1 = [round(val, 4) for val in sol1]

# Problem 2
A2 = [[3, 2],
      [1, 4]]
b2 = [16, 14]

A2_inv = inverse_2x2(A2)
sol2 = mat_vec(A2_inv, b2)
sol2 = [round(val, 4) for val in sol2]

print("\nPython check:")
print("Problem 1 solution [x, y] =", sol1)
print("Problem 2 solution [x, y] =", sol2)