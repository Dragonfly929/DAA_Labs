import math
import timeit
import matplotlib.pyplot as plt


def algorithm1(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        if c[i]:
            j = 2*i
            while j <= n:
                c[j] = False
                j = j+i
        i = i+1

    primes = []
    for k in range(2, n+1):
        if c[k]:
            primes.append(k)

    return primes


def algorithm2(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2

    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j = j+i
        i = i+1

    primes = []
    for k in range(2, n+1):
        if c[k]:
            primes.append(k)

    return primes


def algorithm3(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2

    while i <= n:
        if c[i]:
            j = i+1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j = j+1
        i = i+1

    primes = []
    for k in range(2, n+1):
        if c[k]:
            primes.append(k)

    return primes


def algorithm4(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2

    while i <= n:
        j = 1
        while j < i:
            if i%j == 0 and j != 1:
                c[i] = False
            j = j+1
        i = i+1

    primes = []
    for k in range(2, n+1):
        if c[k]:
            primes.append(k)

    return primes


def algorithm5(n):
    c = [True] * (n+1)
    c[1] = False
    i = 2

    while i <= n:
        j = 2
        while j <= math.sqrt(i):
            if i%j == 0:
                c[i] = False
            j = j+1
        i = i+1

    primes = []
    for k in range(2, n+1):
        if c[k]:
            primes.append(k)

    return primes

sieves = [
    {
        "tag": "Algorithm 1",
        "algo": lambda arr: algorithm1(arr),
        "color": "c"
    },
    {
        "tag": "Algorithm 2",
        "algo": lambda arr: algorithm2(arr),
        "color": "b"
    },
    {
        "tag": "Algorithm 3",
        "algo": lambda arr: algorithm3(arr),
        "color": "k"
    },
    {
        "tag": "Algorithm 4",
        "algo": lambda arr: algorithm4(arr),
        "color": "r"
    },
    {
        "tag": "Algorithm 5",
        "algo": lambda arr: algorithm5(arr),
        "color": "g"
    }
]
plt.title('Sieve of Eratosthenes')
plt.xlabel('n')
plt.ylabel('Time, sec')

for algo in sieves:
    x_values = []
    y_values = []
    for i in range(1, 50):
        start = timeit.default_timer()
        limit = 100*i
        algo["algo"](limit)
        end = timeit.default_timer()
        x_values.append(limit)
        y_values.append(end - start)

    plt.plot(x_values, y_values, label=algo["tag"], color=algo["color"])

plt.legend()
plt.show()

