print("OOP, (c) Verloka Vadim 2018\n\n\n")

import classA
import classB

d = classA.A()

d.test1()
d.test2()
d.F = "simple"
d.test2()

print("P: {}".format(d._P))
d.GetP()

#print("G: {}".format(d.__G))       #exception
print("G: {}".format(d._A__G))      #do not throw exception
d.GetG()

f = classB.B()

f.test1()
f.test2()
f.test3()