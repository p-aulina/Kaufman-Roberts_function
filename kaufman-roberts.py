a_min = 0.2
a_max = 1.3
a_step = 0.1
C = 4
t = [1, 2]
m = len(t)

a = []
ai = []

def calculate_a():
    x = a_min
    while(x <= a_max):
        x = round(x, 1)
        a.append(x)
        x += a_step
    # print(step_counter)

    for i in range(m):
        x = C/(m*t[i])
        for j in range(len(a)):
            ai.append(x*a[j])

s = []
p = []

# def calculate_p():
#     s.append(1)
#     x = 0
#     for i in range(m):
#         for n in range(len(ai)):
#             if (n - t[i] >= 0):
#                 x +=



def print_a():
    for j in range(len(a)):
        print(a[j])
def print_ai():
    x = len(ai)//m
    for i in range(x):
        print(ai[i], ai[x + i])



calculate_a()
print_ai()