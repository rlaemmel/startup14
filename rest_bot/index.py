#
# (C) Ralf Laemmel, 2014
#
# Get the index of polls from the Polls app
#

from commons import get

def index():
    raw = get("polls/")
    final = dict()
    for x in raw:
        final[int(x)] = raw[x]
    return final

if __name__ == '__main__':
    print index()
