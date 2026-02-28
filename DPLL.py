import sys,random

global UCH,PSH
#UCH = False # can turn on with +UCH
UCH = True # on by default
PSH = False

# representation: 
#   a clause is a list of literals
#   tvals is a hash table that maps prop symbols to truth values (ints: 1=true, 0=false, -1=unknown)

class Clause:
  def __init__(self,s): # string
    self.signs = {} # +1 for pos lit, -1 for neg lit
    words = s.split()
    for w in words:
      if w[0]=='-': self.signs[w[1:]] = -1 # does not check for double neg, e.g. --P
      else: self.signs[w] = 1  
  def toString(self):
    s = ""
    for prop,sign in self.signs.items(): s += "%s%s " % ("-" if sign==-1 else "",prop)
    return s

def read_CNF_file(fname):
  clauses = []
  for line in open(fname):
    if "#" in line: line = line[:line.index("#")]
    line = line.rstrip()
    if len(line)==0: continue
    clauses.append(Clause(line))
  return clauses

# returns +1 (sat), -1 (model makes clause false), or 0 (unknown)
# assume clause is not empty, and all props are defined in model
# assume tvals of literals are always +/-1 (signs)

def truth_value(model,clause):
  unknowns = 0
  for prop,val in clause.signs.items():
    if val==model[prop]: return 1 # literal satisfied by model (both true or both false)
    if model[prop]==0: unknowns += 1
  if unknowns==0: return -1 # all literals falsified by model
  else: return 0 # some literals are false; some are unknown

def identify_pure_symbol(clauses,model):
  tvals = {} # keep track of whether each prop in non-sat clauses appears as + or -
  for clause in clauses:
    if truth_value(model,clause)==1: continue
    for prop in clause.tvals.keys(): 
      if prop not in tvals: tvals[prop] = set()
      tvals[prop].add(clause.tvals[prop])
  for prop in tvals:
    if prop not in model and len(tvals[prop])==1: return prop
  return None

def identify_unit_clause(clauses,model):
  for clause in clauses:
    if truth_value(model,clause)==1: continue # has at least one pos lit
    unks = []
    for prop,val in clause.signs.items():
      if model[prop]==0: unks.append(prop) # has exactly 1 unknown lit (the rest should be false)
    if len(unks)==1: p = unks[0]; return p,clause.signs[p]
  return None

calls = 0
DEBUG = True

def DPLL(model,clauses,props):
  global calls
  calls += 1
  if DEBUG: print("model: "+str(model)) # for debugging
  tvals = []
  for clause in clauses:
    s = truth_value(model,clause)
    if s==-1: print("backtracking"); return None # model makes at least one clause false
    tvals.append(s)
  if tvals.count(1)==len(tvals): return model # all clauses are satisfied by model, no unknowns or false

  if len(props)==0: return None
  if UCH:
    ans = identify_unit_clause(clauses,model) # None if not found, else prop,sign
    if ans!=None: 
      prop,sign = ans
      print("forcing %s=%s by UCH" % (prop,sign))
      i = props.index(prop)
      rest = props[:i]+props[i+1:]
      mod2 = model.copy()
      mod2[prop] = sign
      return DPLL(mod2,clauses,rest)

  prop,rest = props[0],props[1:]      
  mod2 = model.copy()
  mod2[prop] = 1 # try true
  if DEBUG: print("trying %s=T" % prop)
  mod3 = DPLL(mod2,clauses,rest)
  if mod3!=None: return mod3
  mod2[prop] = -1 # try false
  if DEBUG: print("trying %s=F" % prop)
  return DPLL(mod2,clauses,rest)

def extract_props(clauses):
  props = set()
  for clause in clauses:
    for prop in clause.signs.keys(): props.add(prop)
  return sorted(list(props))

def print_model(model): # a dict
  for prop in sorted(model.keys()): print("%s: %s" % (prop,model[prop]))

def sat_props(model): 
  sat = []
  for prop,sign in model.items():
    if sign==1: sat.append(prop)
  return sat

if __name__=="__main__":
  print("command: python DPLL.py "+(' ').join(sys.argv[1:]))
  clauses = read_CNF_file(sys.argv[1])
  for lit in sys.argv[2:]:
    if lit=="+PSH": PSH = True
    elif lit=="+UCH": UCH = True
    else: clauses.append(Clause(lit))

  props = extract_props(clauses)
  model = {}
  for prop in props: model[prop] = 0 # unknown

  #random.shuffle(props)
  print(props)
  #sys.exit(0)
  model = DPLL(model,clauses,props)
  if model==None: print("unsatisfiable")
  else: 
    print("solution:"); print_model(model)
    #print("clauses:")
    #for clause in clauses:
    #  print satisfies(model,clause),clause.toString()
    print("just the Satisfied (true) propositions:")
    print(' '.join(sat_props(model)))
  print("total DPLL calls: %s" % calls)
  print("UCH=%s, PSH=%s" % (UCH,PSH))
