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


def read_block():
    """Iterate over fixed sized records"""
    from functools import partial

    RECORD_SIZE = 32
    # for binary files
    with open("somefile.data", "rb") as f:
        records = iter(partial(f.read(), RECORD_SIZE), b"")
        for r in records:
            print(r)


def buffer_read():
    """Read binary data into mutable buffer"""
    import os.path

    def read_into_duffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, "rb") as f:
            f.readinto(buf)
        return buf

    # write a sample file
    # with open("sample.bin", "wb") as f:
    #     f.write(b"Hello world")

    buf = read_into_duffer("sample.bin")
    print(buf)

    with open("newsample.bin", "wb") as f:
        f.write(buf)


# def memory_mapping():
#     """Memory mapping binary files"""
#     import os
#     import mmap
#
#     def memory_map(filename, access=mmap.ACCESS_WRITE):
#         size = os.path.getsize(filename)
#         fd = os.open(filename, os.O_RDWR)
#         return mmap.mmap(fd, size, access=access)
#
#     ...

def learn_ospath()
    """Use the path name to get the file name, directory name, absolute path"""
    import os.path
    path = f"/Users/beazley/Data/data.csv"
    # get the last component of the path
    os.path.basename(path)
    # get the directory name
    os.path.dirname(path)
    # join path component together
    os.path.join("tmp","data",os.path.basename(path))

    # expand the user's home directory
    path = f'~/Data/data.csv'
    os.path.expanduser(path)
    # split the file extension
    os.path.split(path)

