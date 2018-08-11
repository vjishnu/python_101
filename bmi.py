# BMI calculator
print("....BMI CALCULATOR....")
"""read height and weight from user and calculate the Body Mass Index of the user."""
print("....BMI calculator....")
height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
bmi =  (weight / (height * height))
print(f"Your body mass index is {bmi}.")
print("..................")
