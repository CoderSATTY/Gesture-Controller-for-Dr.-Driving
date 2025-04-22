import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Convert BGR to RGB (MediaPipe requires RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame to detect hands
    results = hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),  # Landmark color
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)                   # Connection color
            )
            tip_ids = [4, 8, 12, 16, 20]  # Thumb to pinky tips
   
            wrist = hand_landmarks.landmark[0]
            thumb_f = hand_landmarks.landmark[4]
            # index_f = hand_landmarks.landmark[8]
            # middle_f = hand_landmarks.landmark[12]
            # ring_f = hand_landmarks.landmark[16]
            # little_f = hand_landmarks.landmark[20]
            height, width, _ = frame.shape
            wrist_x, wrist_y = int(wrist.x * width), int(wrist.y * height)
            total_dist = 0

            fingers_up = 0
            fin_tip_ids = tip_ids[1:]  # Index finger to pinky tips
            base_ids = [6, 10, 14, 18]   # Their bases
            if thumb_f.x > hand_landmarks.landmark[3].x:
                    fingers_up += 1

            for tip, base in zip(fin_tip_ids, base_ids):
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[base].y:
                    fingers_up += 1
            if fingers_up >= 4:

                cv2.putText(frame,"Accelerating",(40,100),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    
            elif fingers_up <= 1:
                 
                 cv2.putText(frame,"Braking",(40,100),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
    

            for idx in tip_ids:
                tip = hand_landmarks.landmark[idx]
                tip_x, tip_y = int(tip.x * width), int(tip.y * height)
                rel_x = tip_x - wrist_x
                rel_y =  wrist_y - tip_y 
                # Calculate the distance between tips from ref line
                total_dist+=rel_x


                    
                # print(f"Finger Tip {idx} (relative to wrist): ({rel_x}, {rel_y})")
                print(f"Finger Tip {idx/4}: ({rel_x }, {rel_y})")
                cv2.putText(frame, f"({rel_x },{rel_y})", (tip_x , tip_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)    
                cv2.line(frame, (wrist_x, wrist_y), (wrist_x, 100), (255, 0, 255), 2) 
                cv2.ellipse(
                            frame, 
                            (wrist_x, wrist_y),         
                            (200, 200),                  
                            0,                         
                            180,                          
                            360,                       
                            (0, 255, 0),                
                            2                            
                        )
                if idx==20:
                    cv2.putText(frame, f"Distance = {total_dist}", (wrist_x , 95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                    print           


    cv2.imshow('Hand Landmarks', frame)

    if cv2.waitKey(1) == 13:
        break


# if __name__ == "__main__":



cap.release()
cv2.destroyAllWindows()
