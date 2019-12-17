import argparse

import cv2

from cv2_tools.Management import ManagerCV2
from cv2_tools.Selection import SelectorCV2
from cv2_tools.Storage import StorageCV2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--video', default=0,
        help='input video/stream (default 0, it is your main webcam)')

    parser.add_argument('-s', '--stream',
        help='if you pass it, it means that the video is an streaming',
        action='store_true')

    parser.add_argument('-d', '--details',
        help='if you pass it, it means that you want to see the facial vertexes',
        action='store_true')

    parser.add_argument('--scale', type=float, default=1,
        help='optional parameter to resize the input to the face_recognition library')

    parser.add_argument('-f', '--fps', default=0,
        help='int parameter to indicate the limit of FPS (default 0, it means no limit)',
        type=int)

    args = parser.parse_args()

    if type(args.video) is str and args.video.isdigit():
        args.video = int(args.video)
    manager_cv2 = ManagerCV2(cv2.VideoCapture(0), is_stream=True)
for frame in manager_cv2:
  cv2.imshow('Mug Shots', frame)
cv2.destroyAllWindows()
print(manager_cv2.get_fps())