from imageai.Detection import VideoObjectDetection
import pprint


def EveryFrame(frame_number, output_array, output_count):
    # print("OUTPUT FOR EACH OBJECT:", output_array)
    pprint.pprint(output_array)
    print("OUTPUT COUNT FOR UNIQUE OBJECTS:", output_count)

    # ---- sample output will need later ----
    # Processing
    # Frame: 11
    # [{'box_points': array([240, 421, 320, 478]),
    #   'name': 'car',
    #   'percentage_probability': 69.86241936683655},
    #  {'box_points': array([763, 461, 843, 542]),
    #   'name': 'car',
    #   'percentage_probability': 54.16259765625},
    #  {'box_points': array([935, 522, 1050, 620]),
    #   'name': 'car',
    #   'percentage_probability': 83.64400863647461},
    #  {'box_points': array([1180, 601, 1274, 721]),
    #   'name': 'car',
    #   'percentage_probability': 57.02694058418274},
    #  {'box_points': array([337, 590, 475, 716]),
    #   'name': 'car',
    #   'percentage_probability': 89.89233374595642}]
    # OUTPUT
    # COUNT
    # FOR
    # UNIQUE
    # OBJECTS: {'car': 5}
    # TIME: 0:0: 0.44
    # -------------------------------------------

    fps = 25  # fps that the script reports for 1 second of the video
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
                                             output_file_path="Videos\\ROAD (faster)",
                                             frames_per_second=25,
                                             minimum_percentage_probability=50,
                                             log_progress=True,
                                             per_frame_function=EveryFrame)

# only executes once the whole video has been analyzed
print("REEEEEEEEEEEEEEEEEEEEE")
