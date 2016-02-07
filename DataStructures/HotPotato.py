#Simulation: Hot Potato
# http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html

import Queue
import random

def hotPotato(namelist, num):
    simqueue = Queue.Queue(10)
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.getsize() > 1:
        for i in xrange(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == '__main__':
    tmp = hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], random.randint(7, 12))
    print tmp
