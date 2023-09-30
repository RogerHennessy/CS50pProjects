# Roger Hennessy
# 07-09-2023

# Create our main function
# Here we will just ask for input then send it to convert()
def main():
    inputFace = input("Whats you face? ")
    convert(inputFace)

# Create our convert function. In here we will just replace/update the faces.
def convert(faces="noFace"):
    print ("",faces.replace(":(","🙁").replace(":)","🙂"))



# Lets call main()
if __name__ == "__main__":
    main()
