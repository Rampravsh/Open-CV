import cv2
import numpy as np

def run_video_project():
    """
    Captures video from the default camera, converts it to grayscale,
    and displays both original and grayscale feeds side-by-side.
    """
    # Initialize video capture from the default camera
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break

        # Get frame dimensions
        height, width, _ = frame.shape

        # 1. Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 2. Create a 3-channel image from the grayscale version to stack them
        gray_stacked = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

        # 3. Combine the original and grayscale frames side-by-side
        combined_frame = np.hstack((frame, gray_stacked))

        # 4. Add text labels
        cv2.putText(combined_frame, 'Original Color', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(combined_frame, 'Grayscale', (width + 10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)


        # Display the combined frame
        cv2.imshow('Original vs. Grayscale', combined_frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting project...")
            break

    # Release the camera and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_video_project()