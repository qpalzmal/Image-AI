from imageai.Detection import VideoObjectDetection
import cv2
import OpenCVCamera as webcam
import asyncio


# LAPTOP WEBCAM RUNS AT 30 FPS
def EveryFrame(frame_number, output_array, output_count):
    # print(output_array)
    print(output_count)
    # print("END OF FRAME: ", frame_number)
    print("")


camera = cv2.VideoCapture(0)

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")

# 1 = bad ---- 5 = good
detector.loadModel(detection_speed="normal")  # 1 speed 5 accuracy
# detector.loadmodel(detection_speed="faster")  # 3 speed 3 accuracy
# detector.loadmodel(detection_speed="flash")  # 5 speed 1 accuracy


async def main():
    await detector.detectObjectsFromVideo(output_file_path="Videos\\WEBCAM",
                                          frames_per_second=30,
                                          minimum_percentage_probability=50,
                                          log_progress=True,
                                          camera_input=camera,
                                          per_frame_function=EveryFrame)
    await webcam.main()


if __name__ == "__main__":
    try:
        main()
    finally:
        print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print("")
        detector.detectObjectsFromVideo(output_file_path="Videos\\WEBCAM",
                                        frames_per_second=30,
                                        minimum_percentage_probability=50,
                                        log_progress=True,
                                        camera_input=camera,
                                        per_frame_function=EveryFrame)
        webcam.main()
