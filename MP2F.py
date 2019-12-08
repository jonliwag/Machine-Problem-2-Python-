from math import sqrt
import numpy as np

# setting the inputs from user
x1 = int(input('input x-component of first point: '))
y1 = int(input('input y-component of first point: '))
x2 = int(input('input x-component of second point: '))
y2 = int(input('input y-component of second point: '))
x3 = int(input('input x-component of third point: '))
y3 = int(input('input y-component of third point: '))

x1y1 = (x1**2) + (y1**2)
x2y2 = (x2**2) + (y2**2)
x3y3 = (x3**2) + (y3**2)
A = np.array([(x1y1, x1, y1, 1), (x2y2, x2, y2, 1), (x3y3, x3, y3, 1)], dtype = float)

m1 = A[0:,1:]
detm1 = np.linalg.det(m1)
detm1f = round(detm1)

# matrix excluding the column with index '1'
mat0 = A[0:, 0]
mat2 = A[0:, 2]
mat3 = A[0:, 3]

# combining the columns and computing its determinant
m2 = np.column_stack((mat0, mat2, mat3))
detm2 = -1 * (np.linalg.det(m2))
detm2f = round(detm2)

# matrix excluding the column with index '2'
mat21 = A[0:, 0]
mat22 = A[0:, 1]
mat33 = A[0:, 3]

# combining the columns and computing its determinant
m3 = np.column_stack((mat21,mat22,mat33))
detm3 = np.linalg.det(m3)
detm3f = round(detm3)

# matrix excluding the column with index '3'
mat30 = A[0:, 0]
mat31 = A[0:, 1]
mat32 = A[0:, 2]

# combining the columns and computing its determinant
m4 = -1 * (np.column_stack((mat30,mat31,mat32)))
detm4 = np.linalg.det(m4)
detm4f = round(detm4)

# matrix excluding the column with index '0'
m5 = A[0:, 1:]
detm5 = np.linalg.det(m5)
detm5f = round(detm5)

h = (-0.5)*(detm2f/detm5f)
k = (-0.5)*(detm3f/detm5f)

rad = detm4f/detm5f

radius = ((x1-h)**2)+((y1-k)**2)
radiusf= sqrt(radius)
print ('')
print ('radius ''r'' of the circle', format(round(radiusf, 2)))
print ('center of the circle (h, k): ', '(', h, ',', k, ')')

if detm1f != 0:
    f21 = detm2f/detm1f
    f31 = detm3f/detm1f
    f41 = detm4f/detm1f
    
    print ('coefficients for the equation of the circle','[', f21, ',', f31, ','
                                                           , f41, ']')
else:
    print ('coefficients in the general equation of the circle: ','[', detm2f, ','
                                                        , detm3f, ',', detm4f, ']')
    




