#
# (C) Ralf Laemmel, 2014
#
# Vote through the Polls app
#

import sys
from commons import post

#
# Send vote via POST request
# Return post-POST request number of votes
#
def vote(poll_id, choice_id):
    content = dict()
    content["poll"] = poll_id
    content["choice"] = choice_id
    return int(post("vote/", content))

#
# Extract poll_id and choice_id from the command line
# Crash when command line arguments are missing
#
if __name__ == '__main__':
    last = len(sys.argv) - 1
    poll_id = int(sys.argv[last-1])
    choice_id = int(sys.argv[last])
    print vote(poll_id, choice_id)
