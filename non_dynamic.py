def find_sum(m):
    last_row = len(m) - 1
    last_column = len(m[0]) - 1
    
    totals = []

    def mov(row, column, total):
        cur_value = m[row][column]
        if row == last_row and column == last_column:
            totals.append(total + cur_value)
            return m[last_row][last_column]
        if column < last_column:
            mov(row, column + 1, total + cur_value)

        if row < last_row:
            mov(row + 1, column, total + cur_value)

        return

    mov(0, 0, 0)

    return max(totals)

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
