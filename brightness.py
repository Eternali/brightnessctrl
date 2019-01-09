#!/usr/bin/python3

from enum import Enum
from fullcolor.colors import Color
from fullcolor.common import CommonColors as c
from os import system, linesep, getuid
from sys import argv


class LOG_LEVELS(Enum):
    ALL = 0
    INFO = 1
    DEBUG = 2
    CRITICAL = 3
    ERROR = 4

    def __lt__(self, other):
        return self.value < other
    
    def __gt__(self, other):
        return self.value > other
    
    def __eq__(self, other):
        return self.value == other


LOG_LEVEL = LOG_LEVELS.ALL
GREY = Color('999999')
ORANGE = Color('FFA500')

def log(msg, level=LOG_LEVELS.ALL):
    if level < LOG_LEVEL:
        return

    if level == LOG_LEVELS.ALL:
        col = GREY
    if level == LOG_LEVELS.INFO:
        col = c.GREEN
    if level == LOG_LEVELS.DEBUG:
        col = c.BLUE
    elif level == LOG_LEVELS.CRITICAL:
        col = ORANGE
    elif level == LOG_LEVELS.ERROR:
        col = c.RED
    else:
        return

    print(col.fg + msg + c.RT)


def check_perms():
    if getuid != 1000:
        log('You are not a sudoer, try running again with root permissions.', LOG_LEVELS.DEBUG)


def read_brightness(bright_file):
    try:
        with open(bright_file, 'r') as bf:
            return int(bf.readline())
    except Exception as e:
        log(e.message, LOG_LEVELS.ERROR)


def write_brightness(bright, bright_file):
    try:
        with open(bright_file, 'w') as bf:
            bf.write(f'{bright}{linesep}')
    except PermissionError as e:
        check_perms()
    except Exception as e:
        log(e.message, LOG_LEVELS.ERROR)


def has_arg(args, to_find):
    return any(a in args for a in to_find)


def consume_named(args, to_consume):
    consumed = []
    for arg in to_consume:
        if arg in args:
            consumed.append(args[args.index(arg) + 1])
            args.remove(consumed[-1])
    return consumed if len(consumed) > 1 else consumed[0] if len(consumed) == 1 else None

def main():
    LOG_LEVEL = int(consume_named(argv, ['-l, --log-level']) or 0)
    bright_file = consume_named(argv, ['-f', '--file']) or '/sys/class/backlight/amdgpu_bl0/brightness'
    interval = int(consume_named(argv, ['-i', '--interval']) or 10)
    change = interval if has_arg(argv, '+') else -1 * interval
    new_brightness = read_brightness(bright_file) + change
    log(f'Setting brightness to {new_brightness}', LOG_LEVELS.INFO)
    write_brightness(new_brightness, bright_file)


if __name__ == '__main__':
    main()

