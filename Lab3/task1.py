import math
def My_function(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    return area

s1 = 1
s2 = 0.5
s3 = 1
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    t_area = My_function(s1, s2, s3)
    print("The area of three triangles is : ", t_area)
else:
    print("Invalid")