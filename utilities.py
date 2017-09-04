from itertools import *


def input_is_integer(a):
    try:
        if float(a):
            return True
    except ValueError:
        return False


def grouper(iterable, n, fillvalue):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))


def kicker_score(fgm):
    return fgm * 3


def running_back_score(rushingyds, rushingtds):
    return rushingyds * .1 + rushingtds * 6


def quarterback_score(passingyds, passingtds, interceptions):
    return passingyds * .04 + passingtds * 6 - interceptions * 2


def receiver_scoring(receptions, receivingyds, receivingtds):
    return receptions * .5 + receivingyds * .1 + receivingtds * 6


def draft_order_randomizer(teams):
    order = random.sample(range(1, (len(teams) + 1)), k=len(teams))
    draft_order = [[teams[i], order[i]] for i in range(len(teams))]

    return draft_order

