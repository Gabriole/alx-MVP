def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) based on weight in kilograms and height in meters.
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None


def get_bmi_category(bmi):
    """
    Return the category for a given BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        bmi = calculate_bmi(weight, height)

        if bmi is None:
            print("Invalid height input. Height cannot be zero.")
        else:
            category = get_bmi_category(bmi)
            print(f"Your BMI is: {bmi}")
            print(f"You are classified as: {category}")

    except ValueError:
        print("Please enter valid numerical values for weight and height.")


if __name__ == "__main__":
    main()
