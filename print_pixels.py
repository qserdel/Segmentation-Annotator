# open an image and print all different picel values in the image
import cv2

if __name__ == "__main__":
    image = cv2.imread("/media/qserdel/7d8c20fc-cf80-4533-9e25-c364688455c5/semantic_segmentation/Segmentation-Annotator/color_labels/grass-1.jpg", cv2.IMREAD_GRAYSCALE)
    values = set()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            values.add(image[i,j])
    print("Different pixel values in the image:", values)

