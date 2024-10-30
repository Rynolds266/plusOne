def readData():
    f = open("runners.txt", "r")
    travels = []  # create the empty list
    for line in f:
        s = line.strip()  # strip off new line character from the end of the line
        name, city, miles, gallons = s.split("\t")  # unpack, split by tab
        # for calculations, convert miles to an int and gallons to a float
        # create dictionary, append it to list
        travels.append({'name': name, 'city': city, 'miles': int(miles), 'gallons': float(gallons)})
    f.close()
    return travels  # return the list of dictionaries

def displayData(trips):
    # trips is the list of dictionaries
    fs = "%-8s %-16s %7s %s"  # create format string
    print(fs % ("Name", "City", "Miles", "Gallons"))  # print header
    for t in trips:  # t is a dictionary
        fs = "%-8s %-16s %6s %5s"  # make format string
        print(fs % (t['name'], t['city'], t['miles'], t['gallons']))

def addTrip(trips):
    nom = input("Enter your first name: ")
    city = input("Enter destination city: ")
    mi = input("Enter miles traveled: ")  # get input
    gal = input("Enter gallons used: ")  # all the data are strings
    # create dictionary
    record = {'name': nom, 'city': city, 'miles': int(mi), 'gallons': float(gal)}
    trips.append(record)  # append dictionary to list
    return trips

def storeData(trips):
    f = open("runners.txt", "w")
    for t in trips:
        # convert each dictionary into a tab-separated string, then write to file
        record = "\t".join([str(t['name']), str(t['city']), str(t['miles']), str(t['gallons'])]) + "\n"
        f.write(record)
    f.close()

def main():
    travel_log = readData()  # read file, convert records to a list of dictionaries

    # Display existing travel log data
    print("Existing Travel Log:")
    displayData(travel_log)

    # Add a new trip
    print("\nAdd a New Trip:")
    travel_log = addTrip(travel_log)

    # Display updated travel log data
    print("\nUpdated Travel Log:")
    displayData(travel_log)

    # Store the updated travel log data
    storeData(travel_log)
    print("Travel log stored in 'runners.txt'.")

    while True:
        print("""Menu options. Choose 1, 2, or 3
        1. Display all trip data
        2. Add a trip
        3. Save and exit""")
        opt = input("Enter your choice, 1, 2 or 3: ")

        if opt == "1":
            print()  # print a blank line
            displayData(travel_log)
        elif opt == "2":
            travel_log = addTrip(travel_log)
        elif opt == "3":
            storeData(travel_log)
            print("Goodbye")
            print()
            break  # exit loop
        else:
            print("Invalid entry, please re-enter your choice")


if __name__ == "__main__":
    main()
