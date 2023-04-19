import math

height = float(input("Введите высоту (в метрах): "))
g = 9.81  # ускорение свободного падения

time = math.sqrt((2 * height) / g)
velocity = g * time

print("Время падения равно", round(time, 2), "с.")
print("Скорость падения равна", round(velocity, 2), "м/с.")
