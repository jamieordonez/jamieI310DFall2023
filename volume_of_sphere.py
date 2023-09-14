import math
def calculate_volume_of_sphere(radius):
    volume=(4/3)*math.pi*(radius**3)
    return volume

vol_1=calculate_volume_of_sphere(30)
vol_2=calculate_volume_of_sphere(40)

print(f'The volume of a sphere with a radius of 30 is {vol_1}')
print(f'The volume of a sphere with a radius of 40 is {vol_2}')
