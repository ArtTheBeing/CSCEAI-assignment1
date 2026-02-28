import DPLL as dpll_mod
from DPLL import Clause, DPLL, extract_props, sat_props

NODES = list('ABCDEFGHI')

EDGES = [
    ('A','C'),
    ('B','C'),('B','D'), ('B','E'),('B','F'), ('B','H'),
    ('C','E'),('C','F'),('C','H'),
    ('D','E'), ('D','F'),
    ('E','F'), ('E','H'), ('E','I'),
    ('F','G'), ('F','H'), ('F','I'),
    ('G','I'),
    ('H','I'),
]

ESET = {(u,v) for u,v in EDGES} | {(v,u) for u,v in EDGES}


def connected(u, v):
    return (u,v) in ESET


def clique_v(node, pos):
    return f"C_{node}_{pos}"


def generate_cnf(nodes, k):
    lines = []

    for pos in range(1, k+1):
        lines.append(' '.join(clique_v(v, pos) for v in nodes))

    for pos in range(1,k+1):
        for i, u in enumerate(nodes):
            for w in nodes[i+1:]:
                lines.append(f"-{clique_v(u, pos)} -{clique_v(w, pos)}")

    for v in nodes:
        for i in range(1,k+1):
            for j in range(i+1, k+1):
                lines.append(f"-{clique_v(v, i)} -{clique_v(v, j)}")

    for i in range(1,k + 1):
        for j in range(i +1,k +1):
            for idx, u in enumerate(nodes):
                for w in nodes[idx + 1:]:
                    if not connected(u, w):
                        lines.append(f"-{clique_v(u, i)} -{clique_v(w, j)}")
                        lines.append(f"-{clique_v(w, i)} -{clique_v(u, j)}")
    return lines

def extract_clique(model, k):
    clique = set()
    for v in NODES:
        for pos in range(1,k+1):
            if model.get(clique_v(v, pos), 0) ==1:
                clique.add(v)
    return sorted(clique)


def solve_clique(k):
    dpll_mod.calls = 0
    lines = generate_cnf(NODES, k)
    clauses =[Clause(line) for line in lines]
    props = extract_props(clauses)
    model ={p: 0 for p in props}
    return DPLL(model, clauses, props), dpll_mod.calls


dpll_mod.DEBUG = False

print(f"Nodes ({len(NODES)}): {NODES}")
print(f"Edges ({len(EDGES)}): {EDGES}")
print()

for k in [3, 4, 5]:
    lines_count = len(generate_cnf(NODES, k))
    print(f"{k}-clique({lines_count} clauses, {len(NODES)*k} variables):")

    result,calls = solve_clique(k)

    if result is None:
        print(f"not found(DPLL calls:{calls})")
    else:
        clique = extract_clique(result, k)
        for a in range(len(clique)):
            for b in range(a+1,len(clique)):
                ok = connected(clique[a], clique[b])
                if(ok == False):
                    break
        print(f"found clique={clique}")
        print(f"verified:{'PASS' if ok else 'FAIL'}")
        print(f"DPLL calls:{calls}")
        print()
