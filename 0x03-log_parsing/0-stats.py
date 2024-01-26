#!/usr/bin/python3
import re

pat = re.compile(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d{1,4})")

file_size = 0
status_codes = {}
lines = 0

interrupted = False

while not interrupted:
    try:
        line = input()

        match = pat.match(line)
        if not match:
            continue

        status_code = int(match.group(1))
        size = int(match.group(2))

        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        file_size += size

        lines += 1

        if lines == 10:
            print(f"File size: {file_size}")
            keys = sorted(status_codes.keys())
            for key in keys:
                print(f"{key}: {status_codes.get(key)}")
            status_codes.clear()
            lines = 0
    except KeyboardInterrupt as e:
        interrupted = True
        result = f"File size: {file_size}\n"
        keys = sorted(status_codes.keys())
        for key in keys:
            result += f"{key}: {status_codes.get(key)}\n"
        print(result)
