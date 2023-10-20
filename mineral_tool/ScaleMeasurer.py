import cv2
import numpy as np

class ImageScaling:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        self.h, self.w = self.img.shape[:2]
        if self.h > 1000 or self.w > 1000:
            self.scale = min(1000 / self.h, 1000 / self.w)
            self.new_size = (int(self.w * self.scale), int(self.h * self.scale))
            self.img = cv2.resize(self.img, self.new_size)
        self.img_copy = self.img.copy()
        self.roi = cv2.selectROI('image', self.img)
        self.x, self.y, self.w, self.h = self.roi
        self.scale_img = self.img[self.y:self.y + self.h, self.x:self.x + self.w]
        self.point1 = None
        self.point2 = None

    def select_points(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.point1 is None:
                self.point1 = (x, y)
                cv2.circle(self.scale_img, self.point1, 5, (0, 0, 255), -1)
                cv2.imshow('scale_img', self.scale_img)
            elif self.point2 is None:
                self.point2 = (x, y)
                cv2.circle(self.scale_img, self.point2, 5, (0, 0, 255), -1)
                cv2.imshow('scale_img', self.scale_img)

    def run(self):
        cv2.imshow('scale_img', self.scale_img)
        cv2.setMouseCallback('scale_img', self.select_points)
        cv2.waitKey(0)
        if self.point1 is None or self.point2 is None:
            raise ValueError("未选择足够的点")
        else:
            dist = np.sqrt((self.point1[0] - self.point2[0])**2 + (self.point1[1] - self.point2[1])**2)
            if dist < 5:
                raise ValueError("两点距离太近，请重新选择")
            else:
                length_pixels = dist
                length_real = float(input("请输入实际长度(um):"))
                scale = length_real / length_pixels
                return {"scale": scale}

# 示例用法
try:
    scaling = ImageScaling("./mineral_tool/mineral_data/a17-.jpg")
    result = scaling.run()
    print("缩放比:", result["scale"])
except ValueError as e:
    print(e)