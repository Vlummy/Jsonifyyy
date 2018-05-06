import sys
from Modules.Jsonify import Jsonify

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

    a = Jsonify()
    a.run()


if __name__ == "__main__":
    main()