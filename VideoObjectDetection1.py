from imageai.Detection import VideoObjectDetection


def EveryFrame(frame_number, output_array, output_count):
    # print("OUTPUT FOR EACH OBJECT:", output_array)
    print("OUTPUT COUNT FOR UNIQUE OBJECTS:", output_count)

    fps = 29  # fps that the script reports for 1 second of the video
    # "Sounds of New York City".mp4 = 29 fps
    # "Road traffic video for object recognition".mp4 = 25 fps

    # used to convert the seconds to usual hrs:mins:secs format
    seconds = frame_number / fps
    minutes = 0
    hours = 0
    while minutes - 60 >= 0 or seconds - 60 >= 0:
        if seconds - 60 >= 0:
            minutes += 1
        else:
            hours += 1
    print("TIME:", str(hours) + ":" + str(minutes) + ":" + str(seconds.__round__(2)))
    print("")


detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")

# 1 = bad ---- 5 = good
# detector.loadModel(detection_speed="normal")  # 1 speed 5 accuracy
detector.loadModel(detection_speed="faster")  # 3 speed 3 accuracy
# detector.loadModel(detection_speed="flash")  # 5 speed 1 accuracy


detections = detector.detectObjectsFromVideo(input_file_path="Road traffic video for object recognition.mp4",
                                             output_file_path="Videos\\ROAD",
                                             frames_per_second=29,
                                             minimum_percentage_probability=50,
                                             log_progress=True,
                                             per_frame_function=EveryFrame)

# only executes once the whole video has been analyzed
print("REEEEEEEEEEEEEEEEEEEEE")
