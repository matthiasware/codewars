# carpark = [[1, 0, 0, 0, 2],
#            [0, 0, 0, 0, 0]]
# result = ["L4", "D1", "R4"]

# carpark = [[2, 0, 0, 1, 0],
#            [0, 0, 0, 1, 0],
#            [0, 0, 0, 0, 0]]
# result = ["R3", "D2", "R1"]

# carpark = [[0, 2, 0, 0, 1],
#            [0, 0, 0, 0, 1],
#            [0, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]]
# result = ["R3", "D3"]

carpark = [[0, 0, 0],
           [0, 0, 0],
           [2, 0, 0]]
result = ["R2"]

carpark = [[0, 0, 0, 0, 2]]
result = []

while 2 not in carpark[0]:
    carpark.pop(0)
position = carpark[0].index(2)
carpark[-1][-1] = 1
path = []
for i in range(len(carpark)):
    goal = carpark[i].index(1)
    distance = position - goal
    position = goal
    path.append(distance)
down = 1
final = []
for i in path:
    if i < 0:
        final.append("D" + str(down))
        down = 1
        final.append("R" + str(- i))
    elif i == 0:
        down += 1
    else:
        final.append("D" + str(down))
        down = 1
        final.append("L" + str(i))
if down != 1:
    final.append("D" + str(down -1))

print(result == final[1:])