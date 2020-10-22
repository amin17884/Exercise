import pulp as p

model = p.LpProblem("Exercise1", p.LpMaximize)

x1 = p.LpVariable(name="x1", lowBound=0)
x2 = p.LpVariable(name="x2", lowBound=0)
x3 = p.LpVariable(name="x3", lowBound=0)
x4 = p.LpVariable(name="x4", lowBound=0)
x5 = p.LpVariable(name="x5", lowBound=0)

model += 250 * x1 + 300 * x2 + 500 * x3 + 450 * x4 + 180 * x5

model += 10 * x1 + 15 * x2 + 7 * x3 + 18 * x4 <= 77
model += 9 * x1 + 13 * x2 + 20 * x5 <= 80
model += x1 + x2 + x3 + x4 + x5 <= 40
print()

status = model.solve()
print(p.LpStatus[status])
print("obj:", p.value(model.objective))
print("x1=", p.value(x1))
print("x2=", p.value(x2))
print("x3=", p.value(x3))
print("x4=", p.value(x4))
print("x5=", p.value(x5))
