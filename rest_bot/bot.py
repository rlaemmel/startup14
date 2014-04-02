#
# (C) Ralf Laemmel, 2014
#
# A bot for polls app:
# continuously vote to maintain a given choice of a given poll as the most popular
#

import sys
import time
from index import index
from detail import detail
from vote import vote

#
# Extract poll_id and choice_id from the command line
# Crash when command line arguments are missing
#
last = len(sys.argv) - 1
poll_id = int(sys.argv[last-1])
choice_id = int(sys.argv[last])

# Announce launch
print "Starting bot for poll " \
  + str(poll_id) \
  + " and choice " \
  + str(choice_id) \
  + " ..."

# Remind of the question
print "The question for poll ID " \
  + str(poll_id) \
  + " is \"" \
  + index()[poll_id] \
  + "\"."

# Remind of the choice
print "The choice for choice ID " \
  + str(choice_id) \
  + " is \"" \
  + detail(poll_id)[choice_id]["choice"] \
  + "\" with current popularity " \
  + str(detail(poll_id)[choice_id]["votes"]) \
  + "."

# Start an infinite loop (use CTRL-C)
try:
    while True:
        max = choice_id
        data = detail(poll_id)
        for x in data:
            if x != choice_id and data[choice_id]["votes"] <= data[x]["votes"]:
                max = x
        if max == choice_id:
            print "Popularity maintained."
        else:
            
            # Report popularity challenge
            print "Popularity challenged by \"" \
              + data[max]["choice"] \
              + "\" with current popularity " \
              + str(data[max]["votes"]) \
              + "."

            # Report on corrective vote
            print "Vote!"
            result = vote(poll_id, choice_id)
            print "The resulting popularity of \"" \
              + data[choice_id]["choice"] \
              + "\" is " \
              + str(result) \
              + "."
                        
        time.sleep(1)
except KeyboardInterrupt:
    print ""
    print "Finishing"
