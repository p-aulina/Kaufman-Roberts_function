# ******************************************************************
#                        [ FILE MANAGEMENT ]
# ******************************************************************
from pathlib import Path

file_p = Path("occupancy.txt")
file_e = Path("blocking.txt")

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
C = 4
t = [1, 2]
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


# ******************************************************************
#                        [ HELPER FUNCTIONS ]
# ******************************************************************
def calculate_all():
    calculate_a()
    calculate_p()
    calculate_e()

def clear_all():
    ai.clear()
    s.clear()
    p.clear()
    ei.clear()

def header():
    print("#", "C =", C)
    print("#")
    for i in range(m):
        print("# \t", "t[%i] =" % (i + 1), t[i])
    print("#")
    print("# \t", end="")
    for i in range(m - 1):
        print("t%i" % (i + 1), "\t \t \t", end="")
    
    print("t%i" % m)

def print_all():
    print(a_min, end="\t")
    for i in range(m):
        print(ei[i], end = "\t")
    print("")


# ******************************************************************
#                              [ MAIN ]
# ******************************************************************
file_exist(file_p)
file_exist(file_e)
header()
while(a_min <= a_max):
    calculate_all()
    print_all()
    clear_all()
    a_min += a_step
    a_min = round(a_min, 1)