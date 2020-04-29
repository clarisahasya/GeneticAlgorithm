import numpy as np 
import random

def chromosome():
    chr=[]
    for i in range(6):    
        chr.append(random.randint(0,9))
    return chr

def population():
    pop=[]
    for i in range(6):
        pop.append(chromosome())
    return pop

def split(chro):
    half = len(chro)//2
    return chro[:half], chro[half:]

def getX(chro, max, min): #-3 <= x <= 3  -2 <= x <= 2
    up = 0
    down = 0
    for i in range(len(chro)):
        g = (chro[i])
        up += (g*(10**-(i+1)))
        down += (9*(10**-(i+1)))
    x = min + (((max-min)*up)/down)
    return x

def getF(x1, x2): #f(x1,x2)
    f = ((4 - (2.1*(x1**2)) + ((x1**4)/3))*(x1**2)) + (x1*x2) + ((-4 + (4*(x2**2)))*(x2**2))
    return f

def getFitness(f):
    fit = 1 / (f + 0.5)
    return fit

def RouletteWheelSelection(pop,fit,total):
    r = random.random()
    i = 0
    # print("random",r)   
    while (r>0):
        r -= fit[i]/total
        i += 1
        if (i == (len(pop)-1)): #berhentiin loop kalo udah sampe batas populasi
            break
    parent = pop[i]
    return parent

# def TournamentSelection(pop):
#     best = []
#     id = []
#     n = len(pop)
#     for i in range (2*n):
#         id = random.choice(pop)
#         a, b = split(id)
#         x1 = getX(a, 3, -3)
#         x2 = getX(b, 2, -2)
#         if (best != []):
#             c, d = split(best)
#             y1 = getX(a, 3, -3)
#             y2 = getX(b, 2, -2)
#         if (best == []) or getFitness(getF(x1,x2)) > getFitness(getF(y1,y2)):
#             best = id
#     return best

def crossover(parent1,parent2):
    cross1, cross2 = [], []
    cross = []
    prob = random.random()
    if (prob < 0.9):
        point = random.randint(0,5)
        cross1[:point] = parent1[:point]
        cross1[point:] = parent2[point:]
        cross2[:point] = parent2[:point]
        cross2[point:] = parent1[point:]
        cross.append(cross1)
        cross.append(cross2)
    else:
        cross.append(parent1)
        cross.append(parent2)
    return cross

def mutation(cross1,cross2):
    prob = random.random()
    if (prob < 0.2):
        for i in range (len(cross1)):
            p = random.random()
            if (p < 0.1):
                cross1[i] = random.randint(0,9)
        for i in range (len(cross2)):
            p = random.random()
            if (p < 0.1):
                cross2[i] = random.randint(0,9)
    cross = []
    cross.append(cross1)
    cross.append(cross2)
    return cross

def theBest(pop):
    maxFit = -9999
    id = []
    for i in range(len(pop)):
        id = pop[i]
        a, b = split(id)
        x1 = getX(a, 3, -3)
        x2 = getX(b, 2, -2)
        f = getF(x1, x2)
        fit = getFitness(f)
        if (fit>maxFit):
            maxFit = fit
            maxId = id
    return maxId

#main program

#Roulette Wheel Selection
pop = population()
generation=1
while(generation<4):
    id = []
    fit = []
    list_fit = []
    newpop = []
    child = []
    best = theBest(pop)
    total = 0
    print("Population ",generation,"=",pop)
    for i in range(len(pop)):
        id = pop[i]
        print("Genotype",i,"=",id)
        a, b = split(id)
        x1 = getX(a, 3, -3)
        x2 = getX(b, 2, -2)
        print("Fenotype",i,"=",x1,x2)
        f = getF(x1, x2)
        print("Nilai Fungsi",i,"=",f)
        fit = getFitness(f)
        list_fit.append(getFitness(f)) #Tampung isi fitnes populasi di array
        total += fit
        print("Fitness",i,"=",fit) 
    print("Total Fitness = ",total)
    print("________________________________________________") 
    for j in range(len(pop)//2):
        parent1 = RouletteWheelSelection(pop,list_fit,total)
        parent2 = RouletteWheelSelection(pop,list_fit,total)
        print("Parent 1 =",parent1)
        print("Parent 2 =",parent2)
        child = crossover(parent1,parent2)
        child = mutation(child[0],child[1])
        print("Child =",child)
        newpop.append(child[0])
        newpop.append(child[1])
    print("")
    print("New Population",generation,"=",newpop)
    print("__________________________________________________________________________________________________________________________________________________________________")
    print("__________________________________________________________________________________________________________________________________________________________________")
    best = theBest(newpop)
    pop = newpop 
    generation+=1

print("Kromosom Terbaik")
print("Genotype = ",best)
a, b = split(best)
x1 = getX(a, 3, -3)
x2 = getX(b, 2, -2)
print("Fenotype = ",x1,x2)
print("Nilai Fungsi = ",getF(x1,x2))
print("Fitness = ",getFitness(getF(x1,x2)))

#Tournament Selection
# generation=1
# pop = population()
# while(generation<4):
#     newpop = []
#     for i in range(len(pop)//2):
#         parent1 = TournamentSelection(pop)
#         parent2 = TournamentSelection(pop)
#         child = crossover(parent1,parent2)
#         child = mutation(child[0],child[1])
#         print("parent 1",parent1)
#         print("parent 2",parent2)
#         print("child",child)
#         newpop.append(child[0])
#         newpop.append(child[1])
#     print("newpopulation ",newpop)
#     best = theBest(newpop)
#     pop = newpop
#     generation+=1