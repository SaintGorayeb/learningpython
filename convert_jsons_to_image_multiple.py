import json
import base64
import numpy as np
import cv2
from PIL import Image
import io
import zlib
import os
from face import detect_faces

def base64_2_image(s):
    z = zlib.decompress(base64.b64decode(s))
    n = np.frombuffer(z, np.uint8)
    mask = cv2.imdecode(n, cv2.IMREAD_UNCHANGED)[:, :, 3]
    return mask

obj = []
count_multiple = 0
count_images = 0
count_no_mask = 0
count_no_faces = 0
count_img_not_found = 0
count_saved_images = 0
for root, directory, filename in os.walk('.'):
    for f in filename:
        count_images += 1
        if f.endswith('.png.json'):
            filename_json = os.path.join(root, f)
            print(filename_json)

            with open(filename_json, 'r') as file:
                json_data = json.loads(file.read())

            objects = json_data['objects']

            print(objects)

            for i, obj in enumerate(objects)
                # IF OBJECT HAS NO MASK ANNOTATION GO TO NEXT FILE
                if 'bitmap' not in obj.keys():
                    count_no_mask += 1
                    continue

                # process bitmap annotation
                image_data = obj['bitmap']['data']
                origin = obj['bitmap']['origin']
                size = (json_data['size']['height'], json_data['size']['width'])

                image = base64_2_image(image_data)
                origin_h = origin[1]
                origin_w = origin[0]

                mask = np.zeros(size)
                mask[origin_h:origin_h+image.shape[0], origin_w:origin_w+image.shape[1]] = image

                # IF ORIGINAL IMAGE NOT FOUND
                img_path = os.path.join(root, f)
                img_ori_path = img_path.replace('ann', 'img').replace('.json', '')
                if not os.path.exists(img_ori_path):
                    count_img_not_found += 1
                    continue
                
                # detect faces
                faces = detect_faces(img_ori_path)
                
                # IF THERE ARE NO FACES IN THE IMAGE
                if len(faces) == 0:
                    count_no_faces += 1
                    continue

                # if it reaches here, save image
                count_saved_images += 1
                filename_png = filename_json.replace('.png.json', f'_{i}.png')
                cv2.imwrite(filename_png, mask)   
            

print('-'*50)
print(f'{count_multiple} multiple objects images found')
print(f'{count_one_object} single object images found')
print(f'{count_no_mask} no mask objects found')
print(f'{count_no_faces} images with no faces discarded')
print(f'{count_img_not_found} missing images')
print(f'{count_saved_images} saved images')
print(f'{count_multiple+count_one_object} total images found')
            