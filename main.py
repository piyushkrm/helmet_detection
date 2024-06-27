from ultralytics import YOLO
  
# trained models
model = YOLO("models/best.pt")

# model = YOLO("models/yolov8.pt")

# model = YOLO("models/yolov8n.pt")
  

#detect object using videos
# model.predict(source="video/video2.mp4", save=True, show=True)           
# model.predict(source="video/video.mp4", save=True, show=True)           

#detect object using images
# model.predict(source="img/vander-films-v8CuPrOvKUA-unsplash.jpg", save=True, show=True)         
# model.predict(source="img/img.jpg", save=True, show=True)         

# detect object using url  
# model.predict(source="https://media.istockphoto.com/id/481220364/photo/beautiful-couple-cycling-on-the-road.jpg?s=2048x2048&w=is&k=20&c=0fBHn2PRrYhNNZcjWV7blBnEDmFDCiisuPsdHoU8bZU=", save=True, show=True)           

#detect object using webcam
model.predict(source="0", show=True)     

  