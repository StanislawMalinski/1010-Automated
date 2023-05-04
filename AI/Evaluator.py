from math import sqrt


def evaluate(position_org):
    s_y = len(position_org)
    s_x = len(position_org[0])
    block_sum = 0
    hole_dict = dict()
    island_dict = dict()
    last_hole_ID = 0
    last_island_ID = 1
    position = [row.copy() for row in position_org]

    block_offset = ((-1, 0), (-1, -1), (0, -1), (1, -1))
    hole_offset = ((-1, 0), (0, -1),)

    columns_changes = [0] * s_x
    rows_changes = [0] * s_y

    for y in range(s_y):
        for x in range(s_x):
            if y > 1 and position_org[y - 1][x] != position_org[y][x]:
                columns_changes[x] += 1

            if x > 1 and position_org[y][x - 1] != position_org[y][x]:
                rows_changes[y] += 1

            if position[y][x] == 0:
                found_neigh = False
                for offset in hole_offset:
                    n_x = offset[0] + x
                    n_y = offset[1] + y

                    if n_x >= s_x or n_x < 0 or n_y >= s_y or n_y < 0:
                        continue

                    if position[n_y][n_x] < 0:
                        if not found_neigh:
                            found_neigh = True
                            position[y][x] = hole_dict[position[n_y][n_x]]
                        else:
                            hole_dict[position[y][x]] = position[n_y][n_x]

                if not found_neigh:
                    last_hole_ID -= 1
                    position[y][x] = last_hole_ID
                    hole_dict[last_hole_ID] = last_hole_ID

            if position[y][x] == 1:
                block_sum += 1
                found_neigh = False
                for offset in block_offset:
                    n_x = offset[0] + x
                    n_y = offset[1] + y

                    if n_x >= s_x or n_x < 0 or n_y >= s_y or n_y < 0:
                        continue

                    if position[n_y][n_x] > 1:
                        if not found_neigh:
                            found_neigh = True
                            position[y][x] = island_dict[position[n_y][n_x]]
                        else:
                            island_dict[position[y][x]] = position[n_y][n_x]

                if not found_neigh:
                    last_island_ID += 1
                    position[y][x] = last_island_ID
                    island_dict[last_island_ID] = last_island_ID

    uq_hole_count = 0
    uq_island_count = 0

    for hole_id_key in hole_dict.keys():
        if hole_dict[hole_id_key] == hole_id_key:
            uq_hole_count += 1

    for island_id_key in island_dict.keys():
        if island_dict[island_id_key] == island_id_key:
            uq_island_count += 1

    average_dispersal_block_in_island = 0
    average_dispersal_block = 0
    average_dispersal_island = 0
    island = dict()

    avg_y = 0
    avg_x = 0

    for y in range(s_y):
        for x in range(s_x):
            if position[y][x] > 1:
                avg_x += x
                avg_y += y
                if island_dict[position[y][x]] in island.keys():
                    island[island_dict[position[y][x]]].append((x, y))
                else:
                    island[island_dict[position[y][x]]] = [(x, y)]

    if block_sum > 0:
        avg_x /= block_sum
        avg_y /= block_sum

    total_distance_for_island_to_center = 0
    total_distance_for_block_in_island = 0
    total_distance = 0

    for land in island.keys():
        avg_block_x_island = 0
        avg_block_y_island = 0
        n = len(island[land])

        for block in island[land]:
            avg_block_x_island += block[0]
            avg_block_y_island += block[1]

        avg_block_x_island /= n
        avg_block_y_island /= n

        total_distance_for_island_to_center += sqrt(
            (avg_block_y_island - avg_y) ** 2 + (avg_block_x_island - avg_x) ** 2)

        for block in island[land]:
            dist = sqrt((avg_x - block[0]) ** 2 + (avg_y - block[1]) ** 2)
            total_distance += dist
            total_distance_for_block_in_island += sqrt(
                (avg_block_x_island - block[0]) ** 2 + (avg_block_y_island - block[1]) ** 2) / n

    if block_sum > 0:
        average_dispersal_block_in_island = total_distance_for_block_in_island
        average_dispersal_block = total_distance / block_sum

    if uq_island_count > 0:
        average_dispersal_island = total_distance_for_island_to_center / uq_island_count

    clear_columns = 0
    clear_rows = 0
    variation_column = 0
    variation_row = 0

    max_clear_column = 0
    max_clear_row = 0

    streak_col = 0
    streak_row = 0

    for y in rows_changes:
        if y == 0:
            clear_rows += 1
            streak_row += 1
        else:
            if streak_row > max_clear_row:
                max_clear_row = streak_row
            streak_row = 0
        variation_row += y
    if streak_row > max_clear_row:
        max_clear_row = streak_row

    for x in columns_changes:
        if x == 0:
            clear_columns += 1
            streak_col += 1
        else:
            if streak_col > max_clear_column:
                max_clear_column = streak_col
            streak_col = 0
        variation_column += x
    if streak_col > max_clear_column:
        max_clear_column = streak_col

    return (uq_hole_count,
            block_sum,
            uq_island_count,
            average_dispersal_block_in_island,
            average_dispersal_island,
            average_dispersal_block,
            clear_columns,
            clear_rows,
            variation_column,
            variation_row,
            max_clear_column,
            max_clear_row)


if __name__ == '__main__':
    tab = [[1, 1, 0, 0],
           [1, 1, 0, 0],
           [0, 0, 0, 0],
           [0, 1, 0, 0]]

    res = evaluate(tab)
    print(res)
    print((1, 5, 2, 0.7071067811865476, 1.2747548783981963, 1.0565662291666151, 2, 1, 3, 3, 2, 1))
