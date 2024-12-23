from my_package.chess import find_successful_positions, print_board

n = 8  # Размер доски
successful_positions = find_successful_positions(n, num_successes=4)

for i, positions in enumerate(successful_positions, 1):
    # Преобразуем координаты из 0-индексации в 1-индексацию
    positions_1_based = [(row + 1, col + 1) for row, col in enumerate(positions)]
    print(f"Удачное расположение {i}: {positions_1_based}")
    print(f"Успешная расстановка {i}:")
    print_board(positions)