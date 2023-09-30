# Roger Hennessy
# 08-09-2023

# Create main()
def main():
    # Ask user from input
    fileType = input ("Please enter your file name: ")

    # Call checkExtension()
    checkExtensions(fileType)


# Create checkExtensions()
def checkExtensions(name):
    # Make it lower case
    name = name.lower()

    # Check filetype and output information
    if ("." in name):
        # Here we have a nested if statement, for all required files types.
        # I think a switch statement could be here also.
        if (".gif"in name):
            print ("image/gif")

        elif (".jpg" in name or "jpeg" in name):
            print ("image/jpeg")

        elif (".png" in name):
            print ("image/png")

        elif (".pdf" in name):
            print ("application/pdf")

        elif (".txt" in name):
            print ("text/plain")

        elif (".zip" in name):
            print ("application/zip")

        else:
            print ("application/octet-stream")

    # No "." so no extension
    else:
        print ("application/octet-stream")

# Call main()
if __name__ == "__main__":
    main()