import threading
from moviepy.editor import *
import time



def cut(path,i):
    video = VideoFileClip(path)
    video_begin = VideoFileClip('F:/西游记/begin.mp4')
    video_end = VideoFileClip('F:/西游记/end.mp4')
    middle = int(video.duration / 2)
    end_time = middle + 5
    begin_time = middle - 5
    clip_begin = video.subclip(0, end_time)
    clip_end = video.subclip(begin_time, video.duration)

    finalclip1 = concatenate_videoclips([video_begin, clip_begin,video_end])
    finalclip2 = concatenate_videoclips([video_begin, clip_end,video_end])
    finalclip1.write_videofile(f"F:/西游记/第{i}集_上.mp4")
    finalclip2.write_videofile(f"F:/西游记/第{i}集_下.mp4")
    video.close()
    video_begin.close()
    video_end.close()


if __name__ == '__main__':
    t1 = time.time()
    Thread = []
    for i in [24]:
        path = f"F:/西游记/西游记1986_{i}.mp4"
        Thread.append(threading.Thread(target=cut,args=(path,i)))
    for thread in Thread:
        thread.start()
    for thread in Thread:
        thread.join()
    t2 = time.time()
    print(t2-t1)