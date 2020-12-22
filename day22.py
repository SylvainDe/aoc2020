# vi: set shiftwidth=4 tabstop=4 expandtab:
import datetime


def get_decks_from_file(file_path="day22_input.txt"):
    with open(file_path) as f:
        return get_decks_from_string(f.read())


def get_decks_from_string(string):
    return [[int(c) for c in d.splitlines()[1:]] for d in string.split("\n\n")]


def play_game(deck1, deck2):
    while deck1 and deck2:
        c1, c2 = deck1.pop(0), deck2.pop(0)
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        elif c2 > c1:
            deck2.append(c2)
            deck2.append(c1)
        else:
            assert False
    # Compute score
    return sum(i * c for i, c in enumerate(reversed(deck1 + deck2), start=1))


def run_tests():
    example1 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
    deck1, deck2 = get_decks_from_string(example1)
    assert play_game(deck1, deck2) == 306


def get_solutions():
    deck1, deck2 = get_decks_from_file()
    print(play_game(deck1, deck2) == 35397)


if __name__ == "__main__":
    begin = datetime.datetime.now()
    run_tests()
    get_solutions()
    end = datetime.datetime.now()
    print(end - begin)
