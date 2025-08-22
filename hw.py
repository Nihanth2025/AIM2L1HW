import cv2

def main():
    image_path = 'input_image.jpg'
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    print("Original image loaded successfully")

    sizes = {
              'small': (200, 200),
              'medium': (400, 400),  
              'large': (600, 600)  
          }

    for size_name, dimensions in sizes.items():
        resized_image = cv2.resize(image, dimensions)
        cv2.imshow(f"sized {size_name}",resized_image)
        cv2.imshow(f"sized {size_name}.jpg",resized_image)
        print(f"Image resized to {dimensions [0]} x {dimensions [1]} pixels {size_name} and saved.")

    print("Display resizing images. Press any key to exit.")
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__=="__main__":
    main()