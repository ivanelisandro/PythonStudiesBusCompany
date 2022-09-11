def fahrenheit_to_celsius(temperature):
    reduction = 32
    ratio = 5 / 9
    result = (temperature - reduction) * ratio
    return round(result, 3)
