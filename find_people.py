import cv2

img = cv2.imread('images/2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('people_body.xml')

results = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=1)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow("Result", img)
cv2. waitKey(0)

