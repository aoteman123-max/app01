import yaml

with open("./data3.yaml","r",encoding="utf-8")as f:
    data=yaml.safe_load(f)
    print("返回字典数据：",data)
    # print(type(data.get("int_value")))
    # print(type(data.get("bool2")))
    # print(type(data.get("data4")))
    print("返回数据类型：",type(data))