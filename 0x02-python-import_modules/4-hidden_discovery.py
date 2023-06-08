#!/usr/bin/python3.8

if __name__ == "__main__":
    import hidden_4
    for e in dir(hidden_4_pyc):
        if e[0] != "_":
            print("{}".format(e))
