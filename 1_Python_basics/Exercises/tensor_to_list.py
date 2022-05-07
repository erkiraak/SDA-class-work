def tensor_to_list(tensor_3d):
    list = []
    for x in range(len(tensor)):
        for y in range(len(tensor[x])):
            for z in range(len(tensor[x][y])):
                list.append(tensor[x][y][z])
    return list


tensor = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
          [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
          [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]

print(tensor_to_list(tensor))