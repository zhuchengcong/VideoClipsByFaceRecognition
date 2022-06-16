# python test.py -img 'xxxx.jpg' -video 'xxx.mp4'
# 运行带参数的python脚本，接受参数的方法

import sys

img_path = None
video_path = None

for i in range(len(sys.argv)):
    if sys.argv[i] == '-img':
        img_path = sys.argv[i + 1]
    if sys.argv[i] == '-video':
        video_path = sys.argv[i + 1]

print('参数img='+img_path)
print('参数video='+video_path)
