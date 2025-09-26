'''
0/1 Knapsack:
------------
m=8 P={1,2,5,6}
n=4 W={2,3,4,5}

- For every object we have a profit and weight. We need to put these
objects in our knapsack such that we get the highest amount of profit
for what the bag can hold in total weight. We want to maximize profit
so this is an optimization problem.

x={0,1,1,0} <- this is how we denot what is included in the bag and
what is not included. In greedy we are taking fractions of the object.
here we either take the object or we don't.
'''

'''
Sets method:
------------
m=8 P={1,2,5,6}
n=4 W={2,3,4,5}
    x={0,1,1,0}
'''