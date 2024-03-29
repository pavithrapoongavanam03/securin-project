from flask import Flask, render_template
from itertools import product

app = Flask(__name__)

#total combination
def totalcomb():
    return 6 * 6

#combination matrix
def combmat():
    matrix = [[(i, j) for j in range(1, 7)] for i in range(1, 7)]
    return matrix

#calculation frequency of combinations
def cal(combm):
    f = {i: 0 for i in range(2, 13)}
    for r in combm:
        for c in r:
            f[sum(c)] += 1
    return f

#Finding the probabilities
def prob(f, total):
    p = {k: v / total for k, v in f.items()}
    return p
#part b
#probabilities of different sums
def findprobs(da, db):
    res = {}
    for ra, rb in product(da, db):
        s= ra + rb
        res[s] = res.get(s, 0) + 1
    return res
#check if a combination of spots for dice A and B preserves the original probabilities
def check(pa, pb, mapprob):
    genprob = findprobs(pa, pb)
    return mapprob == genprob
#generate all possible combinations of spots for dice B
def combb(arr, sides):
    res= []
    n = len(arr)
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                temp.append(arr[j])
        if len(temp) == sides:
            res.append(temp)
    return res
#generate all possible combinations of spots for dice A
def comba(arr, sides):
    res= []
    n = len(arr)
    for i in range(int(n ** sides)):
        temp = []
        t = i
        for j in range(sides):
            ind = t % n
            temp.append(arr[ind])
            t //= n
        res.append(temp)
    return res

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/parta')
def parta():
    total= totalcomb()
    combmatrix = combmat()
    f = cal(combmatrix)
    probability= prob(f, total)
    return render_template('about.html', total_combinations=total, combinations_matrix=combmatrix, frequency=f, probability=probability)

@app.route('/partb')
def partb():
    # Define the spots configurations for the initial dice A and dice B
    num1 = [1, 2, 3, 4]
    num2 = [1, 2, 3, 4, 5, 6, 7, 8]
    #sides of dice
    sides = 6
     # Define the original configurations for dice A and B
    dice_a = [1, 2, 3, 4, 5, 6]
    dice_b = [1, 2, 3, 4, 5, 6]
    #possibles of dice a and dice b
    possibles_a = comba(num1, sides)
    possibles_b = combb(num2, sides)
    #calculating different sums for orginal dice configuration
    map_probabilities = findprobs(dice_a, dice_b)

    found = False
    #iterate through all possible combinations
    for p1 in possibles_a:
        for p2 in possibles_b:
            #check the combination and preserve original probabilities
            if check(p1, p2, map_probabilities):
                transformeddicea = p1
                transformeddiceb = p2
                found = True
                break
        if found:
            break
    #return transformed dice a and b
    return render_template('converter.html', transformedA=transformeddicea, 
    transformedB=transformeddiceb)

if __name__ == '__main__':
    app.run(debug=True)