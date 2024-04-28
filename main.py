from object_detection import ObjectDetection
import cv2
import tensorflow as tf
import math

# Load object detection
od = ObjectDetection()
center_point_prev_frame = []
cap = cv2.VideoCapture('cars.mp4')
count = 0
tracking_object = dict()
tracking_id = 0
while True:
    ret, frame = cap.read()
    count += 1
    if not ret:
        break
    center_point = []
    (class_ids, scores, boxes) = od.detect(frame)
    for box in boxes:
        (x, y, w, h) = box
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        # print("BOX", count, '', x, y, w, h)
        center_point.append((cx, cy))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if count <= 2:
        for pt in center_point:
            for pt2 in center_point_prev_frame:
                distance = math.sqrt((pt2[0] - pt[0]) ** 2 + (pt2[1] - pt[1]) ** 2)  # Euclidean method

                if distance < 20:
                    tracking_object[tracking_id] = pt
                    tracking_id += 1

    else:
        tracking_object_copy = tracking_object.copy()
        center_point_copy = center_point.copy()

        for object_id, pt2 in tracking_object_copy.items():
            object_exists = False
            for pt in center_point_copy:
                distance = math.sqrt((pt2[0] - pt[0]) ** 2 + (pt2[1] - pt[1]) ** 2)
                if distance < 20:
                    tracking_object[object_id] = pt
                    object_exists = True
                    center_point.remove(pt)
                    continue
            if not object_exists:
                tracking_object.pop(object_id)

    for object_id, pt2 in tracking_object.items():
        cv2.circle(frame, pt2, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt2[0], pt2[1] - 7), 0, 1, (0, 0, 255))
        center_point_prev_frame = center_point.copy()

    print("Tracking objects")
    print(tracking_object)


    print("Current frame left points")
    print(center_point)


    cv2.imshow("Video Capturing", frame)
    key = cv2.waitKey(1)  # To let the window display wait and then close
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
