import numpy as np
import cv2
import imutils
import datetime
import base64
import streamlit as st


gun_cascade = cv2.CascadeClassifier('cascade.xml')


def detect_weapons(frame):
  """Detects weapons in a frame and returns the frame with bounding boxes (optional)."""
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))
  weapon_detected = False  

  for (x, y, w, h) in guns:
    weapon_detected = True  
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(frame, 'Firearm detected!', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 255), 2, cv2.LINE_AA)

  
  return frame, weapon_detected


def video_generator():
  """Generator to yield processed video frames."""
  cap = cv2.VideoCapture(0)
  while True:
    ret, frame = cap.read()
    if not ret:
      break
    # Adjust frame size 
    frame = imutils.resize(frame, width=500)  
    frame, weapon_detected = detect_weapons(frame.copy())
    yield frame, weapon_detected
  cap.release()
  cv2.destroyAllWindows()


def get_text_color(weapon_detected, start_color, end_color):
  """Returns text color based on weapon detection and background gradient."""
  if weapon_detected:
    
    return (255, 255, 255)
  else:
    return (0, 128, 128)  


def main():
  """Streamlit application for real-time weapon detection video with gradient background."""
  st.title("Weapon Detection Video Stream")

  
  start_color = (255, 0, 0)  # Red
  end_color = (0, 255, 0)  # Green

 
  width = 500 

 
  video_container = st.empty()
  text_container = st.empty()

  
  frames = video_generator()
  for frame, weapon_detected in frames:
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  

      
      video_container.image(frame, width=width)

      text_color = get_text_color(weapon_detected, start_color, end_color)

      
      text_container.markdown(f"<h3 style='color: rgb({text_color[0]}, {text_color[1]}, {text_color[2]}); text-align: center;'>{'Firearm detected!' if weapon_detected else ''}</h3>", unsafe_allow_html=True)

      

if __name__ == "__main__":
  main()
