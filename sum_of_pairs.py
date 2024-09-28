def sum_of_pairs(List1):
    List2 = []
    for i in List1:
        for j in List1:
            if i + j == 12:
                pair = (i, j)
                if pair not in List2 and (j, i) not in List2:
                    List2.append(pair)
    return List2

List1 = [7, 6,6, 4, 3, 1, 2, 5]

print(sum_of_pairs(List1))
