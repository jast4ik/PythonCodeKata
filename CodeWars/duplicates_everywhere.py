"""
https://www.codewars.com/kata/5e8dd197c122f6001a8637ca
"""


def remove_duplicate_ids(input_dict: dict):
    s_list = {x: [y for y in input_dict[x]] for x in sorted(input_dict, key=int)}

    for key in s_list:
        for i in reversed(range(len(s_list[key]))):
            if s_list[key].count(s_list[key][i]) > 1:
                s_list[key].pop(i)

    for max_key in reversed(s_list):
        for key in s_list:
            s_list[key] = [x for x in s_list[key] if x not in s_list[max_key]] if key != max_key else s_list[key]

    return s_list


if __name__ == "__main__":
    in_dict = {
        "432": ["A", "A", "B", "D", "A"],
        "53": ["L", "G", "B", "C"],
        "236": ["L", "A", "X", "G", "H", "X"],
        "11": ["P", "R", "S", "D"],
    }

    print(remove_duplicate_ids(in_dict))

