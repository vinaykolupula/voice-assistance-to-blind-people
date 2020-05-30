import cv2
camera = cv2.VideoCapture(0)
print(camera.isOpened()) # False
print(camera.read()) # (False, None)
