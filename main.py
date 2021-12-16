# Задание 3
class MyStack:
    def __init__(self):
        self.container = []
        self.max = 0
        self.t = 0

    def appendTiming(self, item):
        item.append(self.t)
        e = (self.t + item[1])
        item.append(e)
        self.container.append(item)

    def push(self, item):
        if self.max == 0:
            return -1
        if len(self.container) == 0:
            self.t = item[0]
            self.appendTiming(item)
            return self.t
        if len(self.container) < self.max:
            self.t = self.t + self.container[-1][1] if self.t + self.container[-1][1] > item[0] else item[0]
            self.appendTiming(item)
            if item[0] >= self.container[0][3]:
                self.container.pop(0)
            return self.t
        else:
            if item[0] >= self.container[0][3]:
                self.t = self.t + self.container[-1][1] if self.t + self.container[-1][1] > item[0] else item[0]
                self.container.pop(0)
                self.appendTiming(item)
                return self.t
            else:
                return -1

    def size(self, max):
        self.max = max

myOutput = []


def runStack():
    stack = MyStack()
    with open('input1.txt') as f:
        line = f.readline()
        max_qty = [int(s) for s in line.split(" ")]
        stack.size(max_qty[0])
        i = 0
        while line and i < max_qty[1]:
            i += 1
            line = f.readline()
            if line:
                item = [int(s) for s in line.split(" ")]
                myOutput.append(str(stack.push(item)) + '\n')


    f = open("output1.txt", "w")
    for line in myOutput:
        f.write(line)
    f.close()


runStack()


# Задание 5
class StackArray:
    def __init__(self):
        self.container = []
        self.t = 0

    def appendTiming(self, item):
        item.append(self.t)
        e = (self.t + item[1])
        item.append(e)
        self.container.append(item)

    def push(self, item):
        for i in range(len(self.container)):
            if len(self.container[i]) == 0:
                self.container[i].append(item)
                return str(i) + ' 0\n'

        st = [sum(i) for i in self.container]
        mint = min(st)
        for i in range(len(self.container)):
            if sum(self.container[i]) == mint:
                t = mint
                self.container[i].append(item)
                return str(i) + ' ' + str(t) + '\n'


    def size(self, max):
        for i in range(max):
            self.container.append([])


def runStackArray():
    stack = StackArray()
    with open('input2.txt') as f:
        line = f.readline()
        max_qty = [int(s) for s in line.split(" ")]
        stack.size(max_qty[0])
        line = f.readline()
        items = [int(s) for s in line.split(" ")]
        index = 0
        for i in items:
            index += 1
            if index > max_qty[1]:
                break
            myOutput.append(stack.push(i))


    f = open("output2.txt", "w")
    for line in myOutput:
        f.write(line)
    f.close()

myOutput = []
# runStackArray()


import time
t_start = time.perf_counter()

# runStack()
# runStackArray

print("Время работы: %s секунд " % (time.perf_counter() - t_start))