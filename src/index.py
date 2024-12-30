import cv2 as cv
from config import lower_bound, upper_bound


def detect_color():
    video_feed = cv.VideoCapture(0) # that we take the webcam feed

    while True:
        _, frame = video_feed.read()
        #  in the hsv colour space it helps to separate the intensity of the colour from the colour itself
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  
        #  the inrange method the real goat which help us to detect the colour
        mask = cv.inRange(hsv, lower_bound, upper_bound)
        res = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('res', res)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    video_feed.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    detect_color()