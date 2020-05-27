import json
import os

DECK = 'ruslan-cartoon-1'

os.system('drill-srs create-deck {}'.format(DECK))

with open('temp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        russian = line.split('-')[0].strip()
        english = line.split('-')[1].strip()

        os.system('drill-srs add-card {} -q "{}" -a "{}"'.format(
            DECK, russian, english
        ))
        os.system('drill-srs add-card {} -q "{}" -a "{}"'.format(
            DECK, english, russian
        ))

        print('{}/{}'.format(i + 1, len(lines)))
