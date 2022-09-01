import yaml

if __name__ == '__main__':
    # 读取yml内容
    with open("data.yml", encoding="utf-8") as f:
        result = f.read()
        x = yaml.load(result, Loader=yaml.FullLoader)
    print(x)

    # 读取json内容
    with open("json.yml", encoding="utf-8") as f:
        result = f.read()
        x = yaml.load(result, Loader=yaml.FullLoader)
    print(x)

    # 写入yml内容
    x['composition']['1999'].append("许三观卖血记")
    with open("w.yml", 'w', encoding='utf-8') as w_f:
        # 覆盖原先的配置文件
        yaml.dump(x, w_f, allow_unicode=True)