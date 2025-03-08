import sys
from report import print_report

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        print_report(sys.argv[1])

main()
