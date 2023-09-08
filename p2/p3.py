import random

class base:

    def __init__(self):
        self.name = input().split()
           
    def show(self):
        A = random.sample(self.name, 11)
        for j in range(0,11):
            for k in range(0, len(self.name)):
                if A[j] == self.name[k]:
                    self.name.pop(k)
                    break
        B = self.name
        for i in range(0,11):
            print (A[i], 'A')
        for l in range(0,11):
            print (B[l], 'B')
        
class Footbalist(base):
    pass

a = Footbalist()
a.show()