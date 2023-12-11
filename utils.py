import json
import urllib.request
import urllib.parse
import ssl


context = ssl._create_unverified_context()


def get_response_json_text(url):
    print('请求数据: ' + url)
    try:
        with urllib.request.urlopen(url, context=context, ) as response:
            # print('获取成功')
            return json.loads(response.read().decode("UTF-8"))
    except Exception as e:
        print(e.code, '报错', e)


def save_text_to_file(name, text):
    if text is not None:
        # if not os.path.isdir("mapdata/"):
        #     os.mkdir("mapdata/" + level)
        try:
            with open("mapdata/" + name + ".json", "w", encoding='utf-8') as file:
                json.dump(text, file, ensure_ascii=False)
        except Exception as e:
            print(e.code, '报错', e)
