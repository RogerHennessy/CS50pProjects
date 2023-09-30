# Roger Hennessy
# 10-09-2023

# Create main()
def main():
    #Here we will get input from the user and then send it to convert()
    userInput = input("Please tell me the time, in 24hr format: ")

    convert(userInput)


# Create convert()
def convert(time):
    # Here we will convert the time into hours and mins.
    hour, mins = time.split(":")
    mins = float(mins)
    hour = float(hour)
    mins = float(round(mins/60,2))

    timeDecimal = (hour + mins)

    if(hour >=7 and hour <= 8):
        print ("breakfast time")

    elif(hour >= 12 and hour <= 13):
        print ("lunch time")

    elif(hour >= 18 and hour <= 19):
        print ("dinner time")

    else:
        print("")

    return timeDecimal

# Call main()
if __name__ == "__main__":
    main()
