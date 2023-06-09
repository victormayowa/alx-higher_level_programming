#!/usr/bin/python3.8

if __name__ == "__main__":
    import sys
    import hidden_4
    module_names = dir(hidden_4)
    filtered_names = sorted(name for name in module_names if not name.startswith("__"))
    for name in filtered_names:
        for name in filtered_names:
            print("{}".format(name))

