#!/usr/bin/python3

if __name__ == "__main__":
    import py_compile
    py_compile.compile("hidden_4.py")
    with open("hidden_4.pyc", "rb") as file:
        magic = file.read(4)  # Read the magic number
        timestamp = file.read(4)  # Read the timestamp
        file.read(4)  # Ignore the size field               
        names = []
        while True:
            byte = file.read(1)
            if byte == b'':
                break
            size = int.from_bytes(byte, byteorder='little')  # Get the size of the name
            name = file.read(size).decode()  # Read the name
            if not name.startswith("__"):
                names.append(name)
            names.sort()
            for name in names:
                print("{}".format(name))
