class base :
    def __init__(self,qad,vazn,sen,tedad):
        self.qad=qad
        self.vazn=vazn
        self.sen=sen
        self.tedad=tedad

    def get_qad(self):
        sum_qad=int()
        for i in self.qad:
            sum_qad+=i
        avg_qad=float(sum_qad/self.tedad)
        return avg_qad

    def get_vazn(self):
        sum_vazn=int()
        for i in self.vazn:
            sum_vazn+=i
        avg_vazn=float(sum_vazn/self.tedad)
        return avg_vazn

    def get_sen(self):
        sum_sen=int()
        for i in self.sen:
            sum_sen+=i
        avg_sen=float(sum_sen/self.tedad)
        return avg_sen


#A Grupe
inp_tedad_A=int(input())
inp_sen_A=input().split()
inp_qad_A=input().split()
inp_vazn_A=input().split()


inp_qad_A=list(map(lambda x: float(x),inp_qad_A))
inp_vazn_A=list(map(lambda x: float(x),inp_vazn_A))
inp_sen_A=list(map(lambda x: float(x),inp_sen_A))

classA=base(inp_qad_A,inp_vazn_A,inp_sen_A,inp_tedad_A)

#B Grupe
inp_tedad_B=int(input())
inp_sen_B=input().split()
inp_qad_B=input().split()
inp_vazn_B=input().split()


inp_qad_B=list(map(lambda x: float(x),inp_qad_B))
inp_vazn_B=list(map(lambda x: float(x),inp_vazn_B))
inp_sen_B=list(map(lambda x: float(x),inp_sen_B))

classB=base(inp_qad_B,inp_vazn_B,inp_sen_B,inp_tedad_B)

#output
print(classA.get_sen())
print(classA.get_qad())
print(classA.get_vazn())

print(classB.get_sen())
print(classB.get_qad())
print(classB.get_vazn())
if classA.get_qad()==classB.get_qad():
    if classA.get_vazn()==classB.get_vazn():
        print('Same')
    elif classA.get_vazn() < classB.get_vazn():
        print('A')
    elif classA.get_vazn()>classB.get_vazn():
        print('B')
elif classA.get_qad()>classB.get_qad():
    print('A')
elif classA.get_qad()<classB.get_qad():
    print('B')