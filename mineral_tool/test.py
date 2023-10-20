import cv2
import numpy as np
from axis import calculate_axes_of_mineral_pixel
from BlackWhiteVisualize import create_black_and_white_image_unsave
import json

json_file = './mineral_tool/mineral_data/a17-.json'
data, black_white_image = create_black_and_white_image_unsave(json_file)
pixel_to_length_ratio = 0.00146
# 创建一个新图像，与黑白图像具有相同的大小和通道
elp = np.copy(black_white_image)  # 使用黑白图像创建一个新图像

for s in data['shapes']:
    label = s['label']
    points = s['points']
    if label != "_background_":
        contours = [np.array(points, dtype=np.int32)]

        # 计算轴
        major_axis, minor_axis, center, angle = calculate_axes_of_mineral_pixel(contours[0])

        # 将轴的长度转换为整数，以便进行绘制
        major_axis = int(major_axis)
        minor_axis = int(minor_axis)

        # 计算轴的端点
        endpoint1 = (
            int(center[0] + 0.5 * major_axis * np.cos(angle)),
            int(center[1] + 0.5 * major_axis * np.sin(angle))
        )
        endpoint2 = (
            int(center[0] - 0.5 * major_axis * np.cos(angle)),
            int(center[1] - 0.5 * major_axis * np.sin(angle))
        )

        # 绘制黑色线
        elp = cv2.line(black_white_image, endpoint1, endpoint2, 0, 10)

        # 绘制红色中心点
        elp = cv2.circle(elp, center, 20, (0, 0, 255), -1)

        # 将长轴长度添加到图像旁边
        cv2.putText(elp, f'Major Axis(cm): {major_axis/10000*pixel_to_length_ratio}', (center[0]+900, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

# 获取屏幕分辨率
screen_width, screen_height = 1920, 1080  # 请根据您的屏幕分辨率进行设置

# 调整图像大小以适应屏幕
elp = cv2.resize(elp, (screen_width, screen_height))

# 显示新图像
cv2.imshow('Visualization', elp)
cv2.waitKey(0)
cv2.destroyAllWindows()