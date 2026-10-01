import cv2


def extract(
    video_path: str,
    image_prefix: str = "./img/frame_",
    image_extension: str = ".jpg"
):
    # Open Video File
    video_capture = cv2.VideoCapture(video_path)

    # frame counter
    i = 0

    while True:
        ret, frame = video_capture.read()

        if ret:
            i += 1
            imgNumber = str(i).zfill(5)
            name = image_prefix + str(imgNumber) + image_extension

            # writing the extracted images
            cv2.imwrite(name, frame)
        else:
            break    

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    extract("Video.mp4")
