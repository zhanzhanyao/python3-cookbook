def read_write():
    """read write text data"""
    # read the entire file as a single string
    with open("somefile.txt","rt") as f:
        f.read()
        f.readlines()
    # Iterate over the lines of the file
        for line in f:
            print(line)

    # Write chunks of text data
    with open("Output.txt","at") as f:
        f.write("I saw an angle")
    # Redirected print statement
        print("Hello, it's me", file=f)

    # if don't use with with statement, need manually close file
    f = open("somefile.txt","rt")
    data = f.read()
    f.close()




