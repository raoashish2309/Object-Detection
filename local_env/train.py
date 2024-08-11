import os
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="data/config.yaml", epochs=150)  # train the model
metrics = model.val()                      # evaluate model performance on the validation set