import os
import sys


if __name__ == '__main__':
    real_path = os.path.realpath(sys.argv[1])
    dir_path = os.path.dirname(real_path)
    executable = sys.executable
    print(f'cd "{dir_path}" ')
    print(f'"{executable}" "{real_path}" ')
