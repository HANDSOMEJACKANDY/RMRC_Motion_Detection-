import numpy as np
import cv2
import time


# get distance between two points
def get_dist(x, y):
    return np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


# a simplified interface to read from video file
def get_frame_from(cap):
    _, frame = cap.read()
    cur_frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)
    return cur_frame


# nominator for possible high contrast fast moving target
def detect_moving_target(old_gray, new_gray):
    pass

# open the camera for warming up
cap = cv2.VideoCapture('slow.MOV')

# grab the first frame
old_frame = get_frame_from(cap)
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)


# possible movements ROI


# start the tracking
while True:
    # Record FPS
    timer = cv2.getTickCount()

    # read the current frame
    cur_frame = get_frame_from(cap)

    # covert to gray scale
    cur_gray = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)

    # Show high contrast moving objects


    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    # Display FPS on frame
    cv2.putText(cur_frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
    # display cur frame
    cv2.imshow('video', cur_frame)
    # waitkey
    if cv2.waitKey(1) == ord('q'):
        break

