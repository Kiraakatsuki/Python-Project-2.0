distance = float(input("Enter the distance traveled (in km): "))
time = float(input("Enter the time taken (in hours): "))
if time > 0:
    speed = distance / time
    print(f"Speed = {speed} km/h")
else:
    print("Error: Time must be greater than zero")