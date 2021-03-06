import requests
import base64
import os

URL = 'http://kube-dev.dummy.ai:31900/model/dummy/tf-object-detection/latest'

with open('test_images/image1.jpg', 'rb') as f:
    result = requests.post(URL, json={
        'image': base64.b64encode(f.read()).decode('utf-8'),
        'ext': 'jpg'
    }).json()
    print(result)

    image_binary = base64.b64decode(result['vis'])
    with open('output.png', 'wb') as f:
        f.write(image_binary)
    os.system('open output.png')

