import time
import cv2

try:
  capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
except TypeError:
  capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
  raise IOError

capture.set(cv2.CAP_PROP_CONVERT_RGB, False)
capture.set(cv2.CAP_PROP_BUFFERSIZE, 4)
capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y', 'U', 'Y', 'V'))
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
capture.set(cv2.CAP_PROP_FPS, 30)

last_capture_start_time = time.time()
while(True):
  try:
    capture_start_time = time.time()
    ret, frame = capture.read()
    if ret is False:
      raise IOError
    capture_end_time = time.time()
    print("Capture FPS = ", 1.0 / (capture_end_time- capture_start_time))
    cv2.imshow('frame',cv2.cvtColor(frame, cv2.COLOR_YUV2BGR_YUYV))
    cv2.waitKey(1)
    print("Real FPS = ", 1.0 / (time.time() - last_capture_start_time))
    last_capture_start_time = capture_start_time
  except KeyboardInterrupt:
    # 終わるときは CTRL + C を押す
    break

capture.release()
cv2.destroyAllWindows()