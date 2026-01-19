import copy
from collections import deque


intial_matrix = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]


visited_list = [
    [False,False,False],
    [False,False,False],
    [False,False,False]
]

my_queue = deque()

my_queue.append(intial_matrix)
    
def swap(new_array,original_array):
    pass


def state_BFS(i,j):
    if not visited_list[i][j]:
        while(my_queue.size()!=0):
            newI=-1
            newJ=-1
            present_state = my_queue.pop()
            #move up
            if i >0:
                newI = i-1
                newJ=j
                visited_list[newI][newJ]=True

                new_array = copy.deepcopy(present_state)
                temp =new_array[i][j]
                new_array[i][j]=new_array[newI][newJ]
                new_array[newI][newJ]=temp
                print("current State : " , new_array)
                my_queue.append(new_array)
                if(new_array==present_state):
                    print("we have the solution")
                    return
            #move down
            if i<len(intial_matrix)-1:
                newI=i+1
                newJ =j
                visited_list[newI][newJ]=True
                new_array = copy.deepcopy(present_state)
                temp =new_array[i][j]
                new_array[i][j]=new_array[newI][newJ]
                new_array[newI][newJ]=temp
                print("current State : " , new_array)
                my_queue.append(new_array)
                if(new_array==present_state):
                    print("we have the solution")
                    return

            #move left
            if j >0:
                newI = i
                newJ=j-1

                visited_list[newI][newJ]=True
                new_array = copy.deepcopy(present_state)
                temp =new_array[i][j]
                new_array[i][j]=new_array[newI][newJ]
                new_array[newI][newJ]=temp
                print("current State : " , new_array)
                my_queue.append(new_array)
                if(new_array==present_state):
                    print("we have the solution")
                    return

            #move down
            if j<len(intial_matrix[0])-1:
                newI=i
                newJ =j+1

                visited_list[newI][newJ]=True
                new_array = copy.deepcopy(present_state)
                temp =new_array[i][j]
                new_array[i][j]=new_array[newI][newJ]
                new_array[newI][newJ]=temp
                print("current State : " , new_array)
                my_queue.append(new_array)
                if(new_array==present_state):
                    print("we have the solution")
                    return




for i in range(len(intial_matrix)):  # Loop through rows
    for j in range(len(goal_matrix[0])): # Loop through columns in the current row
        if(intial_matrix[i][j]==0):
            state_BFS(i,j)
            break