from imageai.Detection import VideoObjectDetection

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo-tiny.h5")
detector.loadModel()
detections = detector.detectObjectsFromVideo(input_file_path=,
                                             output_file_path=,
                                             frames_per_second=60)
