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


# open the camera for warming up
cap = cv2.VideoCapture('slow.MOV')

# grab the first frame
old_frame = get_frame_from(cap)
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# initiate KCF tracker
tracker = cv2.TrackerKCF_create()

# possible movements ROI


# start the tracking
while True:
    # Record FPS
    timer = cv2.getTickCount()

    # read the current frame
    cur_frame = get_frame_from(cap)

    # covert to gray scale
    cur_gray = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    # Display FPS on frame
    cv2.putText(cur_frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
    # display cur frame
    cv2.imshow('video', cur_frame)
    # waitkey
    if cv2.waitKey(1) == ord('q'):
        break


#(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if __name__ == '__main__':

    # Set up tracker.
    # Instead of MIL, you can also use

    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
    tracker_type = tracker_types[2]

    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()

    # Read video
    video = cv2.VideoCapture('slow.MOV')

    # Exit if video not opened.
    if not video.isOpened():
        print
        "Could not open video"
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)
    if not ok:
        print
        'Cannot read video file'
        sys.exit()

    # Define an initial bounding box
    bbox = (287, 23, 86, 320)

    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    while True:
        # Read a new frame
        ok, frame = video.read()
        frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)
        if not ok:
            break

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

        # Display result
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27: break
