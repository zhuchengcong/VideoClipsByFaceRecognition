# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import os

import face_recognition


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
    cap = cv.VideoCapture('target.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            rgb_frame = frame[:, :, ::-1]
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # cv.imshow('frame', gray)
        cv.imshow('frame', frame)
        # cv.imwrite('xxxxxxxxxxxxxxxxxxxxx' + '.jpg', rgb_frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


# read_one_frame()


def clip_video(source_video, target_video, start_time, end_time):
    import cv2
    cap = cv2.VideoCapture(source_video)
    if not cap.isOpened():
        print('video is not opened')
    else:
        success, frame = cap.read()
        f_shape = frame.shape
        f_height = f_shape[0]  # 原视频图片的高度
        f_width = f_shape[1]
        fps = cap.get(5)  # 帧速率
        print('帧速率:', fps)
        frame_number = cap.get(7)  # 视频文件的帧数
        duration = frame_number / fps  # 视频总帧数/帧速率 是时间/秒【总共有多少秒的视频时间】
        if start_time > duration or end_time > duration:
            return
        start_time = fps * float(start_time)
        end_time = fps * float(end_time)
        # AVI格式编码输出 XVID
        four_cc = cv2.VideoWriter_fourcc(*'mp4v')
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


def clip_video_by_face(source_video, target_video, img, detection_interval_time):
    """
    剪辑视频中出现人脸的片段
    :param source_video: 源视频路径
    :param target_video: 输出视频路径
    :param img: 需要剪辑的人脸
    :param detection_interval_time: 人脸对比间隔时间单位秒，间隔时间越大，速度越快，出现人脸的视频前后视频时间越长
    :return:
    """
    if not os.path.exists(img):
        raise FileNotFoundError('not exists' + img)
    if not os.path.exists(source_video):
        raise FileNotFoundError('not exists' + source_video)

    known_image = face_recognition.load_image_file(img)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    known_faces = [known_encoding]
    # print('start_time', datetime.datetime.now())
    start_time = datetime.datetime.now()
    import cv2
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
        four_cc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(target_video, four_cc, fps, (int(f_width), int(f_height)))

        read_num = 25 * detection_interval_time
        num = 25 * detection_interval_time
        count = 0
        find = False
        while True:
            count += 1
            print('progress', str("%.2f" % (count/frame_number * 100)) + '%')
            success, frame = cap.read()
            if success:
                if find:
                    if num < read_num:
                        video_writer.write(frame)
                        num += 1
                    else:
                        # print('write num', num)
                        find = False
                else:
                    if num < read_num:
                        num += 1
                    else:
                        # print('pass_num', num)
                        rgb_frame = frame[:, :, ::-1]
                        face_locations = face_recognition.face_locations(rgb_frame)
                        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                        for face_encoding in face_encodings:
                            result = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
                            # print(result * 30)
                            if result[0]:
                                print('write face true frame')
                                video_writer.write(frame)
                                num = 0
                                find = True
                                break
                            else:
                                # print(num)
                                num = 0
                                find = False
            else:
                break
    cap.release()
    # print('endtime', datetime.datetime.now())
    end_time = datetime.datetime.now()
    print('spend time:', end_time - start_time)


# clip_video_by_face('F:\\剪辑素材库\\陈都灵\\source.mp4', 'F:\\剪辑素材库\\陈都灵\\test2.mp4', 'chenduling.png', 2)
# clip_video('F:\\剪辑素材库\\陈都灵\\18776860_da3-1-16.mp4', 'F:\\剪辑素材库\\陈都灵\\source.mp4', 660, 690)
    #     while True:
    #         count += 1
    #         success, frame = cap.read()
    #         if success:
    #             # 加了这句话之后识别精度大降
    #             # small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    #             rgb_frame = frame[:, :, ::-1]
    #             face_locations = face_recognition.face_locations(rgb_frame)
    #             face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    #             for face_encoding in face_encodings:
    #                 result = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
    #                 if result[0]:
    #                     print('write face true frame')
    #                     video_writer.write(frame)
    #                     num = 0
    #                     break
    #                 else:
    #                     print(count)
    #         else:
    #             break
    # cap.release()