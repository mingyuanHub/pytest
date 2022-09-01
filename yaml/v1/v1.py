import yaml

if __name__ == '__main__':
    with open("data.yml", encoding="utf-8") as f:
        result = f.read()
        x = yaml.load(result, Loader=yaml.FullLoader)
    print(x)

    with open("json.yml", encoding="utf-8") as f:
        result = f.read()
        x = yaml.load(result, Loader=yaml.FullLoader)
    print(x)