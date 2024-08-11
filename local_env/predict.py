import os
import cv2 
import argparse as ar
from ultralytics import YOLO

def process_image(img,obj_detection):
    """Function to detect object in a given image."""
    
    # Make predictions
    results = obj_detection(img)
    results

    # Extract results
    for result in results:
        boxes = result.boxes  # box coordinates

        for box in boxes:
            label = obj_detection.names[int(box.cls)]
            score = float(box.conf)
            bbox = box.xyxy[0].tolist()
            x1, y1, x2, y2 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

            # Draw the bounding box on the image
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f'{label} {score:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return img

ROOT_DIR = os.getcwd()
args = ar.ArgumentParser()
args.add_argument("--mode",default='image')
args.add_argument("--infilepath",default=os.path.join(ROOT_DIR,"input","image_for_prediction.jpg"))
args.add_argument("--outfilepath",default=os.path.join(ROOT_DIR,"output"))
args = args.parse_args()

# Load a pretrained model
model = YOLO(os.path.join(ROOT_DIR,"runs","detect","train3","weights","best.pt")) 
args.outfilepath = os.path.join(args.outfilepath,os.path.basename(args.infilepath))

if args.mode in ['image'] :
    img = cv2.imread(args.infilepath)
    img = process_image(img,model)
    cv2.imwrite(args.outfilepath,img)
    
else:
    cap = cv2.VideoCapture(args.infilepath)
    ret, frame = cap.read()
    output_video = cv2.VideoWriter(args.outfilepath,
								  cv2.VideoWriter_fourcc(*'MP4V'),
								  25,
								  (frame.shape[1],frame.shape[0]))
    while ret:
        frame = process_image(frame,model)
        output_video.write(frame)
        ret,frame = cap.read()
    cap.release()
    output_video.release()

cv2.destroyAllWindows()
