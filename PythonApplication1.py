import cv2 as cv
from matplotlib import pyplot as plt





cam = cv.VideoCapture(0)

while True:
    
    result, image = cam.read()

    
    cv.imshow("GeeksForGeeks", image)

    
    key = cv.waitKey(1)
    if key == ord(' '):  
        cv.imwrite("GeeksForGeeks.png", image)
        print("Image captured!")
        break  

    
    if key == ord('q'):
        print("Exiting...")
        break


cam.release()
cv.destroyAllWindows()

img = cv.imread("GeeksForGeeks.png")

image1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.blur(image1, (5, 55))
Gblur = cv.GaussianBlur(image1, (55, 5), 5)
Mblur = cv.medianBlur(image1, 5)
Bblur = cv.bilateralFilter(image1, 20, 200, 200)
sobelxy = cv.Sobel(image1, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
filtered_image_xy = cv.convertScaleAbs(sobelxy)
edges = cv.Canny(image1, 50, 150)
laplacian = cv.Laplacian(image1, cv.CV_64F)



plt.subplot(3,3,1),plt.imshow(img)
plt.text(400, 100, 'orig', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,2),plt.imshow(img_gray)
plt.text(400, 100, 'gray', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,3),plt.imshow(blur)
plt.text(400, 100, 'blur', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,4),plt.imshow(Gblur)
plt.text(400, 100, 'Gaussian', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,5),plt.imshow(Mblur)
plt.text(400, 100, 'median', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,6),plt.imshow(Bblur)
plt.text(400, 100, 'bilateral', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,7),plt.imshow(filtered_image_xy)
plt.text(400, 100, 'SobelXY', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,8),plt.imshow(edges)
plt.text(400, 100, 'Canny', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.subplot(3,3,9),plt.imshow(laplacian)
plt.text(400, 100, 'laplacian', color = 'White', fontsize = 20)
plt.xticks([]),plt.yticks([])
plt.show()
