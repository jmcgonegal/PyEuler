import sys
# read in the file matrix
f = open('matrix.txt','r')
matrix = []
for line in f:
  row = []
  for value in list(line.split(',')):
    row.append(int(value))
  matrix.append(row)
f.close()
# test matrix = 994
'''matrix = [[131,673,234,103,18],
[201,96,342,965,150],
[630,803,746,422,111],
[537,699,497,121,956],
[805,732,524,37,331]]'''
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right
delta_name = ['^', '<', 'v', '>'] # for policy grid.

# here comes dynamic programming!
def stochastic_value():
    value = [[sys.maxint for row in range(len(matrix[0]))] for col in range(len(matrix))]
    #policy = [[' ' for row in range(len(matrix[0]))] for col in range(len(matrix))]
    # loop until there is no value that changes (eg everything is optimized)
    change = True
    while change:
      change = False
      for x in range(len(matrix)):
        for y in range(len(matrix[0])):
          for d in range(len(delta)):
            # find goal on right
            if y == len(matrix)-1:
              # goal found
              if(value[x][y] == sys.maxint):
                value[x][y] = matrix[x][y]
                #policy[x][y] = '*'
                change = True
            else:
              # xy movements
              x1 = x+delta[d][0]
              y1 = y+delta[d][1]

              if x1 >= 0 and x1 < len(matrix) and y1 >= 0 and y1 < len(matrix[0]):
                cost = matrix[x][y] + value[x1][y1]
                if cost < value[x][y]:
                  # a lower value was found, keep looping
                  value[x][y] = cost
                  #policy[x][y] = delta_name[d]
                  change = True
    #for line in policy:
    #  print line
    return value
  
# calculate cost
res = stochastic_value()

# find the lowest cost in the left hand column
lowest_sum = res[0][0]
for row in res:
  if row[0] < lowest_sum:
    lowest_sum = row[0]
print lowest_sum
