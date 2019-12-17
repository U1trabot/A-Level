import cv2
from cv2_tools.Management import ManagerCV2
# keystroke=27 is the button `esc`
manager_cv2 = ManagerCV2(cv2.VideoCapture(0), is_stream=True)

# This for will manage file descriptor for you
for frame in manager_cv2:
  cv2.imshow('Mug Shots', frame)
cv2.destroyAllWindows()
print(manager_cv2.get_fps())