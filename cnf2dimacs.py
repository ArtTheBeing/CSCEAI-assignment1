import sys

lines = []
for line in open(sys.argv[1]): lines.append(line.rstrip())

symboltable = {}

for line in lines:
  if line.startswith("p cnf") or len(line)==0: continue
  w = line.split()
  if w[-1]=="0": w = w[:-1] 
  for sym in w:
    if sym[0]=='-': sym = sym[1:]
    symboltable[sym] = 1


n = 1
for (sym,num) in symboltable.items(): 
  symboltable[sym] = n   
  print("c symtable: %s = %s" % (n,sym))
  n += 1

nclauses = 0
for line in lines:
  if line.startswith("p cnf") or len(line)==0: continue
  nclauses += 1

print("p cnf %d %d" % (len(symboltable),nclauses))

for line in lines:
  if line.startswith("p cnf") or len(line)==0: print(line); continue
  w = line.split()
  if w[-1]=="0": w = w[:-1] 
  numbers = []
  for sym in w:
    sign = ""
    if sym[0]=='-': sym,sign = sym[1:],"-"
    numbers.append("%s%s" % (sign,symboltable[sym]))
  numbers.append("0")
  print(' '.join(numbers))

