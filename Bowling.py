Frame # = 1
d = 10
while Frame <= 10:
   if d == 10: 
      d = int(input("Number of pins down: "))
      s = 10
      Frame # = Frame # + 1
   elif d < 10:
      e = 10-d
      d = int(input("Number of pins down (0-%d)" % e))
      if d = e:
         s = 10 
      elif d != e:
         s = 10 - e
print("Total score is %d" % s)
