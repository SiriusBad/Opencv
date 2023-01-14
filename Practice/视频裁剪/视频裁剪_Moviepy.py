from moviepy.editor import *
import time
video = VideoFileClip('H:/西游记/西游记1986_2425.mkv')
middle = int(video.duration / 2)
end_time = middle + 5
begin_time = middle - 5
clip_begin = video.subclip(0, 170)
clip_end = video.subclip(video.duration - 70, video.duration)
clip1 = video.subclip(0,end_time)
clip2 = video.subclip(begin_time,video.duration)

finalclip1 = concatenate_videoclips([clip1,clip_end])
finalclip2 = concatenate_videoclips([clip_begin,clip2])
finalclip1.write_videofile("第一集上.mp4")
finalclip2.write_videofile("第一集下.mp4")
