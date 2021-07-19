# the QUEUE Data Structure use the concept of FIFO just like the traditional queuing system
# in this case, the LIST DS won't cut it
# I will import DEQUE from COLLECTIONS

from collections import deque

# define a variable for the container holding the queue
queue = deque([])
queue.append("Jane")
queue.append("Jason")
queue.append("Page")
# queue.append("Mark")
# queue.append("Federico")
queue.popleft()
queue.popleft()
queue.popleft()
# we can mess with this a little bit
# ask user whether they want to empty the queue
last_person = True
if not last_person:
    print("Someone is still on the LINE")
else:
    queue.popleft()

# at this point we can test for when the condition is false
print(queue)
if not queue:
    # this execute to be true and print "no one on the queue, awesome
    print("End of LINE, No one on the queue !!!")
