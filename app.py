import streamlit as st
from moviepy.editor import VideoFileClip, ImageClip, TextClip, CompositeVideoClip
import tempfile

def make_video(vf):
  video_clip=vf
  video_clip.write_videofile("test.mp4",codec='libx264',fps=24)
  #video_file=open("test.mp4",'rb')
    #video_bytes = output_file.read()
    #st.video(video_bytes) 
  video_bytes = video_clip.read()
  st.video(video_bytes)
    #st.video(final_clip)


f = st.file_uploader("Upload file",type=['mp4'])


  
  
if f is not None:
  #f.write('video.mp4')
  tfile = tempfile.NamedTemporaryFile(delete=False)
  tfile.write(f.read())
  st.video(f)




clicked = st.button('Create Video')
if(clicked is True):
    
  vf = VideoFileClip(tfile.name)
  #vf = VideoFileClip('video.mp4')
    
  make_video(vf)