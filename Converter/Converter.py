def printChoicesWithIndexes(arrayIn):
    for index, options in enumerate(arrayIn):
        print ((index + 1), options)


def convert_kph_to_mph(kilometers_in):
    print (kilometers_in, " Kilometers in miles is ", kilometers_in * 0.62137)


def convert_mph_to_kph(miles_in):
    print ""


def convert_centimeters_to_inches():
    print ""


def convert_inches_to_centimeters():
    print ""


def convert_kilo_to_pounds():
    print ""


def convert_pounds_to_kilos():
    print ""


def take_input(conversion):
    print ("Enter the number of %s that you would like to convert" % conversion)
    return input()


conversions = ["Weight", "Length", "Speed", "Exit"]
speedConversions = ["KphToMph", "MphToKph"]
lengthConversions = ["CentimetersToInches", "InchesToCentimeters"]
weightConversions = ["KiloToPounds", "PoundsToKils"]
while True:
    print ("Enter The conversion you would like")
    printChoicesWithIndexes(conversions)
    choice = input()
    print ("Choice is ", conversions[choice-1])

    if choice == 1:
        printChoicesWithIndexes(weightConversions)

        if choice == 1:
            print("1")
        elif choice == 2:
            print("2")
        else:
            print("Not a valid option")

    elif choice == 2:
        printChoicesWithIndexes(lengthConversions)

        if choice == 1:
            print("1")
        elif choice == 2:
            print("2")
        else:
            print("Not a valid option")

    elif choice == 3:
        printChoicesWithIndexes(speedConversions)
        choice = input()

        if choice == 1:
            convert_kph_to_mph(take_input("Kilometers"))
        elif choice == 2:
            print("2")
        else:
            print("Not a valid option")

    elif choice == 4:
        print ("Exiting...................")
        break

    else:
        print ("Invalid Option")
