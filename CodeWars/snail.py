"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
"""


def snail(snail_map):
    snail_list = list()

    while len(snail_map) > 0:
        snail_list += [x for x in snail_map.pop(0)]
        snail_list += [snail_map[i].pop(-1) for i in range(len(snail_map))]
        snail_list += ([x for x in snail_map.pop(-1)[::-1]] if len(snail_map) > 0 else [])
        snail_list += [snail_map[i].pop(0) for i in reversed(range(len(snail_map)))]

    return snail_list


if __name__ == "__main__":
    in_list = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    print(snail(in_list))
