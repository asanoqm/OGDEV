import requests
import json
import base64  # 画像はbase64でエンコードする必要があるため

API_KEY = "APIのキーを記入"

def text_detection(image_path):
    api_url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(API_KEY)
    with open(image_path, "rb") as img:
        image_content = base64.b64encode(img.read())
        req_body = json.dumps({
            'requests': [{
                'image': {
                    'content': image_content.decode('utf-8')  # base64でエンコードしたものjsonにするためdecodeする
                },
                'features': [{
                    'type': 'TEXT_DETECTION'
                }]
            }]
        })
        res = requests.post(api_url, data=req_body)
        res_json = res.json()
        res_text = res_json["responses"][0]["textAnnotations"][0]["description"]

        return res_text


if __name__ == "__main__":
    img_path = "leader.jpg"
    result = text_detection(img_path)
    print(result)
