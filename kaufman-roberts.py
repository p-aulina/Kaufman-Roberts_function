# ******************************************************************
#                        [ FILE MANAGEMENT ]
# ******************************************************************
from pathlib import Path

file_p = Path("occupancy.txt")
file_e = Path("blocking.txt")
file_y = Path("requests.txt")

def file_exist(file):
    if not file.exists():
        file.touch()

# ******************************************************************
#                        [ INPUT PARAMETERS ]
#
#  a_min - minimum traffic offered per one unit of system capacity
#  a_max - maximum traffic offered per one unit of system capacity
#  a_step - calculation step
#  C - system capacity
#  t - stream requests
#  m - class number
# ******************************************************************
a_min = 0.2
a_max = 1.3
a_step = 0.1
C = 10
t = [1, 2, 3]
m = len(t)


# ******************************************************************
#                       [ TRAFFIC INTENSITY ]
# ******************************************************************
ai = []
def calculate_a():
    a = a_min*C/m
    for i in range(0, m, 1):
        ai.append(a/t[i])


# ******************************************************************
#              [ OCCUPANCY PROBABILITY DISTRIBUTION ]
# ******************************************************************
s = []
p = []
def calculate_p():
    s.append(1)
    for n in range(1, C + 1, 1):
        x = 0
        for i in range(0, m, 1):
            if (n - t[i] >= 0):
                x += t[i]*ai[i]*s[n - t[i]]
        s.append(x/n)
    sum = 0
    for n in range(0, C + 1, 1):
        sum += s[n]
    for n in range(0, C + 1, 1):
        p.append(s[n]/sum)


# ******************************************************************
#                      [ BLOCKING PROBABILITY ]
# ******************************************************************
ei = []
def calculate_e():
    for i in range(m):
        x = 0
        for n in range(C - t[i] + 1, C + 1, 1):
            x += p[n]
        ei.append(x)

y = []
def calculate_y():
    for n in range(0, C + 1):
        for i in range(m):
            if 0 <= n - t[i] <= C:
                y.append(ai[i]*t[i]*p[n - t[i]]/p[n])
            else:
                y.append(0)

# ******************************************************************
#                        [ HELPER FUNCTIONS ]
# ******************************************************************
def calculate_all():
    calculate_a()
    calculate_p()
    calculate_y()
    calculate_e()

def clear_all():
    ai.clear()
    s.clear()
    p.clear()
    y.clear()
    ei.clear()

col_t_width = 12
col_a_width = 8

def header(file_h):
    with file_h.open(mode = "w") as file:
        file.write(f"# C = {C}\n")
        file.write("#\n")
        for i in range(m):
            file.write(f"#\tt[{i + 1}] = {t[i]}\n")
        file.write("#\n")
        if file_h == file_e:
            file.write(f"{'a':<{col_a_width}}")
            for i in range(m):
                file.write(f"t{i + 1:<{col_t_width}}")
            file.write("\n")

def write_blocking():
    with file_e.open(mode = "a") as file:
        file.write(f"{a_min:<{col_a_width}}")
        for i in range(m):
            file.write(f"{round(ei[i], 9):<{col_t_width + 1}}")
        file.write("\n")

def write_occupancy():
    with file_p.open(mode = "a") as file:
        file.write(f"\na = {a_min}\n")
        file.write(f"{'n':<{col_a_width}}p[n]\n")
        for i in range(C + 1):
            file.write(f"{i:<{col_a_width}}{p[i]}\n")

def write_requests():    
    with file_y.open(mode = "a") as file:
        file.write(f"\n{a_min}\n")
        file.write(f"{'n':<{col_a_width}}")
        for i in range(m):
            file.write(f"t{i+1:<{col_t_width}}")
        file.write(f"{':':<{col_a_width}}sum\n")

        for n in range(0, C + 1):
            file.write(f"{n:<{col_a_width}}")
            for i in range(m):
                file.write(f"{round(y[n*m + i], 7):<{col_t_width + 1}}")
            file.write(f"{':':<{col_a_width}}{n}\n")
        


# ******************************************************************
#                              [ MAIN ]
# ******************************************************************
file_exist(file_p)
file_exist(file_e)
file_exist(file_y)
header(file_e)
header(file_p)
header(file_y)
while(a_min <= a_max):
    calculate_all()
    write_blocking()
    write_occupancy()
    write_requests()
    clear_all()
    a_min += a_step
    a_min = round(a_min, 1)