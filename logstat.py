from collections import defaultdict
import os
import pathlib
import re
import datetime
import sys
from typing import Generator

def parse_log_line(line: str) -> dict:
    parts = re.split(r'(INFO|DEBUG|WARNING|ERROR)', line)
    if len(parts) < 2:
        return None

    return {
        'timestamp': datetime.datetime.strptime(parts[0].strip(), '%Y-%m-%d %H:%M:%S'),
        'level': parts[1].strip().upper(),
        'message': ''.join(parts[2:]).strip()
    }

def load_logs(path: str) -> Generator[dict]:
    if not path:
        return []

    if not os.path.isfile(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield parse_log_line(line)
        return None


def filter_logs_by_level(logs: Generator[dict], level: str) -> Generator[dict]:
    for log in logs:
        if level:
            if log['level'].upper() == level.upper():
                yield log
        else:
            yield log

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1

    return dict(counts)

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:17}| {count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python logstat.py <path_to_log_file> <level>")
        sys.exit(1)

    path = pathlib.Path(sys.argv[1].strip()).absolute
    level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    # path = pathlib.Path('example.log').absolute()
    # level = 'ERROR'

    display_log_counts(count_logs_by_level(load_logs(path)))

    if level:
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filter_logs_by_level(load_logs(path), level):
            print(f"{log['timestamp']} - {log['message']}") 

    sys.exit(0)
