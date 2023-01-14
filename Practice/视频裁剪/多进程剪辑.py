from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
from moviepy.editor import *

def cut_none(path,i):
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

def cut_no_tail(path,i):
    video = VideoFileClip(path)
    video_begin = VideoFileClip('F:/西游记/begin.mp4')
    video_end = VideoFileClip('F:/西游记/end.mp4')
    middle = int(video.duration / 2)
    end_time = middle + 5
    begin_time = middle - 5
    clip_begin = video.subclip(0, end_time)
    clip_end = video.subclip(begin_time, video.duration)

    finalclip1 = concatenate_videoclips([clip_begin,video_end])
    finalclip2 = concatenate_videoclips([video_begin, clip_end,video_end])
    finalclip1.write_videofile(f"F:/西游记/第{i}集_上.mp4")
    finalclip2.write_videofile(f"F:/西游记/第{i}集_下.mp4")
    video.close()
    video_begin.close()
    video_end.close()

def cut_no_head(path,i):
    video = VideoFileClip(path)
    video_begin = VideoFileClip('F:/西游记/begin.mp4')
    video_end = VideoFileClip('F:/西游记/end.mp4')
    middle = int(video.duration / 2)
    end_time = middle + 5
    begin_time = middle - 5
    clip_begin = video.subclip(0, end_time)
    clip_end = video.subclip(begin_time, video.duration)

    finalclip1 = concatenate_videoclips([video_begin, clip_begin,video_end])
    finalclip2 = concatenate_videoclips([video_begin, clip_end])
    finalclip1.write_videofile(f"F:/西游记/第{i}集_上.mp4")
    finalclip2.write_videofile(f"F:/西游记/第{i}集_下.mp4")
    video.close()
    video_begin.close()
    video_end.close()

if __name__ == '__main__':
    t1 = time.time()
    path = []
    Thread = []
    list = [13,17,21]
    for i in list:
        p = 'F:/西游记/西游记1986_' + str(i) + '.mkv'
        path.append(p)
    p = 'F:/西游记/西游记1986_' + str(25) + '.mp4'
    path.append(p)
    list.append(25)
    # with ProcessPoolExecutor() as pool:      #多进程
    #     pool.map(cut_no_tail, path, list)
    with ThreadPoolExecutor() as pool:
        pool.map(cut_no_head, path, list)    #多线程
    t2 = time.time()
    print(t2 - t1)
