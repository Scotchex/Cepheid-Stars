import cv2
import numpy as np

def detect(video_path):
    cap = cv2.VideoCapture(video_path)
    circle_areas = {}
    data = {}
    prev_area = None
    start_time = None

    def calculate_circle_area(radius):
        return 3.14159 * (radius ** 2)

    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

    circle_sizes = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        

        if contours:
            (x, y), radius = cv2.minEnclosingCircle(contours[0])
            area = calculate_circle_area(radius)
            if prev_area is None or area != prev_area:
                prev_area = area
                if start_time is None:
                    start_time = frame_count / fps
            circle_areas[area] = frame_count / fps

            circle_sizes.append((radius, area))
            cv2.putText(frame, f'Area: {area:.2f} sq. px', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
        
        out.write(frame)
        cv2.imshow('Frame', frame)
        delay = int(1000 / fps) 
        cv2.waitKey(delay)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    for area, time in sorted(circle_areas.items(), key=lambda x: x[1]):
        data[time] = round(area)
    
    return data