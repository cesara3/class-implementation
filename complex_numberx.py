# ======================================================
# Complex number examples that can be checked using python
# ======================================================

import cmath
import math

# complex numbers are the set of all real numbers in the form of a + bi
# where a is a real number and b is an imaginary number

# what is the difference between i and j? tbh there is really no difference, it depends on the field of study.
# usually in mathematics and physics i is used, in engineering/programming j is used (to not get confused with current (i/I))
# you might see a mix of both since we are introducing it but after a while,
# we will switch to solely using j

# ------------------------------------------------------
# Real vs Imaginary Numbers
# ------------------------------------------------------
real_number = math.sqrt(64)
imaginary_num = cmath.sqrt(-64)

print("Real number sqrt(64):", real_number)
print("Imaginary number sqrt(-64):", imaginary_num)

# ------------------------------------------------------
# Example with imaginary unit
# ------------------------------------------------------
imaginary_example = (4j)**2
print("Example (4j)^2:", imaginary_example)

# we can do a powers of "i" function but in our case j
def power_of_j(n):
    r = n % 4
    if r == 0:
        return 1
    if r == 1:
        return 1j
    if r == 2:
        return -1
    else:
        return -1j

# examples
print("i^7  =", power_of_j(7))
print("i^24 =", power_of_j(24))
print("i^15 =", power_of_j(15))
print("i^17 =", power_of_j(17))
print("i^987=", power_of_j(987))

# ------------------------------------------------------
# Creating and printing complex numbers
# z = a + bi : where a is the real part and b is the imaginary
# ------------------------------------------------------
z1 = 3 + 7j
z2 = 2 - 3j

scaled_z1 = z1 * 2

y3 = 4 + cmath.sqrt(-9)
y4 = 8 + cmath.sqrt(-16)

print("z1 =", z1)
print("z2 =", z2)
print("scaled_z1 =", scaled_z1)
print("y3 =", y3)
print("y4 =", y4)

# ------------------------------------------------------
# Lets use the complex numbers we created to do some basic operations
# Addition examples
# ------------------------------------------------------
print("\n--- Addition ---")

addition_example1 = z1 + z2
addition_example2 = y3 + y4

print("z1 + z2 =", addition_example1)
print("y3 + y4 =", addition_example2)

# ------------------------------------------------------
# Subtraction examples
# ------------------------------------------------------
print("\n--- Subtraction ---")

sub_x1 = 6 + 7j
sub_x2 = 5 + 10j
subtraction_example1 = sub_x1 - sub_x2
print("sub_x1 - sub_x2 =", subtraction_example1)

sub_y1 = 24 - cmath.sqrt(-64)
sub_y2 = 12 + 3j
subtraction_example2 = sub_y1 - sub_y2
print("sub_y1 - sub_y2 =", subtraction_example2)

sub_z1 = 3 - 2 * cmath.sqrt(-18)
sub_z2 = 2 + 3 * cmath.sqrt(-8)
subtraction_example3 = sub_z1 - sub_z2
print("sub_z1 - sub_z2 =", subtraction_example3)

# ------------------------------------------------------
# Multiplication examples
# when multiplying complex numbers there is two key things we must remember
# One of them is the FOIL multiplication method
# The other is our power of i rules, most importantly i^2 = -1
# ------------------------------------------------------
print("\n--- Multiplication ---")
mult_x1 = -8 + 10j
mult_x2 = 3 + 8j
multiplication_example1 = mult_x1 * mult_x2
print("mult_x1 * mult_x2 =", multiplication_example1)

mult_y1 = 24 + 7j
mult_y2 = 13 - 10j
multiplication_example2 = mult_y1 * mult_y2
print("mult_y1 * mult_y2 =", multiplication_example2)

# ------------------------------------------------------
# Division examples
# we use the comple conjugates to divide
# we find the complex conjugate by changing the sign if the complex number
# a + bi  ---> a - bi
# a - bi  ---> a + bi
# lets say z = a + bi and the complex conjugate is z* = a - bi
# ------------------------------------------------------
print("\n--- Conjugates & Division ---")
z = 3 + 4j
conju_z = z.conjugate()
print("z =", z)
print("Conjugate of z:", conju_z)
print("z * conjugate of z:", z * conju_z) # this should give us a real number

div_z1 = -8 + 6j
div_z2 = 8 - 5j
division_example1 = div_z1 / div_z2
print("div_z1 / div_z2 =", division_example1)

div_y1 = 5 - 4j
div_y2 = 2 + 3j
division_example2 = div_y1 / div_y2
print("div_y1 / div_y2 =", division_example2)

# ------------------------------------------------------
# Magnitude (absolute value)
# the distance from the orgin in the complex plane
# |z| = sqrt(a^2 + b^2)
# ------------------------------------------------------
print("\n--- Magnitude ---")
z = 3 + 4j
magnitude = abs(z)
print("z =", z)
print("|z| =", magnitude)

# ------------------------------------------------------
# Phase/Angle
# This is the angle the complex number makes with the real axis
# ------------------------------------------------------
print("\n--- Phase / Angle ---")
z = 3 + 4j
phase_radians = cmath.phase(z)
phase_degrees = math.degrees(phase_radians)

print("z =", z)
print("Phase (radians):", phase_radians)
print("Phase (degrees):", phase_degrees)

# ------------------------------------------------------
# Rectangular to Polar
# Rectangular form: z = a + bi
# Polar form: z = r(cosθ + i sinθ) or z = re^(iθ)
# Where r is the magnitude and theta (θ) is the angle
# ------------------------------------------------------
print("\n--- Rectangular to Polar ---")
z = 1 + 1j
r, theta = cmath.polar(z)

print("z =", z)
print("Magnitude r:", r)
print("Angle θ (radians):", theta)
print("Angle θ (degrees):", math.degrees(theta))

# ------------------------------------------------------
# Polar to Rectangular
# -------------------------------------------------------
print("\n--- Polar back to Rectangular ---")

z_rectangular = cmath.rect(r, theta)
print("Rectangular form:", z_rectangular)

#--------------------------------------------------
# Quadratic Formula with Complex Roots
# This shows why complex numbers are important, they allow us to find solutions to equations that have no real solutions
print("\n--- Quadratic Formula with Complex Roots ---")

#solve x^2 + 4x + 13 = 0
a = 1
b = 4
c = 13

discriminant = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

print("Equation: x^2 + 4x + 13 = 0")
print("Discriminant:", discriminant)
print("Root 1:", root1)
print("Root 2:", root2)



#-------------------------------------------------------
# Now we move from complex numbers to vectors and matrices.
#-------------------------------------------------------



#-------------------------------------------------------
# Vectors 
# A vector is a quantity that has both size (magnitude) and direction
#---------------------------------------------------------
print("\n--- Vectors ---")

v = [10, 7]
w = [3, 6]

def add_vectors(a,b):
    return [a[0] + b[0], a[1] + b[1]]

def subtract_vectors(a,b):
    return [a[0] - b[0], a[1] - b[1]]

print("v =", v)
print("w =", w)
print("v + w =", add_vectors(v, w))
print("v - w =", subtract_vectors(v, w))

#--------------------------------------------------
# Dot Product (Row X Column)
# The Dot Product multiplies two vectors together and produces a scalar (one number)
# The Dot Product measures how much two vectors point in the same direction
#---------------------------------------------------
print("\n--- Dot Product ---")

dot_v = [6, 7]
dot_w = [4, 2]

def dot_product(a,b):
    return a[0] * b[0] + a[1] * b[1]

print("dot_v =", dot_v)
print("dot_w =", dot_w)
print("v · w =", dot_product(dot_v, dot_w))

#---------------------------------------------------
# 2x2 Matrices
# A matrix is a rectangular array of numbers, the entries can be both
# Entries can be real or complex
#--------------------------------------------------
print("\n--- 2x2 Matrices ---")
real_matrix = [[5,6],
                [4,8]] #real entries

complex_matrix = [[2,3j],
                [1-1j,4]] # complex entries


print("Real Matrix:\n", real_matrix)
print("Complex Matrix:\n", complex_matrix)

# Multiplying matrices with vectors
print("\n--- Matrix-Vector Multiplication ---")
A = [[2, 3],
     [1, 4]]

x = [1, 2]

def mat_vec(M,vect):
    return [M[0][0] * vect[0] + M[0][1] * vect[1],
            M[1][0] * vect[0] + M[1][1] * vect[1]]

print("A =", A)
print("x =", x)
print("A x =", mat_vec(A, x))


# Determinant 
# The Determinant of a 2x2 matrix tells us wether the matrix can
# be used to solve equations
# for 2x2 matrix A = [a,b]
#                    [c,d]
# the determinant is: det(A) = ad - bc
# what does the determinant tell us?
# -if determinant DOES NOT equal zero, the matrix is invertible
# -if determinat DOES equal zero, the matrix is NOT invertible
print("\n--- Determinant ---")

def det2(M):
    a, b = M[0]
    c, d = M[1]
    return a*d - b*c
A = [[2, 3],
     [1, 4]]

print("A =", A)
print("det(A) =", det2(A))

#--------------------------------------------------
# Matrix Addition
#--------------------------------------------------
print("\n--- Matrix Addition ---")
# Define matrix A (2x2)
A = [[1,2],
     [3,4]]

# Define matrix B (2x2)
B = [[5,6],
     [7,8]]

# Create empty 2x2 result matrix
C = [[0,0],[0,0]]

# Loop through rows
for i in range(2):
    # Loop through columns
    for j in range(2):
        # Add corresponding entries
        C[i][j] = A[i][j] + B[i][j]

print("A =", A)
print("B =", B)
print("A + B =", C)

#--------------------------------------------------
# Inverse of a 2x2 matrix
#--------------------------------------------------
print("\n--- Inverse of a 2x2 Matrix ---")

def inverse_2x2(M):
    det = det2(M)
    if det == 0:
        return None
    a, b = M[0]
    c, d = M[1]
    return [[d/det, -b/det], [-c/det, a/det]]

A = [[2, 3],
     [1, 4]]

print("A =", A)
print("det(A) =", det2(A))
print("A^(-1) =", inverse_2x2(A))

# ------------------------------------------------------
# 2x2 Systems of Equations
# Solve:
# 2x + 3y = 7
# 1x + 4y = 9
# ------------------------------------------------------
print("\n--- 2x2 System of Equations ---")

A = [[2, 3],
     [1, 4]]

b = [7, 9]

print("A =", A)
print("b =", b)

A_inv = inverse_2x2(A)

if A_inv is not None:
    solution = mat_vec(A_inv, b)
    solution = [round(val, 3) for val in solution] #rounds 
    print("Solution [x, y] =", solution)
else:
    print("Matrix is not invertible, so the system cannot be solved this way.")
