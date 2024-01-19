#!/usr/bin/python3

if __name__ == "__main__":
    """prints from hidden pyc"""
    import hidden_4

    filenames = dir(hidden_4)
    for filename in filenames:
        if filename[0:2] != "__":
            print(filename)
