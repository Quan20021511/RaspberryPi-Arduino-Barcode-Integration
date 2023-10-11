import cv2
from pyzbar.pyzbar import decode
import serial

# Constants for barcode values
barcode1 = "20161299"
barcode2 = "20161290"

# Initialize camera
cap = cv2.VideoCapture(0)

# Initialize a list to store barcode content
barcode_codes = []

# Initialize a serial communication object
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
    ser.reset_input_buffer()

while True:
    # Read frames from the camera
    ret, frame = cap.read()

    # Convert the image from BGR to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect barcodes in the image
    barcodes = decode(gray)

    for barcode in barcodes:
        data1 = barcode.data.decode("utf-8")

        if data1 not in barcode_codes:
            content = data1[0:8]
            barcode_codes.append(data1)

            with open('Barcode_codes.txt', 'a') as f:
                f.write(content + '\n')

            print("Barcode:", content)

        if data1 == barcode1:
            ser.write(b"1\n")
            content = " "
            dt = ser.readline().decode().rstrip()
            print(dt)

        if data1 == barcode2:
            ser.write(b"2\n")
            content = " "
            dt = ser.readline().decode().rstrip()
            print(dt)

        x, y, w, h = barcode.rect

        # Draw a bounding box around the barcode
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 150, 0), 2)

        # Resize the image to 640x480
        frame = cv2.resize(frame, (640, 480))

        # Display the image on the screen
        cv2.imshow('frame', frame)

        # If the user presses 'q', exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release camera resources and close all display windows
cap.release()
ser.close()
cv2.destroyAllWindows()
