# -*- coding: UTF-8 -*-

import os

from utils import get_response_json_text, save_text_to_file

base_url = 'https://geo.datav.aliyun.com/areas_v3/bound/'


if not os.path.isdir("mapdata"):
    os.mkdir("mapdata")

if not os.path.isdir("mapdata/china"):
    os.mkdir("mapdata/china")

if not os.path.isdir("mapdata/china/province"):
    os.mkdir("mapdata/china/province")

if not os.path.isdir("mapdata/china/city"):
    os.mkdir("mapdata/china/city")

# if not os.path.isdir("mapdata/china/district"):
#     os.mkdir("mapdata/china/district")

if not os.path.isdir("mapdata/area-code"):
    os.mkdir("mapdata/area-code")

code_dic = {}
parent_dic = {}

print('开始获取infos.json')
infoText = get_response_json_text(base_url + 'infos.json')
if infoText is None:
    exit(-1)

save_text_to_file('infos', infoText)

for code in list(infoText.keys()):
    area = infoText[code]
    level = area['level']
    name = area['name']

    if level in [
        'country',
        'province',
        'city'
    ]:
        code_dic[area['adcode']] = area
        p_code = area['parent']['adcode']
        if p_code is not None:
            if parent_dic.get(p_code) is None:
                parent_dic[p_code] = []
            parent_dic.get(p_code).append(area)

        if level == 'country':
            print(level + ': ' + str(code) + ', ' + name)
            text = get_response_json_text(base_url + code + "_full.json")
            save_text_to_file('china/china', text)
        elif level == 'province':
            print(level + ': ' + str(code) + ', ' + name)
            text = get_response_json_text(base_url + code + "_full.json")
            save_text_to_file('china/province/' + code, text)
        elif level == 'city':
            print(level + ': ' + str(code) + ', ' + name)
            text = get_response_json_text(base_url + code + "_full.json")
            save_text_to_file('china/city/' + code, text)
        # 区域level只有轮廓不需要下载
        # elif level == 'district':
        #     url = base_url + code + ".json"
        #     text = get_response_json_text(url)
        #     save_text_to_file('china/district/' + code, text)

base_path = 'mapdata/china/'

tree_dic = {
    'level': 0,
    'name': "中国",
    'code': 10000,
    "dataPath": base_path + "china.json",
    "items": []
}


def get_children(code, level):
    children = []
    if parent_dic.get(code) is not None:
        for child in parent_dic.get(code):
            child_dic = {
                'level': level,
                'name': child['name'],
                'code': child['adcode'],
                'dataPath': base_path + child['level'] + '/' + str(child['adcode']) + '.json'
            }
            children.append(child_dic)
            child_dic['items'] = get_children(child['adcode'], level + 1)
    return children


tree_dic['items'] = get_children(100000, 1)

save_text_to_file('area-code/china-area', tree_dic)

print("写入完成")
