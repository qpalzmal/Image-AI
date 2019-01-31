from imageai.Detection import VideoObjectDetection


def EveryFrame(frame_number, output_array, output_count):
    print("OUTPUT FOR EACH OBJECT: ", output_array)
    print("OUTPUT COUNT FOR UNIQUE OBJECTS: ", output_count)
    # print("END OF FRAME: ", frame_number)
    print("")


detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")

# 1 = bad ---- 5 = good
detector.loadModel(detection_speed="normal")  # 1 speed 5 accuracy
# detector.loadmodel(detection_speed="faster")  # 3 speed 3 accuracy
# detector.loadmodel(detection_speed="flash")  # 5 speed 1 accuracy


detections = detector.detectObjectsFromVideo(input_file_path="Sounds of New York City.mp4",
                                             output_file_path="Videos\NEW YORK",
                                             frames_per_second=30,
                                             minimum_percentage_probability=50,
                                             log_progress=True,
                                             per_frame_function=EveryFrame)

# for object in detections:
#     print(object["name"], ":", object["percentage_probability"])

# camera.release()
print("REEEEEEEEEEEEEEEEEEEEE")
