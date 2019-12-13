#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    var = len(sys.argv)
    if var <= 1:
        print("{}".format("0"))
    else:
        if var == 2:
            print("{:s}".format(sys.argv[1]))
        else:
            print("{:d}".format(sum(int(num) for num in sys.argv[1:])))
