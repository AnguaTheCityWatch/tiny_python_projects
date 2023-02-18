#!/usr/bin/env python3
"""
Autor: Ken Youncen-Clark
Purpose: Say Hello, while learning Python basics.
"""

import argparse


def get_args():
    """
    Get the command line arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='Name to greet')
    return parser.parse_args()


def main():
    """
    This is where the job is done
    """
    args = get_args()
    name = args.name
    print('Hello, ' + name + '!')


if __name__ == '__main__':
    main()
