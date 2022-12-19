import cv2
import pytesseract

PATH = 'Z:\Images\8411cd218f6e65f5a6af10c90b787836.jpg'


if __name__ == '__main__':
    frame = cv2.imread(PATH)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=1)
    neural = pytesseract.image_to_string(
        opening,
        lang='eng',
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    )
    print(neural)
