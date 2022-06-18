# python start_clip.py -source source.mp4 -target target.mp4 -img chenduling.png -time 1
# 运行带参数的python脚本，接受参数的方法
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(os.path.dirname(BASE_DIR))
sys.path.insert(0, str(BASE_DIR))

from code.main import clip_video_by_face

source_video_path = None
target_video_path = None
img_path = None
detection_time = 1

for i in range(len(sys.argv)):
    if sys.argv[i] == '-source':
        source_video_path = sys.argv[i + 1]
    if sys.argv[i] == '-target':
        target_video_path = sys.argv[i + 1]
    if sys.argv[i] == '-img':
        img_path = sys.argv[i + 1]
    if sys.argv[i] == '-time':
        detection_time = int(sys.argv[i + 1])

clip_video_by_face(source_video_path, target_video_path, img_path, detection_time)
