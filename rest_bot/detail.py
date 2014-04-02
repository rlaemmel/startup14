#
# (C) Ralf Laemmel, 2014
#
# Get the choices for a poll from the Polls app
#

import sys
from commons import get

def detail(poll_id):
    raw = get("polls/"+str(poll_id)+"/")
    final = dict()
    for x in raw:
        final[int(x)] = raw[x]
    return final

# Extract the poll_id from the command line; default to 1
if __name__ == '__main__':
    last = len(sys.argv) - 1
    if last < 0: poll_id = 1
    else:
        try:
            poll_id = int(sys.argv[last])
        except ValueError:
            poll_id = 1
    print detail(poll_id)
