from ultralytics import YOLO

model = YOLO("./weights/yolov8n.pt")

results = model.predict(source="./data/samples/SHANGHAI_Test/frames/05_021", show=False, save=True, classes=[0], device=0)