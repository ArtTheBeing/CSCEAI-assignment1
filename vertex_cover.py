import DPLL as dpll_mod
from DPLL import Clause, DPLL, extract_props, sat_props

NODES = list('ABCDEFGHIJKL')

EDGES = [
    ('A','B'),('A','H'),
    ('B','I'),
    ('C','D'), ('C','K'),
    ('D', 'E'), ('D','K'),
    ('E','F'), ('E','L'),
    ('F','G'), ('F','L'),
    ('G', 'H'),
    ('H','J'),
    ('I','J'), ('I','K'),
    ('J','K'), ('J','L'),
]

def vc_var(node):
    return f"VC_{node}"

def subsets(nodes, size):
    if size == 0:
        return [[]]
    r = []
    for i in range(len(nodes)):
        for j in subsets(nodes[i+1:], size-1):
            r.append([nodes[i]] + j)
    return r

def generate_cnf(nodes, edges, k):
    lines = []

    for u, w in edges:
        lines.append(f"{vc_var(u)} {vc_var(w)}")

    for s in subsets(nodes, k + 1):
        lines.append(' '.join(f"-{vc_var(n)}" for n in s))

    return lines

def solve_vc(k):
    dpll_mod.calls = 0
    lines = generate_cnf(NODES, EDGES, k)
    clauses = [Clause(line) for line in lines]
    props = extract_props(clauses)
    model = {p: 0 for p in props}
    return DPLL(model, clauses, props), dpll_mod.calls

if __name__ == '__main__':
    dpll_mod.DEBUG = False

    print(f"Nodes({len(NODES)}):{NODES}")
    print(f"Edges({len(EDGES)}):{EDGES}")
    print()

    for k in [7, 6]:
        lines_count = len(generate_cnf(NODES, EDGES, k))
        print(f"cover size<={k}({lines_count}clauses):")
        result, calls = solve_vc(k)
        if result is None:
            print(f"not found(DPLL calls: {calls})")
        else:
            cover = [n for n in NODES if result.get(vc_var(n), 0) == 1]
            outside = [n for n in NODES if result.get(vc_var(n), 0) != 1]
            for u, w in EDGES:
                ok = result.get(vc_var(u), 0) == 1 or result.get(vc_var(w), 0) == 1
            print(f"found cover = {cover}(size {len(cover)})")
            print(f"Nodes not in cover: {outside}")
            print(f"verified: {'PASS' if ok else 'FAIL'}")
            print(f"DPLL calls: {calls}")
        print()
