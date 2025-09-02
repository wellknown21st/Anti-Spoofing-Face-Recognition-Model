from cvzone.FaceDetectionModule import FaceDetector
import cv2
import torch

print(torch.cuda.device_count())
print(torch.cuda.get_device_name())
def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        if bboxs:
            for bbox in bboxs:
                center = bbox["center"]
                x, y, w, h = bbox['bbox']
                score = int(bbox['score'][0] * 100)
                cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()
