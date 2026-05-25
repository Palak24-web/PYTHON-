def fahernheit_to_celcius(fahrenheit):
    return 5 * (farehnheit-32) / 9

    fahrenheit=int(input("enter tempature in fahrenheit:"))
    c= fahernheit_to_celcius(fahrenheit)
    print(f" {round(c,2)} ° C")  # round is used to round off the decimal value to only 2 places or given places