import cv2
import win32gui
import win32con
import pygetwindow as gw

def hide_taskbar_and_bring_to_front(window_title):
    # Find the window by title (exact match)
    hwnd = win32gui.FindWindow(None, window_title)
    
    if hwnd:
        # Remove the taskbar icon by changing the window style
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style | win32con.WS_EX_TOOLWINDOW)

        # Bring window to the front
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)

def process_image():
    # Open image recognition window
    cap = cv2.VideoCapture(0)  # Example, use your image recognition logic here
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Image Recognition', frame)

        # Bring to front once window opens
        hide_taskbar_and_bring_to_front('Image Recognition')

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_image()

#another

import cv2

def process_video(frame_limit=100):
    cap = cv2.VideoCapture(0)  # Change 0 to your video file path if needed

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        
        # Check if frame limit is reached
        frame_count += 1
        if frame_count >= frame_limit:
            break

    # Release the capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()

    return "Finished after processing {} frames".format(frame_count)

if __name__ == "__main__":
    result = process_video()
    print(result)
