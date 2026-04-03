def weather():
    print("What is the temperature scale if you enter in celsius enter C if you enter in fahrenheit enter F?")
    scale = input("Enter the temperature scale (C/F): ")
    if scale.upper() == 'C':
        temp_c = float(input("Enter the temperature in Celsius: "))
        temp_f = (temp_c * 9/5) + 32
        print(f"{temp_c}°C is equal to {temp_f}°F")
    elif scale.upper() == 'F':
        temp_f = float(input("Enter the temperature in Fahrenheit: "))
        temp_c = (temp_f - 32) * 5/9
        print(f"{temp_f}°F is equal to {temp_c}°C")
pass

weather