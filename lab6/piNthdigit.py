import time
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt

def chudnovsky(num_digits):
    getcontext().prec = num_digits + 2
    C = 426880 * Decimal(10005).sqrt()
    factorial_memo = [1]
    power_memo = [1]

    for i in range(1, 6 * num_digits + 1):
        factorial_memo.append(factorial_memo[-1] * i)

    for i in range(1, num_digits + 1):
        power_memo.append(power_memo[-1] * -262537412640768000)

    total_sum = Decimal(0)

    for k in range(num_digits):
        M = factorial_memo[6 * k] * ((545140134 * k) + 13591409)
        X = factorial_memo[3 * k] * (factorial_memo[k] ** 3) * power_memo[k]
        total_sum += Decimal(M) / X

    if total_sum == 0:
        return Decimal(0)

    pi = C / total_sum
    return pi

def gauss_legendre(num_digits):
    getcontext().prec = num_digits + 2
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(0.25)
    p = Decimal(1)
    for i in range(num_digits):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) * (a - a_next)
        a = a_next
        p *= 2
    return (a + b) * (a + b) / (4 * t)

def bailey_borwein_plouffe(num_digits):
    getcontext().prec = num_digits + 2
    pi = Decimal(0)
    for k in range(num_digits):
        pi += (Decimal(1) / 16**k) * (
            (Decimal(4) / (8*k + 1)) -
            (Decimal(2) / (8*k + 4)) -
            (Decimal(1) / (8*k + 5)) -
            (Decimal(1) / (8*k + 6))
        )
    return pi

def bellard(num_digits):
    getcontext().prec = num_digits + 2
    pi = Decimal(0)
    for k in range(num_digits):
        pi += (Decimal(-1) ** k / (1024 ** k)) * (
            Decimal(256) / (10 * k + 1) +
            Decimal(1) / (10 * k + 9) -
            Decimal(64) / (10 * k + 3) -
            Decimal(32) / (4 * k + 1) -
            Decimal(4) / (10 * k + 5) -
            Decimal(4) / (10 * k + 7) -
            Decimal(1) / (4 * k + 3)
        )
    pi /= 2 ** 6
    return pi


x_values = range(0, 301, 20)

chudnovsky_time = []
gauss_legendre_time = []
bailey_borwein_plouffe_time = []
bellard_time = []

algorithms = [chudnovsky, gauss_legendre, bailey_borwein_plouffe, bellard]
algorithm_labels = ['Chudnovsky', 'Gauss-Legendre', 'Bailey-Borwein-Plouffe', 'Bellard']
algorithm_colors = ['cyan', 'blue', 'black', 'green']

for algorithm, label, color in zip(algorithms, algorithm_labels, algorithm_colors):
    algorithm_time = []
    for x in x_values:
        start = time.time()
        _ = algorithm(x)
        end = time.time()
        algorithm_time.append(end - start)
    plt.plot(x_values, algorithm_time, color=color, label=label)
    if algorithm == algorithms[-1]:
        plt.title('Time Complexity')
        plt.ylabel('Execution Time, sec')
        plt.xlabel('n')
        plt.legend(loc='upper right')

plt.show()