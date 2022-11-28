import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    list_dict = []
    with open(filename) as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i].replace("\n", "")
        header = lines[0].split(sep=",")
        for j in range(1, len(lines)):
            elements = lines[i].split(sep=",")
            list_dict.append(dict(zip(header, elements)))
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
