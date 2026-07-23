from argparse import ArgumentParser


def arg_parser():
    parser = ArgumentParser()

    parser.add_argument(
        'greeting', default=None, type=str, help='Greeting msg')

    parser.add_argument(
        '-n', '--numbers', type=float, default=0, nargs=3,
        help='add 3 numbers')

    parser.add_argument(
        '-c', '--chars', type=str, nargs='*', default=None,
        help='add characters')

    parser.add_argument(
        '-t', '--trials', type=int, choices=[1, 2, 3, 4, 5], default=0,
        help='How many times u ran the gode before getting it right')

    return parser.parse_args()


def main():
    args = arg_parser()
    print(args)
    print(args.greeting)
    print(args.numbers[1]*args.numbers[0] + args.numbers[2])
    print('Your next Password must be:', args.chars[-1]+args.chars[0]+'Meow@9')

    adj = ''
    if args.trials <= 2:
        adj = "\033[32mLEGEND\033[0m"
    if args.trials > 2:
        adj = '\033[31mLOOSER\033[0m'
    print('it took you', args.trials, f'trials to get it right! What a {adj}!')


if __name__ == '__main__':
    main()
