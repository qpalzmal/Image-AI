from imageai.Detection import VideoObjectDetection
import OpenCVCamera as cvcamera
import asyncio


def EveryFrame(frame_number, output_array, output_count):
    # print(output_array)
    print(output_count)
    # print("END OF FRAME: ", frame_number)
    print("")


camera = cvcamera.camera

detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")

# 1 = bad ---- 5 = good
detector.loadModel(detection_speed="normal")  # 1 speed 5 accuracy
# detector.loadmodel(detection_speed="faster")  # 3 speed 3 accuracy
# detector.loadmodel(detection_speed="flash")  # 5 speed 1 accuracy


# calling a async function returns a coroutine object and doesn't run them
async def DetectObjects():
    await detector.detectObjectsFromVideo(output_file_path="Videos\\WEBCAM",
                                          frames_per_second=30,  # LAPTOP WEBCAM RUNS AT 30 FPS
                                          minimum_percentage_probability=50,
                                          log_progress=True,
                                          camera_input=camera,
                                          per_frame_function=EveryFrame)


async def main():
    await cvcamera.show_webcam(cam=camera)
    loop = asyncio.new_event_loop()

    # detect_task = loop.create_task(DetectObjects())
    show_webcam_task = loop.create_task(cvcamera.main())

    # loop.run_until_complete(detect_task)
    loop.run_until_complete(show_webcam_task)

    print("TRY ENSURE FUTURE")
    # asyncio.ensure_future(cvcamera.main())
    await asyncio.ensure_future(DetectObjects())


if __name__ == "__main__":
    main_loop = asyncio.new_event_loop()
    main_loop.run_until_complete(main())
