import cv2

# Check OpenCV version
print("OpenCV version:", cv2.__version__)

# Test camera access (press 'q' to exit)
cap = cv2.VideoCapture(0)  # Open default camera (usually index 0)
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        cv2.imshow('Camera Test', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
