# importing major libraries
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip,AudioFileClip
from moviepy.editor import *
import tempfile
from moviepy.video.fx.all import crop

def fonts():
    font={
        'Amiri' : 'Amiri-bold',
        'Anton':'fonts/Anton/Anton-Regular.ttf',
        'Lobster':'fonts/Anton/Lobster-Regular.ttf',
        'TiltWarp':'fonts/Anton/TiltWarp-Regular.ttf',
    }
    return font

def open_files_and_crop(video_file_name, duration=20):

    try:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(video_file_name.read())

        video_file = VideoFileClip(tfile.name, audio=False)

        # getting duration of video and check custom duration with video duration
        video_time = video_file.duration
        if duration <= video_time:
            duration = duration

        else :
            duration = video_time

        # now cut video and make it length as same as audio
        video_file = video_file.subclip(0, t_end=duration)
        
        (w, h) = video_file.size

        crop_width = h * 9/16

        x1, x2 = (w - crop_width)//2, (w+crop_width)//2
        y1, y2 = 0, h

        video_file = crop(video_file, x1=x1, y1=y1, x2=x2, y2=y2)

        video_file = video_file.resize((1080,1920))
        video_file.duration

        return video_file
    
    except :
        return "not working"


# function for getting video
def open_files(video_file_name, duration=20):

    try:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(video_file_name.read())

        video_file = VideoFileClip(tfile.name, audio=False)

        # getting duration of video and check custom duration with video duration
        video_time = video_file.duration
        if duration <= video_time:
            duration = duration

        else :
            duration = video_time

        # now cut video and make it length as same as audio
        video_file = video_file.subclip(0, t_end=duration)

        video_file = video_file.resize((1080,1920))

        return video_file
    
    except :
        return "not working"

    
# spliting text in multiple lines and adjusting time for video
def txt_split(quotation,video_file):
    
    quotation = quotation.split(",")

    for i in range(len(quotation)):
        quotation[i] = '"' + quotation[i] + '"'

    length_array = len(quotation)
    length_video = video_file.duration

    # for waiting to start video
    divide = length_array+length_video
    wait = length_video/divide

    # for duration
    due = length_video/length_array
    due = due-wait-0.15
    start_clip = due+wait
    
    return quotation,due,start_clip

# effects on text
def text_clip_center(text: str, color,fontSize, selected_font, duration: int, start_time: int = 0):
    key_list = fonts().get(selected_font)
    txt_clip = TextClip(text, fontsize=fontSize, color=color, font=key_list)
    txt_clip = txt_clip.set_position("center").set_duration(duration).set_start(start_time).crossfadein(.6).crossfadeout(.6)

    return txt_clip

# formating text on video
def appling_txt(quotes , fontSize, color, due, start_clip, selected_font):

    # this array is for storing clips of text
    text_clips = []

    # this loop is creating sections of clips
    for i in range(len(quotes)):
        lec_str = str(quotes[i])
        if i == 0:
            text_clip_one_cen = text_clip_center(lec_str,color=color,fontSize=fontSize, duration=due ,selected_font=selected_font)
            text_clips.append(text_clip_one_cen)
        
        # here we are chcking i is equal to i then simply adding with multiply start time with apparence of loop
        elif i == i:
            text_clip_cen = text_clip_center(lec_str,color=color,fontSize=fontSize, selected_font=selected_font, duration= due, start_time=start_clip*i)
            text_clips.append(text_clip_cen)

    return text_clips

# final step isto compose video
def compose(video_file,text_clips):

    # show clips is first store data in form of array
    show_clips = [video_file]

    for j in range(len(text_clips)):
        show_clips.append(text_clips[j])

    # all data store now compsing a a video
    result = CompositeVideoClip(
        show_clips)
    
    return result
    

