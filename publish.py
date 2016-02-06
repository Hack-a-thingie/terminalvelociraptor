
import random

journal_values = {}
journal_values["Nature"] = [60, 20]
journal_values["PRL"] = [40, 20]
journal_values["PRA"] = [20, 20]
journal_values["Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki"] = [10, 20]
journal_values["arxiv"] = [1, 20]

journals = ["Nature", "PRL", "PRA", "Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki", "arxiv"]

def try_journal(name, value, param):
    print "Trying in %s with %d..." % (name, value)
    if value > random.randrange(param):
        return True
    else:
        return False

def submit_manuscript(points):
    total = points.APG + points.APP + points.APC + points.APM + points.APB
    for journal in journals:
        if try_journal(journal, total, journal_values[journal][0]):
            print "ACCEPTED!"
            return journal_values[journal][1]

    return 0
