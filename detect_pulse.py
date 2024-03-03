import cv2
import numpy as np

def detect_pulsation(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path) 
    dict_areas = {}
    frame_skip = 0.1
    max_area = 0
    # Iterate through each frame of the video
    frame_count = 0
    while True:
    
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break
        
        # Convert the frame to grayscale for simplicity
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if frame_count % frame_skip == 0:
                contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area >= max_area:
                        max_area = area
                        dict_areas[max_area] = frame_count

        frame_count = frame_count + 1
        print(frame_count)
    
    # Calculate the period of pulsation
    time = 0

    # Release the video capture object
    cap.release()
    return time, dict_areas
