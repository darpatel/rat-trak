import cv2

# Open video capture with the webcam (0 is typically the default webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully test
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read frames in a loop
while True:
    ret, frame = cap.read()
    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv2.imshow('Webcam Feed', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture when done
cap.release()
cv2.destroyAllWindows()
