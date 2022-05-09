import os
import yaml
import json
import io


def writer_file(data, file_name: str):
    try:
        result = json.loads(str(data))
        with open(file_name, 'w') as file:
            json.dump(result, file)
        return 1
    except json.decoder.JSONDecodeError:
        pass

    try:
        fp = io.StringIO(str(data))
        result = yaml.safe_load(fp)
        with open(file_name, 'w') as file:
            yaml.dump(result, file, default_flow_style=False)
        return 1
    except:
        pass

    try:
        result = ''.join(data)
        with open(file_name, 'w') as file:
            file.writelines(data)
        return result
    except:
        pass


def read_file_yaml(file_name: str) -> dict:
    with open(file_name, 'r') as file:
        data_from_file = yaml.safe_load(file)
    return data_from_file


def is_dir(key: str) -> bool:
    return not(key.split('.')[-1] in ('txt', 'yaml', 'json'))


def set_up_structure(structure: dict, path=[]):
    list_keys = list(structure.keys())
    for key in list_keys:
        if is_dir(key):
            os.mkdir(os.getcwd()+'\\'+'\\'.join(path)+f'\\{key}')
            path.append(key)
            set_up_structure(structure[key], path)
            del path[-1]
        else:
            data = structure[key]
            writer_file(data, os.getcwd()+'\\'+'\\'.join(path) + f'\\{key}')


if __name__ == "__main__":
    dict_dir = read_file_yaml(os.getcwd()+'\\result1.yaml')
    set_up_structure(dict_dir)
