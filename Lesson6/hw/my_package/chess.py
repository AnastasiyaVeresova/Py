# my_package/chess.py

def is_valid(board, row, col):
    """Проверяет, можно ли поставить ферзя на позицию (row, col)."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    """Решает задачу о n ферзях и возвращает все возможные решения."""
    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)

    board = [-1] * n
    solutions = []
    solve(0)
    return solutions

def find_successful_positions(n, num_successes=4):
    """Находит заданное количество успешных расстановок ферзей."""
    solutions = solve_n_queens(n)
    return solutions[:num_successes]

def print_board(positions):
    """Печатает шахматную доску с ферзями."""
    n = len(positions)
    board = [['- ' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(positions):
        board[row][col] = '+ '

    for row in board:
        print(' '.join(row))
    print()

# Основной скрипт
if __name__ == "__main__":
    n = 8  # Размер доски
    successful_positions = find_successful_positions(n, num_successes=4)

    for i, positions in enumerate(successful_positions, 1):
        # Преобразуем координаты из 0-индексации в 1-индексацию
        positions_1_based = [(row + 1, col + 1) for row, col in enumerate(positions)]
        print(f"Удачное расположение {i}:\n {positions_1_based}\n")
        print_board(positions)
