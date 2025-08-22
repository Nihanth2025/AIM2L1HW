import cv2
image =cv2.imread('example.jpg')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
resized_image=cv2.resize(gray_image,(224,224))


cv2.imshow('Resized Image',resized_image)


key=cv2.waitKey(0)


if key == ord('s'):

  cv2.imwrite('resized_image.jpg',resized_image) 
  print('Image saved as resized_image.jpg')
else:
  print("Image not saved")


cv2.destroyAllWindows()


print(f"Processed image Dimensions: {resized_image.shape}")

