"""Mrqueue is a mutil level ring buffer.
I got the inspiration from the multi-level paging mechanism.
Mrqueue get the value from the first primary queue. When need to store a value and the primary queue is
full, then put the value into Secondary Queue.
"""
import Queue

class MrRingBuffer():
    """
    MrRingBuffer class 
    """ 

    def __init__(self, levelSize=2, queueSize=0 ,activeMrQueue=0):
        self.levelSize = levelSize
        self.activeMrQueue = activeMrQueue
        self.queueSize = queueSize
        self.mrqueues = []
        for i in range(levelSize):
            queue = Queue.Queue(queueSize)
            self.mrqueues.append(queue)

    def get(self):
        if not self.mrqueues[self.activeMrQueue].empty():
            return self.mrqueues[self.activeMrQueue].get()
        else:
            self.activeMrQueue = (self.activeMrQueue + 1) % self.levelSize
            return self.mrqueues[self.activeMrQueue].get()

    def put(self, value):
        if self.mrqueues[self.activeMrQueue].full():
            self.mrqueues[(self.activeMrQueue + 1) % self.levelSize].put(value)
        else:
            self.mrqueues[self.activeMrQueue].put(value)

    def getActiveMrQueueNumber(self):
        return self.activeMrQueue

