#somador on off
import re

data = None
with open('input.txt', 'r') as file:
    data = file.read()

def somador_on_off(text):
    total = 0
    counting = False

    pattern = re.compile(r'(?i)(?P<on>\bon\b)|(?P<off>\boff\b)|\s(?P<equals>[=])\s|\b(?P<number>\d+)\b')

    for match in pattern.finditer(text):
        if match.group('on'):
            counting = True
        elif match.group('off'):
            counting = False
        elif match.group('equals') and counting:
            print("Current sum:", total)
        elif match.group('number') and counting:
            total += int(match.group('number'))

somador_on_off(data)
