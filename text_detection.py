import cv2
from PIL import  Image
from  pytesseract import pytesseract

camera=cv2.VideoCapture(0)

while True:
    _,img=camera.read()
    cv2.imshow('Yazi Tanima',img)

    if cv2.waitKey(1)&0xFF==ord('s'):
        cv2.imwrite('secondTest.png',img)
        break

camera.release()
cv2.destroyAllWindows()

def tesseract():
    path_of_tes=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path='secondTest.png'
    pytesseract.tesseract_cmd=path_of_tes
    text1=pytesseract.image_to_string(Image.open(image_path))
    print(text1)

tesseract()
