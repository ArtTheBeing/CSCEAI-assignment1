import DPLL as dpll_mod
from DPLL import Clause, DPLL, extract_props, sat_props

def var(i, j):
    return f"Q_{i}_{j}"

def generate_cnf(n=8):
    lines = []

    for i in range(1, n+1):
        lines.append(' '.join(var(i, j) for j in range(1,n+1)))

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(j+1, n+1):
                lines.append(f"-{var(i,j)} -{var(i,k)}")
            for k in range(i+1, n+1):
                lines.append(f"-{var(i,j)} -{var(k,j)}")

    for i in range(1, n+1):
        for j in range(1, n+1):
            for d in range(1, n):
                if i + d <= n and j + d <= n:
                    lines.append(f"-{var(i,j)} -{var(i+d,j+d)}")
                if i + d <= n and j - d >= 1:
                    lines.append(f"-{var(i,j)} -{var(i+d,j-d)}")
    return lines

def print_board(model, n=8):
    for i in range(1, n + 1):
        row = ['Q' if model.get(var(i, j), 0) == 1 else '.' for j in range(1, n + 1)]
        print(' '.join(row))


dpll_mod.DEBUG = False

n = 8
base_lines = generate_cnf(n)
print(f"8-Queens: {len(base_lines)} clauses, {n*n} variables")
print()
extra_c = []

for sol_num in range(1, 3):
    dpll_mod.calls = 0

    all_clauses = [Clause(line) for line in base_lines] + extra_c
    props = extract_props(all_clauses)
    model = {p: 0 for p in props}
    result = DPLL(model, all_clauses, props)
    if result is None:
        print("No more solutions found.")
        break
    queens = sorted(p for p in sat_props(result) if p.startswith('Q_'))

    print(f"Solution {sol_num}(DPLL calls: {dpll_mod.calls}):")
    print_board(result, n)
    print(f"Queens:{queens}")
    print()
    block = Clause(' '.join(f"-{q}" for q in queens))
    extra_c.append(block)
