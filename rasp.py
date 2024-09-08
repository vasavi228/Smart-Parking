import cv2
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
from flask import Flask, Response, send_file
import io

app = Flask(__name__)

def capture_image():
    with PiCamera() as camera:
        camera.resolution = (640, 480)
        rawCapture = PiRGBArray(camera)
        time.sleep(0.1)
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
    return image

def find_empty_squares(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    squares = []

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:  # Check if the contour has 4 sides
            area = cv2.contourArea(approx)
            if area > 1000:  # Filter out small contours
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = w / float(h)
                if 0.9 < aspect_ratio < 1.1:  # Check if the shape is close to a square
                    squares.append((x, y, w, h))

    return squares

def highlight_squares(image, squares):
    for (x, y, w, h) in squares:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

@app.route('/image')
def image():
    image = capture_image()
    squares = find_empty_squares(image)
    highlighted_image = highlight_squares(image, squares)
    _, buffer = cv2.imencode('.jpg', highlighted_image)
    image_io = io.BytesIO(buffer)
    return send_file(image_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
