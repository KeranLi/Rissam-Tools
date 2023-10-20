import json
import cv2
import numpy as np

class MineralVisualizer:
    def __init__(self, json_file, img_path):
        self.json_file = json_file
        self.data = self.read_data()
        self.img = cv2.imread(img_path)

    def read_data(self):
        with open(self.json_file) as f:
            return json.load(f)

    def label_to_mask(self, shape):
        mask = np.zeros(shape, dtype=np.uint8)

        for s in self.data['shapes']:
            points = s['points']
            label = s['label']
            if label != "_background_":
                color = [int(c) for c in np.random.randint(0, 256, size=3)]
                contours = [np.array(points, dtype=np.int32)]
                cv2.fillPoly(mask, contours, color)

        return mask

    def label_to_rgb(self):
        if self.data is None:
            self.data = self.read_data()

        viz = self.img.copy()  # 创建一个图像副本

        for s in self.data['shapes']:
            label = s['label']
            points = s['points']
            if label != "_background_":
                color = [int(c) for c in np.random.randint(0, 256, size=3)]
                contours = [np.array(points, dtype=np.int32)]
                cv2.fillPoly(viz, contours, color)

        return viz

    def visualize(self):
        if self.data is None:
            self.data = self.read_data()

        viz = self.label_to_rgb()

        # 获取屏幕分辨率
        screen_width, screen_height = 1920, 1080  # 请根据您的屏幕分辨率进行设置

        # 调整图像大小以适应屏幕
        viz = cv2.resize(viz, (screen_width, screen_height))

        # 显示图像
        cv2.imshow('Visualization', viz)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    json_file = './mineral_tool/mineral_data/a17-.json'
    img_file = './mineral_tool/mineral_data/a17-.jpg'
    visualizer = MineralVisualizer(json_file, img_file)
    viz = visualizer.visualize()