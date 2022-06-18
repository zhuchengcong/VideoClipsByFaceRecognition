
# [VideoClipsByFaceRecognition](https://github.com/zhuchengcong/VideoClipsByFaceRecognition.git)

使用opencv-python,face_recognition识别视频中的人脸,进行剪辑，剪掉不想关的部分
> 目前剪辑出来的视频没有音频，后续使用moviepy实现音频同步

## :star: 技术栈

- python 3.6
- face_recognition
- opencv-python
- virtualenv

## 目录结构

```
├── code
│   ├── main // 主要代码
│   └── start_clip // 入口文件
```

## :rocket: 使用者指南

```bash
git clone https://github.com/zhuchengcong/VideoClipsByFaceRecognition.git

cd VideoClipsByFaceRecognition

virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
cd code
python start_clip.py -source source.mp4 -target target.mp4 -img chenduling.png -time 1
```

## :bulb: 需要注意的事情

- dlib包安装不上的话，需要自行去下载dlib-19.8.1-cp36-cp36m-win_amd64.whl离线安装



## :参数
- python start_clip.py 
* `-source` -源视频路径.
* `-target` - 输出视频路径.
* `-img` -需要识别剪辑的人脸图片.
* `-time` -人脸对比间隔时间单位秒，间隔时间越大，速度越快，出现人脸的视频前后视频时间越长.

