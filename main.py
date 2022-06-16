# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# from moviepy.editor import *

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60

#
#
# import imageio.v3 as iio
#
# for i, frame in enumerate(iio.imiter("D:\\18776860-1-80.flv")):
#     print("Mean of frame %i is %1.1f" % (i, frame.mean()))

def read_one_frame():
    import cv2 as cv

    cap = cv.VideoCapture('D:\\18776860-1-80.flv')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        print(frame)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        cv.imwrite('xxxxxxxxxxxxxxxxxxxxx' + '.jpg', frame)

        break
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

import cv2


def clip_video(source_video, target_video, start_time, end_time):
    cap = cv2.VideoCapture(source_video)
    if not cap.isOpened():
        print('video is not opened')
    else:
        success, frame = cap.read()
        f_shape = frame.shape
        f_height = f_shape[0]  # 原视频图片的高度
        f_width = f_shape[1]
        fps = cap.get(5)  # 帧速率
        frame_number = cap.get(7)  # 视频文件的帧数
        duration = frame_number / fps  # 视频总帧数/帧速率 是时间/秒【总共有多少秒的视频时间】
        if start_time > duration or end_time > duration:
            return
        start_time = fps * float(start_time)
        end_time = fps * float(end_time)
        # AVI格式编码输出 XVID
        four_cc = cv2.VideoWriter_fourcc(*'H264')
        video_writer = cv2.VideoWriter(target_video, four_cc, fps, (int(f_width), int(f_height)))
        num = 0
        while True:
            success, frame = cap.read()
            if int(start_time) <= int(num) <= int(end_time):
                if success:
                    video_writer.write(frame)
                else:
                    break
            num += 1
            if num > frame_number:
                break
    cap.release()