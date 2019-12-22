import ruamel_yaml as yaml

def read_yaml(filename):
    with open(filename,'r') as f:
        data = yaml.load(f,Loader=yaml.Loader)
    return data

def write_yaml(filename,data):
    with open(filename,'w') as f:
        yaml.dump(data,f,indent=True)

def collate_yaml_keywords(data,keys):
    collated = []
    for k in keys:
        values = []
        for name in data:
            values.append(data[name][k])
        collated.append(values)
    return collated
