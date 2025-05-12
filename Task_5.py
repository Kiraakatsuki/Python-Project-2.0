KM_TO_MILES = 0.621371
CM_TO_METERS = 0.01
GRAMS_TO_KG = 0.001
value = float(input("Enter the value to convert: "))
unit = input("Enter the unit (km, cm, g): ")
if unit == "km":
    print(f"{value} kilometers is {value * KM_TO_MILES} miles")
elif unit == "cm":
    print(f"{value} centimeters is {value * CM_TO_METERS} meters")
elif unit == "g":
    print(f"{value} grams is {value * GRAMS_TO_KG} kilograms")
else:
    print("Error: Unknown unit")
