import sys
import os
import yaml
import json
import io


def structure_check(file_name: str):
    content = read_file(file_name)
    try:
        result = json.loads(''.join(content))
        return result
    except json.decoder.JSONDecodeError:
        pass

    try:
        fp = io.StringIO(''.join(content))
        result = yaml.safe_load(fp)
        return result
    except:
        pass

    try:
        result = ''.join(content)
        return result
    except:
        pass


def read_file(file_name: str) :
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data


def writer_file_yaml(data: dict):
    with open('result1.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)


def set_up_structure(path: str, flag=False) -> dict:
    dict_res = dict()
    if len(os.listdir(path)) == 0:
        return dict()
    else:
        for file in os.listdir(path):
            if os.path.isdir(path + f'\\{file}'):
                dict_res[file] = set_up_structure(path + f'\\{file}', True)
            else:
                content = structure_check(path + f'\\{file}')
                dict_res[file] = [content]
    if flag:
        return dict_res
    else:
        helper_dict = dict()
        helper_dict[path.split('\\')[-1]] = dict_res
        return helper_dict


if __name__ == "__main__":
    try:
        args = sys.argv
        writer_file_yaml(set_up_structure(args[1]))
        print('result in result1.yaml')
    except FileNotFoundError:
        print("don't find this file")
