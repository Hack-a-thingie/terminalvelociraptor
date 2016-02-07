import random

journals = []

journals.append(["Science", 80, 10])
journals.append(["Nature", 60, 9])
journals.append(["Physical Review Letters", 40, 7])
journals.append(["New Journal of Physics", 20, 4])
journals.append(["Physical Review A", 20, 3])
journals.append(["Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki", 10, 2])
journals.append(["arxiv", 1, 1])


def try_journal(name, value, param):

    print("Trying in %s with %d..." % (name, value)),
    if value > random.randrange(param):
        return True
    else:
        return False


def submit_manuscript(points):
    total = points.APG + points.APP + points.APC + points.APM + points.APB
    for journal in journals:
        if try_journal(journal[0], total, journal[1]):
            print("\033[1;32;48mACCEPTED! \033[0m")
            return journal[2]
        else:
            print("\033[1;31;48mREJECTED! \033[0m")

    return 0
