import sys
import os
import yaml
import json


def structure_check(file_name: str):
    try:
        result = read_file_json(file_name)
        return result
    except json.decoder.JSONDecodeError:
        pass
    try:
        result = read_file_yaml(file_name)
        return result
    except:
        pass


def read_file(file_name: str):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data


def read_file_yaml(file_name: str) -> dict:
    with open(file_name, 'r') as file:
        data_from_file = yaml.safe_load(file)
    return data_from_file


def writer_file_yaml(data: dict):
    with open('result.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)


def read_file_json(file_name: str) -> dict:
    with open(file_name, 'r') as file:
        data_from_file = json.load(file)
    return data_from_file


def set_up_structure(path: str, flag=False) -> dict:
    dict_res = dict()
    if len(os.listdir(path)) == 0:
        return dict()
    else:
        for file in os.listdir(path):
            if os.path.isdir(path + f'\\{file}'):
                dict_res[file] = set_up_structure(path + f'\\{file}', True)
            else:
                dict_res[file.split('.')[0]] = [structure_check(path + f'\\{file}')]
    if flag:
        return dict_res
    else:
        helper_dict = dict()
        helper_dict[path.split('\\')[-1]] = dict_res
        return helper_dict


if __name__ == "__main__":
    print(read_file_yaml('validation_rules.yaml'))
    try:
        args = sys.argv
        writer_file_yaml(set_up_structure(args[1]))
        print('result in result.yaml')
    except FileNotFoundError:
        print("don't find this file")
