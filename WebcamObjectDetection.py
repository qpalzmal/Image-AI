from imageai.Detection import VideoObjectDetection
import OpenCVCamera as cvcamera
import asyncio


def call_everyframe(frame_number, output_array, output_count):
    loop = asyncio.new_event_loop()
    frame_task = loop.create_task(EveryFrame(frame_number, output_array, output_count))
    loop.run_until_complete(frame_task)


async def EveryFrame(frame_number, output_array, output_count):
    # print(output_array)
    print(output_count)
    # print("END OF FRAME: ", frame_number)
    print("")
    await asyncio.sleep(1)


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
                                          per_frame_function=EverFrame)


async def main():
    # loop = asyncio.new_event_loop()

    # detect_task = loop.create_task(DetectObjects())
    # show_webcam_task = loop.create_task(cvcamera.main())

    # loop.run_until_complete(detect_task)
    # loop.run_until_complete(show_webcam_task)

    await DetectObjects()
    await cvcamera.show_webcam(cam=camera)


if __name__ == "__main__":
    main_loop = asyncio.new_event_loop()
    main_loop.run_until_complete(main())
