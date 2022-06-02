# speeders task

print("welcome to the speeders fine calculation system")
print("enter the name of the speeder")
name = input()
print("enter the speed limit (in km/h)")
limit = int(input())
print(f"enter {name}'s speed (in km/h)")
speed = int(input())
if speed - limit > 29:
    fine = 180
elif speed - limit <20-29:
    fine = 130
elif speed - limit <10-19:
    fine = 80
elif speed - limit <10:
    fine = 30
