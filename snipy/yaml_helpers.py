import ruamel_yaml as yaml

def yaml_read(filename):
    with open(filename,'r') as f:
        data = yaml.load(f,Loader=yaml.Loader)
    return data

def yaml_write(filename,data):
    with open(filename,'w') as f:
        yaml.dump(data,f,default_flow_style=None,indent=True)

def yaml_collate_by_keywords(data,keys):
    collated = []
    for k in keys:
        values = []
        for name in data:
            values.append(data[name][k])
        collated.append(values)
    return collated
