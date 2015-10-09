import argparse
from tail import Tail

def main():
    parser = argparse.ArgumentParser(description='Read and display file from the end.')
    parser.add_argument('file', metavar='FILE', type=str,
                       help='file name to be tailed.')
    parser.add_argument('-n', dest='lines', type=int, default=10,
                       help='display last [n] lines')
    parser.add_argument('-f', dest='follow', action='store_true', default=False,
                        help='continuosly tailing file.')
    parser.add_argument('-s', dest='sleep', type=float, default=1.0,
                        help='with -f, sleep for N seconds, (deafult 1.0)')

    args = parser.parse_args()
    tail = Tail(open(args.file, 'rb'))
    try:
        if args.follow:
            tail.seek_end()
            for line in tail.follow(delay=args.sleep):
                print line            
        else:
            if args.lines > 0:
                lines = tail.tail(args.lines)

            for line in lines:
                print line
    except KeyboardInterrupt:
        pass
    finally:
        tail.close()

if __name__ == "__main__":
    main()