import json
from random import choice


def gen_person():
    name = ''
    tel = ''
    key = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    while len(key) != 10:
        key += choice(nums)

    person = {
        key: {
            'name': name,
            'tel': tel
        }
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons_dict.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open("persons_dict.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())

