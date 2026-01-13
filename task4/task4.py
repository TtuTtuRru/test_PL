import sys

def read_nums(file_path):

    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip()]

def min_moves(nums):

    nums_sorted = sorted(nums)
    median = nums_sorted[len(nums_sorted) // 2]
    moves = sum(abs(num - median) for num in nums_sorted)
    return moves

def main():

    file_path = sys.argv[1]
    nums = read_nums(file_path)

    moves = min_moves(nums)

    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()