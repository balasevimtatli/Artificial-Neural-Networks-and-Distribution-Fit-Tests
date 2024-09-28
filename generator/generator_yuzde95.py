import random
import numpy as np
import xlwt
from scipy.stats import poisson
def Grouping(List):
    group = []
    groupFreuencies = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    mx = max(List)
    mn = min(List)
    step = 0.1 * (mx - mn)
    alt = mn
    for i in range(1, 11):
        ust = alt + step
        group.append([alt, ust])
        alt = ust
    for i in List:
        for j in range(10):
            if i >= group[j][0] and i < group[j][1]:
                groupFreuencies[j] += 1
                break

    groupFreuenciesL = list(groupFreuencies.values())
    mx = max(groupFreuenciesL)
    for i in range(10):
        if mx==0:
            mx=1
        groupFreuencies[i] = groupFreuencies[i] / mx

    return groupFreuencies
def Uniform(size, Param):
    valList = []
    a = Param[0]
    b = Param[1]
    for i in range(size):
        rval=random.uniform(a,b)
        valList.append(rval)
    return valList, Grouping(valList), "Uniform", [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

def Ustel (size, Param):
    valList = []
    lambd = Param[0]
    for i in range(size):
        rval=random.expovariate(1/lambd)
        valList.append(rval)

    return valList, Grouping(valList), "Ustel", [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def Beta(size, Param):
    valList = []
    alpha = Param[0]
    beta = Param[1]
    for i in range(size):
        rval=random.betavariate(alpha, beta)
        valList.append(rval)

    return valList, Grouping(valList), "Beta", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]


def Normal(size, Param):
    valList = []
    mu = Param[0]
    sigma = Param[1]

    for i in range(size):
        rval = random.normalvariate(mu, sigma)
        valList.append(rval)

    return valList, Grouping(valList), "Normal", [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def Weibull(size, Param):
    valList = []
    k = Param[0]
    lam = Param[1]

    for i in range(size):
        rval = random.weibullvariate(k, lam)
        valList.append(rval)

    return valList, Grouping(valList), "Weibull", [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def Lognormal(size, Param):
    valList = []
    mu = Param[0]
    sigma = Param[1]

    for i in range(size):
        rval = random.lognormvariate(mu, sigma)
        valList.append(rval)

    return valList, Grouping(valList), "Lognormal", [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def Geometric(size, Param):
    valList = []
    prob = Param[0]

    for i in range(size):
        rval = np.random.geometric(prob)
        valList.append(rval)

    return valList, Grouping(valList), "Geometric", [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def Poisson(size, Param):
    valList = []
    lambd = Param[0]

    for i in range(size):
        rval = poisson.rvs(lambd)
        valList.append(rval)

    return valList, Grouping(valList), "Poisson", [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


wb = xlwt.Workbook()
ws = wb.add_sheet('Test Sayfası')
style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',
                    num_format_str='#,##0.00')

style1 = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on',
                    num_format_str='#,##0.00')

dists = {0: Uniform, 1: Ustel, 2: Beta, 3: Normal, 4: Weibull, 5: Lognormal, 6: Geometric, 7: Poisson}
styles = [style0, style1]
s = 0
f = open("dataSet.txt", "w")

for dt in range(8):
    for i in range(2000):
        size = random.randint(100, 300)
        if dt == 0: #Uniform
            a = random.randint(1, 100)
            b = random.randint(100, 1000)
            param = [a, b]
        elif dt == 1:  # Ustel
            lambd = random.uniform(0.1, 2)
            param = [lambd]
        elif dt == 2:  # Beta
            alpha = random.uniform(0.5, 5)
            beta = random.uniform(0.5, 5)
            param = [alpha, beta]
        elif dt == 3:  # Normal
            mu = random.uniform(0, 100)
            sigma = random.uniform(0.1, 10)
            param = [mu, sigma]
        elif dt == 4:  # Weibull
            k =random.uniform(0.5, 5)
            lam = random.uniform(0.1, 2)
            param = [k, lam]
        elif dt == 5:  # Lognormal
            mu = random.uniform(0, 100)
            sigma = random.uniform(0.1, 10)
            param = [mu, sigma]
        elif dt == 6:  # Geometric
            prob = random.uniform(0.1, 0.99)
            param = [prob]
        elif dt == 7:  # Poisson
            lambd = random.uniform(0.1, 2)
            param = [lambd]

        print(" Set:", i, "Size:", size)
        values, res, name, frmt = dists[dt](size, param)
        for j in range(10):
            ws.write(s, j, res[j])

        ws.write(s, j + 1, name)

        for i in range(len(param)):
            ws.write(s, j+2+i, param[i])

        for i in range(len(frmt)):
            ws.write(s, j + 4 + i, frmt[i])



        s += 1

        parameter_info = str(param)[1:-1].replace(",", ";")
        for i in values:
            f.write(f"{i}:{size}:{parameter_info}:{name}\n")

f.close()
wb.save(path+'95_example_last_update_control_959.xls')
