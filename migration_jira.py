#! /usr/bin/env python
import sys
import json
from pathlib import Path

component = 'Platform'
issue_type = 'Devops Build'

#trello_status = ['Backlog',
#                 'To Do',
#                 'Doing',
#                 'For Review',
#                 'MEP']

trello_status = ['To Do']


def convert_card():
    input_file = sys.argv[1]
    board = json.loads(Path(input_file).read_text())

    status = {s['id']: s['name'] for s in board['lists'] if not s['closed'] and s['name'] in trello_status}


    #print(status)
    id_items = [item[0] for item in status.items()]
    #print(id_items)
    cards = [card for card in board['cards'] if not card['closed'] and card['idList'] in id_items]
    for c in cards:
        c['status'] = status[c['idList']]
    #print(cards[0])

    print('Component,Issue Type,Status,Summary,Description')
    for card in cards:
        print(f"\"{component}\",\"{issue_type}\",\"{card['status']}\",\"{card['name']}\",\"Imported from {card['url']}\"")


if __name__ == '__main__':
    convert_card()
