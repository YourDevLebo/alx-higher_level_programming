#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i_sum = 0
    if len(sys.argv) - 1 > 0:
        for i in range(1, len(sys.argv)):
            i_sum += int(str(sys.argv[i]))
    print("{}".format(i_sum))
