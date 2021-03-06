'''
Problem Introduction
    A thief finds much more loot than his bag can fit. Help him to find the most valuable combination
    of items assuming that any fraction of a loot item can be put into his bag.

Problem Description
    Task.           The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
    Input Format.   The first line of the input contains the number n of items and the capacity W of a knapsack.
                    The next n lines define the values and weights of the items. The i-th line contains integers v i and w i —the
                    value and the weight of i-th item, respectively.
                    Constraints. 1 ≤ n ≤ 10 3 , 0 ≤ W ≤ 2 · 10 6 ; 0 ≤ v i ≤ 2 · 10 6 , 0 < w i ≤ 2 · 10 6 for all 1 ≤ i ≤ n. All the
                    numbers are integers.
    Output Format.  Output the maximal value of fractions of items that fit into the knapsack.
'''
# using python3
# Approach-I: running time complexity: O(n^2)
'''
def BestItem(weights, values):
    # a --> weight array, b --> value array
    maxValuePerWeight = 0
    bestItem = 0
    n = len(weights)
    for i in range(0, n):
        if weights[i] > 0:
            if (values[i]/weights[i]) > maxValuePerWeight:
                maxValuePerWeight = (values[i]/weights[i])
                bestItem = i
    return i

def knapsack(W, weights, values):
    totalValue = 0
    n = len(weights)
    for i in range(0, n):
        if W == 0:
            return totalValue
        i = BestItem(weights, values)
        a = min(weights[i], W)
        print(totalValue, a, i)
        totalValue += a*(values[i]/weights[i])
        weights[i] -= a
        W -= a
    return totalValue
'''

# Approach-II: running time complexity: O(nlogn)
'''
First sort the items with decreaing value per unit weight
then choose which item to put into knapsack
'''

# Accepted solution (w/o any test case failure)

def fractional_knapsack(value, weight, capacity):
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value

# Had a failed test case on submission - couldn't find out why?!
'''
def knapsackFast(W, weights, values):
    # variable initialize
    totalValue = 0
    n = len(weights)
    # Sorting
    valuePerUnitWeight = [(y,x,y/x) for x,y in zip(weights,values)]
    # print(valuePerUnitWeight)
    valuePerUnitWeight.sort(key= lambda tup: tup[2],reverse=True)
    # print(valuePerUnitWeight)
    # Rearrangement
    values = [x for tup in valuePerUnitWeight for x in values if tup[0]==x]
    weights = [y for tup in valuePerUnitWeight for y in weights if tup[1]==y]
    # iterate and select item from sorted list until knapsack is full
    for i in range(0, n):
        if W == 0:
            return totalValue
        else:
            a = min(weights[i], W)
            totalValue += a*(float(valuePerUnitWeight[i]))
            weights[i] -= a
            W -= a
    return totalValue
'''

if __name__ == '__main__':
    (n, W) =  map(int, input().split())
    w = []
    v = []
    while n>0:
        x = input()
        v.append(int(x.split()[0])) # weight
        w.append(int(x.split()[1])) # value
        n -= 1
    # print(knapsack(W, w, v))
    # print(knapsackFast(W,w,v))
    print(fractional_knapsack(v, w, W))