import sys
from Sexpr import *

def convCNF(expr):
  expr = eliminate_biconditionals(expr)
  expr = eliminate_xors(expr)
  expr = eliminate_implications(expr)
  expr = push_negs_inward(expr)
  expr = distribute(expr)
  expr = or_wrapper(expr) 
  return expr

def or_wrapper(expr):
  if expr.list==None or (is_disjunction(expr)==False and is_conjunction(expr)==False):
    return make_Sexpr_from_list(['or',expr])
  return expr

def make_Sexpr_from_list(lst): 
  expr = Sexpr(tokenize(""),0)
  expr.list = [x if isinstance(x,Sexpr) else Sexpr(tokenize(x),0) for x in lst]
  return expr

def negate(expr): return make_Sexpr_from_list([Sexpr('not'),expr])

def eliminate_implications(expr):
  if expr.atom!=None: return expr
  oper = expr.list[0]
  if oper.atom=="->" or oper.atom=="implies":
    if len(expr.list)!=3: raise Exception("implication can only have 2 arguments")
    a,b = expr.list[1],expr.list[2]
    newlist = ['or',negate(a),b]
    newexpr = make_Sexpr_from_list(newlist)
    return eliminate_implications(newexpr)
  else:
    return make_Sexpr_from_list([eliminate_implications(x) for x in expr.list])

def eliminate_biconditionals(expr):
  if expr.atom!=None: return expr
  oper = expr.list[0]
  if oper.atom=="<->":
    if len(expr.list)!=3: raise Exception("biconditional can only have 2 arguments")
    a,b = expr.list[1],expr.list[2]
    newlist1 = ['->',a,b]
    newlist2 = ['->',b,a]
    newexpr1 = make_Sexpr_from_list(newlist1) 
    newexpr2 = make_Sexpr_from_list(newlist2) 
    newlist = ["and",newexpr1,newexpr2]
    newexpr = make_Sexpr_from_list(newlist) 
    return eliminate_biconditionals(newexpr)
  else:
    return make_Sexpr_from_list([eliminate_biconditionals(x) for x in expr.list])

def eliminate_xors(expr):
  if expr.atom!=None: return expr
  oper = expr.list[0]
  if oper.atom=="xor":
    if len(expr.list)!=3: raise Exception("xor can only have 2 arguments")
    a,b = expr.list[1],expr.list[2]
    newlist1 = ['and',a,negate(b)]
    newlist2 = ['and',b,negate(a)]
    newexpr1 = make_Sexpr_from_list(newlist1) 
    newexpr2 = make_Sexpr_from_list(newlist2) 
    newlist = ["or",newexpr1,newexpr2]
    newexpr = make_Sexpr_from_list(newlist) 
    return eliminate_xors(newexpr)
  else:
    return make_Sexpr_from_list([eliminate_xors(x) for x in expr.list])

def push_negs_inward(expr):
  if expr.atom!=None: return expr
  if expr.list[0].atom=='not':
    subexpr = expr.list[1]
    if subexpr.atom!=None: return expr
    oper = subexpr.list[0]
    if oper.atom=="and" or oper.atom=="or":
      args = subexpr.list[1:]
      args = [negate(x) for x in args]
      args = [push_negs_inward(x) for x in args]
      flipop = "and" if oper.atom=="or" else "or"
      return make_Sexpr_from_list([flipop]+args)
    elif oper.atom=="not": return push_negs_inward(subexpr.list[1])
    else: raise Exception("error: don't know how to push negation inward over the following operator: %s" % oper.atom)
  else: return make_Sexpr_from_list([push_negs_inward(x) for x in expr.list]) 

def is_literal(expr): return expr.atom!=None or expr.list[0].atom=="not"

def is_conjunction(expr): return expr.atom==None and expr.list[0].atom=="and"

def is_disjunction(expr): return expr.atom==None and expr.list[0].atom=="or"


def distribute(expr):
  if is_literal(expr): return expr
  oper = expr.list[0].atom

  if not (is_conjunction(expr) or is_disjunction(expr)):
    raise Exception("error: unexpected operator %s in distribute()" % oper)
  args = [distribute(x) for x in expr.list[1:]]

  if oper=="and":
    absorbed = []
    for arg in args:
 
      if is_conjunction(arg): absorbed += arg.list[1:]
      else: absorbed.append(arg)
    return make_Sexpr_from_list(["and"]+absorbed)

  elif oper=="or":
    if len(args)==1: return args[0]
    absorbed = []
    for i in range(len(args)):
      arg = args[i]
      if is_conjunction(arg):
        terms = arg.list[1:]
        others = args[:i]+args[i+1:]
        newargs = []
        for other in others: 
          for term in terms:
            disjoined = make_Sexpr_from_list(["or",term]+others)
            newargs.append(disjoined)
        return distribute(make_Sexpr_from_list(["and"]+newargs))
      if is_disjunction(arg): absorbed += arg.list[1:]
      else: absorbed.append(arg)
    return make_Sexpr_from_list(["or"]+absorbed)

def validate_PropLog(expr):
  if expr.atom!=None: return True
  if len(expr.list)==0: return False
  oper = expr.list[0]
  if oper.atom==None: return False
  oper = oper.atom
  if oper not in ["<->","->","implies","and","or","not","xor"]: return False 
  args = expr.list[1:]
  for arg in args:
    if validate_PropLog(arg)==False: return False
  if (oper=="<->" or oper=="->" or oper=="xor") and len(args)!=2: return False
  if oper=="not" and len(args)!=1: return False
  return True

DIMACS = False

if __name__=="__main__":
 if len(sys.argv)<2: sys.stderr.write("usage: python convCNF.py <propositional_kb> [-DIMACS]\n"); sys.exit(0)
 if "-DIMACS" in sys.argv: DIMACS = True

 for line in open(sys.argv[1]):
  line = line.rstrip()
  print("# "+line)
  if line.startswith('#') or len(line)==0: continue
  if '#' in line: line = line[:line.index('#')]
  toks = tokenize(line)
  expr = Sexpr(toks,0)

  cnf = convCNF(expr)

  if is_conjunction(cnf): clauses = cnf.list[1:]
  else: clauses = [cnf]
  clauses = [or_wrapper(c) for c in clauses]

  print("")
  if DIMACS:
    for clause in clauses: print(clause.toDIMACS())
  else:
    for clause in clauses: print(clause.toString())
  print("")

