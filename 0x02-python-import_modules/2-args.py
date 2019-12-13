#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    var = len(sys.argv) - 1
    if var > 0:
        if var == 1:
            print(var, "argument:")
            print("{:d}:".format(var), sys.argv[var], end='\n')
        else:
            print(var, "arguments:")
            for name in range(var):
                print("{:d}:".format(name + 1), sys.argv[name + 1], end='\n')
    else:
        print(var, "arguments.")
