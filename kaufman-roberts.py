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

    for j in range(len(a)):
        for i in range(m):
            x = C/(m*t[i])
        
            ai.append(x*a[j])

s = []
p = []
x = 0

def calculate_p():
    for i in range(0, len(ai), m):
        s.append(1)
        l = len(s) - 1
        for n in range(1, C + 1):
            x = 0
            for j in range(m):
                if(n - t[j] >= 0):
                    x += ai[i + j]*t[j]*s[n - t[j] + l]
            s.append(x/n)

    for i in range(0, len(s), C + 1):
        sum = 0
        for j in range(C + 1):
            sum += s[i + j]
        for j in range(C + 1):
            p.append(s[j]/sum)




    # for i in range(len(s)):
    #     print(s[i])




def print_a():
    for j in range(len(a)):
        print(a[j])
def print_ai():
    x = len(ai)//m
    for i in range(x):
        print(ai[i], ai[x + i])

def print_ai2():
    for i in range(0, len(ai)//2, 2):
        print(ai[i], ai[i+1])
def print_s():
    for i in range(len(s)):
        if (i%5 == 0):
            print("i", i//5)
        print(s[i])



calculate_a()
print_ai2()
calculate_p()
