import cv2
import numpy as np
import json

def create_black_and_white_image_save(json_file, output_image_path):
    # 读取JSON数据
    with open(json_file, 'r') as file:
        data = json.load(file)

    # 获取图像的宽度和高度
    width = data['imageWidth']
    height = data['imageHeight']

    # 创建一个空白的黑白图像
    black_white_image = np.zeros((height, width), dtype=np.uint8)

    for s in data['shapes']:
        label = s['label']
        points = s['points']
        if label != "_background_":
            contours = [np.array(points, dtype=np.int32)]

            # 填充轮廓
            cv2.fillPoly(black_white_image, contours, 255)

    # 保存生成的黑白图像
    cv2.imwrite(output_image_path, black_white_image)

    return black_white_image

def create_black_and_white_image_unsave(json_file):
    # 读取JSON数据
    with open(json_file, 'r') as file:
        data = json.load(file)

    # 获取图像的宽度和高度
    width = data['imageWidth']
    height = data['imageHeight']

    # 创建一个空白的黑白图像
    black_white_image = np.zeros((height, width), dtype=np.uint8)

    for s in data['shapes']:
        label = s['label']
        points = s['points']
        if label != "_background_":
            contours = [np.array(points, dtype=np.int32)]

            # 填充轮廓
            cv2.fillPoly(black_white_image, contours, 255)

    return data, black_white_image

if __name__ == '__main__':
    json_file = './mineral_tool/mineral_data/a17-.json'  # 替换为您的JSON文件路径
    output_image_path = './mineral_tool/results/output_image.png'  # 保存生成的黑白图像的路径
    create_black_and_white_image_save(json_file, output_image_path)