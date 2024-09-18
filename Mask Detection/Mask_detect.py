import cv2
import numpy as np
import imutils
from keras.models import load_model

class FaceMaskDetector:
    def __init__(self, model_path):
        # Load the pre-trained model
        self.model = load_model(model_path)

    def adjust_brightness_contrast(self, frame, brightness=0, contrast=0):
        # Adjust the brightness and contrast of the frame
        if brightness != 0:
            if brightness > 0:
                shadow = brightness
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + brightness
            alpha_b = (highlight - shadow) / 255
            gamma_b = shadow
            frame = cv2.addWeighted(frame, alpha_b, frame, 0, gamma_b)

        if contrast != 0:
            f = 131 * (contrast + 127) / (127 * (131 - contrast))
            alpha_c = f
            gamma_c = 127 * (1 - f)
            frame = cv2.addWeighted(frame, alpha_c, frame, 0, gamma_c)

        return frame

    def detect_mask(self, frame):
        # Resize frame to fit model input
        resized_frame = cv2.resize(frame, (224, 224))
        # Normalize pixel values
        normalized_frame = resized_frame / 255.0
        # Expand dimensions to match model input
        expanded_frame = np.expand_dims(normalized_frame, axis=0)
        # Make prediction
        prediction = self.model.predict(expanded_frame)
        # Return prediction
        return prediction[0][0]  # Assuming binary classification (Mask/No Mask)

# Start video capture
video_capture = cv2.VideoCapture(0)

# Error handling for when the video stream could not be opened
if not video_capture.isOpened():
    raise IOError("Cannot open webcam")

# Load the mask detector model
# Replace 'path_to_mask-detector-model.h5' with the actual path to your model
fmd = FaceMaskDetector("C:/Users/ZRasheed/Desktop/Pekka Task/Updated auto code project/facial based attendance/mask_detector.model")
#fmd = FaceMaskDetector("https://www.kaggle.com/datasets/shantanu1118/face-mask-detection-dataset-with-4k-samples")
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize the frame for optimization
    frame = imutils.resize(frame, width=400)

    # Adjust brightness and contrast
    frame = fmd.adjust_brightness_contrast(frame)

    # Detect mask
    mask_prob = fmd.detect_mask(frame)

    # Add prediction text on frame
    label = "Mask" if mask_prob > 0.5 else "No Mask"  # Adjust the threshold as needed
    label_color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

    cv2.putText(frame, f"{label}: {mask_prob:.2f}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, label_color, 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break loop on key press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture when everything is done
video_capture.release()
cv2.destroyAllWindows()
