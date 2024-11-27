from Math_operations.Basic_operations import Arithmetic
from Math_operations.Geometry import Area

print("Arithmetic Operations")
print("5 + 3 = ",Arithmetic.add(5,3))
print("10 - 7 = ",Arithmetic.substract(10,7))
print("5 * 3 = ",Arithmetic.multiply(5,3))
print("8 / 2 = ",Arithmetic.divide(8,2))
print("8 / 0 = ",Arithmetic.divide(8,0))



print("\nArea Calculations : ")
print("Rectangle (length = 5, width = 3 ):",Area.rectangle_area(5,3))
print("Circus (Radius = 7):",Area.circle_area(7))
print("Triangle (base = 4, Height = 5):",Area.triangle_area(4,5))
