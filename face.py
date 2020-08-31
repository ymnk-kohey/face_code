import cv2

img = cv2.imread("photo.jpg")

cascade_file_face = "face.xml"
cascade_face = cv2.CascadeClassifier(cascade_file_face)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
human_face = cascade_face.detectMultiScale(img_gray, minSize=(5, 5))


for (x, y, w, h) in human_face:
    color = (0, 225, 0)
    pen_w = 10 
    cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness = pen_w)

font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, "human_face", (x + w + -2100, y + h + -400), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imwrite("photo1.jpg", img)