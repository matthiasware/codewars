import numpy as np

board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]

board = np.array(board)
p = set(np.array(range(1,10)))
# check rows
#r = np.all([np.equal(p, np.unique(row)) for row in board])
# check columns
#c = np.all([np.equal(p, np.unique(col)) for col in board.T])
# check submatrices
# s = np.all([p == np.unique(si) for si in sm])

sm = np.split(np.concatenate(np.split(board, 3, axis=1)), 9, axis=0)
rcu = [np.unique(i) for rc in [board, board.T] for i in rc]

uniques = [np.unique(i) for j in [sm, board, board.T] for i in j]
np.all([set(i) == p for i in uniques])