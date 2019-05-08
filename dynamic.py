def find_sum(m):
    right_bound = len(m[0]) - 1
    down_bound = len(m) - 1
    
    explored_nodes = {}
    
    def mov(row, column):
        value = m[row][column]
        right_max_value = 0
        down_max_value = 0
        if row == down_bound and column == right_bound: 
            explored_nodes[(row, column)] = m[row][column]
            return value

        right_node = (row, column + 1)

        if right_node in explored_nodes:
            right_max_value = value + explored_nodes[right_node] 
        
        elif column < right_bound:
            right_max_value = value + mov(row, column + 1)

        down_node = (row + 1, column)
        
        if down_node in explored_nodes:
            down_max_value = value + explored_nodes[down_node]
        
        elif row < down_bound:
            down_max_value = value + mov(row + 1, column)

        max_value = right_max_value if right_max_value > down_max_value else down_max_value

        explored_nodes[(row, column)] = max_value

        return max_value

    return mov(0, 0)

if __name__ == "__main__":
    # answer: 4416
    # m = [
    #     [131, 673, 234, 103, 18],
    #     [201, 96, 342, 965, 150],
    #     [630, 803, 746, 422, 111],
    #     [537, 699, 497, 121, 956],
    #     [805, 732, 524, 37, 331]
    # ]

    # answer: 140
    # m = [
    #     [20, 20, 10, 10],
    #     [10, 20, 10, 10],
    #     [10, 20, 20, 20],
    #     [10, 10, 10, 20]
    # ]

    # print(find_sum(m))

    # answer: 1185980 (not really sure if this is correct)
    with open('project_euler_p081_matrix.txt') as textFile:
        data = [[int(n) for n in line.split(',')] for line in textFile]

    print(find_sum(data))
