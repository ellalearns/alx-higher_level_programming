#!/usr/bin/python

if __name__ == "__main__":
    """prints from hidden pyc"""
    import hidden_4

    files = dir(hidden_4)
    for file in files:
        if file[0:2] != "__":
            print(file)
