def convert(grams):
    ounces = 28.3495231 * grams
    print("Your ounces are:",ounces)

def tempC(fahren):
    centigrade = (5 / 9) * (fahren - 32)
    print("Your Centigrade temperature is:", centigrade)
    
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            print(f'Chickens:{chickens}, Rabbits:{rabbits}')  

def permut(line, empty = ""):
    if len(line) == 0:
        print(empty)
    else:
        for i in range(len(line)):
            gera = line[:i] + line[i+1:]
            permut(gera, empty + line[i])              


