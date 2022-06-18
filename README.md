
# [VideoClipsByFaceRecognition](https://github.com/zhuchengcong/VideoClipsByFaceRecognition.git)

更具人脸图片自动识别人脸剪辑视频，剪掉不想关的部分，自动砍柴。
> 目前剪辑出来的视频没有音频，后续使用moviepy实现音频同步

## :star: 特性

- python 3.6
- face_recognition
- opencv
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





