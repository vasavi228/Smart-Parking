This project uses Raspberry Pi equipped with a camera monitors parking spaces, detecting vehicle movement using computer vision. Real-time occupancy data is fed into a booking website, allowing users to reserve available spots. Python and OpenCV handle image processing and car detection, while the backend manages user information and bookings.

Raspberry Pi Sensor
Overview:  
The Raspberry Pi 3B+ is equipped with a Pi Camera module to monitor and detect vehicle movement within parking areas.
Detailed Process:
- Camera Setup: The Pi Camera module is connected to the Raspberry Pi 3B+. It captures video footage of the parking spaces.
- Image Processing: Using computer vision algorithms (e.g., OpenCV), the Raspberry Pi analyzes the captured video frames to detect the presence or movement of vehicles.
- Detection Logic: Algorithms are programmed to recognize changes in pixel intensity or motion patterns that indicate a vehicle entering or leaving a parking space.
- Output: When a vehicle is detected, the system updates the parking occupancy status in real-time, which can be further processed by other components of the system.


Booking Website
Overview:
A user-friendly website enables remote booking of parking slots, enhancing convenience for users.
Detailed Process:
- User Interface: The website provides an intuitive interface where users can view available parking slots, select a desired slot, and make a booking.
- Booking Management: Upon selection, the booking system communicates with the backend server to reserve the chosen parking slot.
- Confirmation: Users receive confirmation of their booking via email or SMS, including details such as slot number and duration.
- Integration: The booking website interfaces with other system components to ensure real-time updates on slot availability and occupancy status.

- Backend Processes
Overview:
Python programming language uses OpenCV and YOLO for car detection and backend image processing to manage user information and parking slot bookings.
Detailed Process:
Car Detection and Image Processing: OpenCV is used along with the haarcascade_cars.xml file for initial car detection. 
Three YOLO files are employed for further processing:
A Python file for car detection
A configuration file
A weights file







