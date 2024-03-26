#!/usr/bin/python3
import re
import sys

pat = re.compile(
    r"\d+.\d+.\d+.\d+ - \[.*\] \"GET /\w+/260 HTTP/1.1\" (\d{3}) (\d{1,4})")

file_size = 0
status_codes = {}
lines = 0


def print_msg(file_size, status_codes):
    result = f"File size: {file_size}\n"
    keys = sorted(status_codes.keys())
    for key in keys:
        result += f"{key}: {status_codes.get(key)}\n"
    result.rstrip('\n')
    sys.stdout.write(result)


try:
    while True:
        try:
            line = input()
        except EOFError:
            break

        match = pat.match(line)
        if not match:
            continue

        status_code = int(match.group(1))
        size = int(match.group(2))

        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        file_size += size

        lines += 1

        if lines == 10:
            print_msg(file_size, status_codes)
            status_codes.clear()
            lines = 0
finally:
    print_msg(file_size, status_codes)
