import cv2
import mediapipe as mp
import pandas

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()


video_path = "kickboxing-muay thai.mp4" 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # when video ends
    
    # frame to RGB 
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = pose.process(rgb_frame)
    
    # landmarks
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # display
    cv2.imshow('MediaPipe Skeleton', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


cap.release()
cv2.destroyAllWindows()


# add exception handling