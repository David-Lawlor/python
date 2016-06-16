def printChoicesWithIndexes(arrayIn):
    for index, options in enumerate(arrayIn):
        print ((index + 1), options)


def convert_kph_to_mph(kilometers_in):
    print (kilometers_in, " Kilometers in miles is ", kilometers_in * 0.62137)


def convert_mph_to_kph(miles_in):
    print (miles_in, " Miles in kilometers is ", miles_in * 1.6093)


def convert_centimeters_to_inches(centimeter_in):
    print (centimeter_in, " centimeters in inches is ", centimeter_in * 0.39370)


def convert_inches_to_centimeters(inches_in):
    print (inches_in, " inches in centimeters is ", inches_in * 2.5400)


def convert_kilo_to_pounds(kilos_in):
    print (kilos_in, " kilos in pounds is ", kilos_in * 2.2046)


def convert_pounds_to_kilos(pounds_in):
    print (pounds_in, " pounds in kilos is ", pounds_in * 0.45359)


def take_input(conversion):
    print ("Enter the number of %s that you would like to convert" % conversion)
    return input()


conversions = ["Weight", "Length", "Speed", "Exit"]
speedConversions = ["KphToMph", "MphToKph"]
lengthConversions = ["CentimetersToInches", "InchesToCentimeters"]
weightConversions = ["KiloToPounds", "PoundsToKils"]
while True:
    print ("Enter the number for the conversion you would like")
    printChoicesWithIndexes(conversions)
    choice = input()
    print ("Choice is ", conversions[choice-1])

    if choice == 1:
        printChoicesWithIndexes(weightConversions)

        if choice == 1:
            convert_kilo_to_pounds(take_input("Kilos"))
        elif choice == 2:
            convert_pounds_to_kilos((take_input("pounds")))
        else:
            print("Not a valid option")

    elif choice == 2:
        printChoicesWithIndexes(lengthConversions)

        if choice == 1:
            convert_centimeters_to_inches(take_input("centimeters"))
        elif choice == 2:
            convert_inches_to_centimeters(take_input("inches"))
        else:
            print("Not a valid option")

    elif choice == 3:
        printChoicesWithIndexes(speedConversions)
        choice = input()

        if choice == 1:
            convert_kph_to_mph(take_input("Kilometers"))
        elif choice == 2:
            convert_mph_to_kph(take_input("Miles"))
        else:
            print("Not a valid option")

    elif choice == 4:
        print ("Exiting...................")
        break

    else:
        print ("Invalid Option")
