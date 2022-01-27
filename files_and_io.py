def read_write():
    """read write text data"""
    # read the entire file as a single string
    with open("somefile.txt", "rt") as f:
        f.read()
        f.readlines()
        # Iterate over the lines of the file
        for line in f:
            print(line)

    # Write chunks of text data
    with open("Output.txt", "at") as f:
        f.write("I saw an angle")
        # Redirected print statement
        print("Hello, it's me", file=f)

    # if don't use with with statement, need manually close file
    f = open("somefile.txt", "rt")
    data = f.read()
    f.close()

    # print to file
    with open("test.txt", "wt") as f:
        print("someone like you", file=f)


def learn_print():
    "Usage of separator and line end"
    print("a", 1, 2, 3)
    print("a", 1, 2, 3, sep=",")
    print("a", 1, 2, 3, end="!!\n")

    # print in one line
    for i in range(5):
        print(i, end=" ")



