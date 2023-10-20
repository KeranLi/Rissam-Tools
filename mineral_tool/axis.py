import cv2
import numpy as np

def calculate_axes_of_mineral_actual(contour, pixel_to_length_ratio):
    # 计算轮廓的矩
    M = cv2.moments(contour)
    
    # 计算轮廓的中心
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    
    # 计算长轴和短轴的方向
    theta = 0.5 * np.arctan2(2 * M['mu11'], M['mu20'] - M['mu02'])
    
    # 计算长轴和短轴的长度
    a = np.sqrt(8 * (M['mu20'] + M['mu02'] + np.sqrt(4 * M['mu11']**2 + (M['mu20'] - M['mu02'])**2)))
    b = np.sqrt(8 * (M['mu20'] + M['mu02'] - np.sqrt(4 * M['mu11']**2 + (M['mu20'] - M['mu02'])**2)))
    
    major_axis = max(a, b) * pixel_to_length_ratio
    minor_axis = min(a, b) * pixel_to_length_ratio

    print(f"Major Axis (μm): {major_axis}, Minor Axis (μm): {minor_axis}")
    print(f"Center: {(cx, cy)}, Angle (degrees): {np.degrees(theta)}")
    
    return major_axis, minor_axis, (cx, cy), theta

def calculate_axes_of_mineral_pixel(contour):
    # 计算轮廓的矩
    M = cv2.moments(contour)
    
    # 计算轮廓的中心
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    
    # 计算长轴和短轴的方向
    theta = 0.5 * np.arctan2(2 * M['mu11'], M['mu20'] - M['mu02'])
    
    # 计算长轴和短轴的长度
    a = np.sqrt(8 * (M['mu20'] + M['mu02'] + np.sqrt(4 * M['mu11']**2 + (M['mu20'] - M['mu02'])**2)))
    b = np.sqrt(8 * (M['mu20'] + M['mu02'] - np.sqrt(4 * M['mu11']**2 + (M['mu20'] - M['mu02'])**2)))
    
    major_axis = max(a, b)
    minor_axis = min(a, b)

    print(f"Major Axis (μm): {major_axis}, Minor Axis (μm): {minor_axis}")
    print(f"Center: {(cx, cy)}, Angle (degrees): {np.degrees(theta)}")
    
    return major_axis, minor_axis, (cx, cy), theta