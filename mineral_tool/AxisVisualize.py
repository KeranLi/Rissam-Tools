import cv2
import numpy as np
from axis import calculate_axes_of_mineral
from BlackWhiteVisualize import create_black_and_white_image_unsave
import json

class AxisVisualizer:
    def __init__(self, json_file):
        self.json_file = json_file

    def visualize(self):
        data, black_white_image = create_black_and_white_image_unsave(self.json_file)

        for s in data['shapes']:
            label = s['label']
            points = s['points']
            if label != "_background_":
                contours = [np.array(points, dtype=np.int32)]

                # 计算轴
                major_axis, minor_axis, center, angle = calculate_axes_of_mineral(contours[0])

                # 将轴的长度转换为整数，以便进行绘制
                major_axis = int(major_axis)
                minor_axis = int(minor_axis)

                # 绘制轴
                center = tuple(map(int, center))  # 确保中心坐标为整数
                angle_deg = np.degrees(angle)
                cv2.ellipse(black_white_image, center, (major_axis, minor_axis), angle_deg, 0, 360, 255, 10)

                print(f"Major Axis: {major_axis} (μm), Minor Axis: {minor_axis} (μm)")
                print(f"Center: {center} (μm), Angle (degrees): {angle_deg} (μm)")

        # 显示图像
        cv2.imshow('Visualization', black_white_image)
        cv2.waitKey()
        # cv2.destroyAllWindows()

if __name__ == '__main':
    json_file = './mineral_tool/mineral_data/a17-.json'  # 替换为您的JSON文件路径
    visualizer = AxisVisualizer(json_file)
    visualizer.visualize()