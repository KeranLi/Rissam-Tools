import json
import cv2
print(cv2.__version__)
import numpy as np

#----------Define the function for calculating the area of a single mineral crystal start----------
def calculate_single_area(points, pixel_to_length_ratio):
  # Gain ponits in the annotated files
  points = np.array(points).astype(np.float32)
  # Calculating pixel areas
  pixel_area = cv2.contourArea(points)
  # Transform to actual areas
  actual_area = pixel_area * (pixel_to_length_ratio ** 2)
  return actual_area
#----------Define the function for calculating the area of a single mineral crystal over----------

#----------Define the function for calculating the area of total mineral crystals start----------
def calculate_total_area(data, pixel_to_length_ratio):
  # Area initializing
  total_area = 0 
  # Loading all annotated shapes
  for shape in data['shapes']:
    # Gain ponits in the annotated files
    points = np.array(shape['points']).astype(np.float32)
    # Check the integraty of annotated files
    if points.size > 0:
      try:
        # Calculating pixel areas
        pixel_area = cv2.contourArea(points)
        # Transfrom to actual areas
        actual_area = pixel_area * (pixel_to_length_ratio ** 2)
      except Exception as e:
        print("-----------Unfortunately!Errors occurred during calculation!----------:", e) 
        actual_area = 0
    else:
      actual_area = 0
    # Total area
    total_area += actual_area
  return total_area
#----------Define the function for calculating the area of total mineral crystals over----------

#----------Define the function for calculating the areas of every mineral crystals start---------- 
def calculate_multiple_area(data, pixel_to_length_ratio):
  # List initialization, for store the areas of each crystal
  areas = []
  # Loading all crystals  
  for shape in data['shapes']:
     # Calculate the actual area of each crystal  
     area = calculate_single_area(shape['points'], pixel_to_length_ratio)
     # Adding to the list
     areas.append(area)

  return areas
#----------Define the function for calculating the areas of every mineral crystals over----------

# -----------Here is a example of single crystal for testing start----------
'''
@Note: here I pre-set an isosceles right triangle where the side is 100.
       Theoritically, the area would be 5000
'''
data = {'shapes': [{'points': [[0,0], [100,0], [100,100]]}]}
shape = data['shapes'][0]
points = shape['points']
single_area = calculate_single_area(points, 1)
print("----------Test start----------\n")
print(
  "-----------Congratulation!The area is: {}----------\n".format(single_area)
) # 5000
print("----------Test over----------\n")
# -----------Here is a example of single crystal for testing over----------

# -----------Here is a example of multiple crystals for testing start----------
data = {
  'shapes': [
    {
      'points': [[0,0], [100,0], [100,100]] # 第一个三角形
    },
    { 
     'points': [[0,0], [200,0], [200,200]] # 第二个三角形
    }
  ]
}

# calculate areas of each crystal
each_areas = calculate_multiple_area(data, 1)

print("----------Test start----------\n")
print("----------Each shape's area:----------\n")
for index, area in enumerate(each_areas):
  print("----------Shape {}: {}----------\n".format(index+1, area))
print("----------Test over----------\n")
# -----------Here is a example of multiple crystals for testing over----------

# Main function
if __name__ == '__main__':

  # Loading my annotated data
  with open('./mineral_tool/mineral_data/a17-.json') as f:
    data = json.load(f)

  # Calculating
  every_area = calculate_multiple_area(data, 1.56)

  # Results print
  print("----------Mineral calculating start----------\n")
  print("----------Each shape's area:----------\n")
  for index, area in enumerate(every_area):
    print("----------Shape {}: {} (μm x μm)----------\n".format(index+1, area))
  print("----------Mineral calculating over----------\n")