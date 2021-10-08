import cv2

image = cv2.imread('QR.png')
det = cv2.QRCodeDetector()
main_data, data_1, data_2 = det.detectAndDecode(image)
print(main_data)
