import streamlit as st
import streamlit_nested_layout
from moviepy.editor import *
import main
import tempfile

color = [
    "white",
    "AliceBlue",
    "AntiqueWhite"
    "aqua",
    "aquamarine",
    "aquamarine1",
    "bisque4",
    "black",
    "BlanchedAlmond",
    "blue",
    "blue1",
]

st.set_page_config(page_title="First app",page_icon='tada',layout='wide')

with st.container():
    st.subheader('Hi : Welcome to Our Site')
    st.title('Here You Can Edit Video')
    st.write('---')

    col = st.columns(2)
    with col[0]:
        img_text = st.text_area('Text on image')

    with col[1]:
        uploaded_file = st.file_uploader('Upload a video', type=['mov', 'mp4'])

    middle_col = st.columns([2,5,2])
with middle_col[1]:

    if uploaded_file is not None and img_text != "":

        # displaying video file
        st.video(uploaded_file)
        
        inner_col = st.columns(3)
        with inner_col[0]:
            edit_option = st.selectbox(
                'Select Edit option',["Edit Only","Crop and Edit"]
            )
        
        with inner_col[1]:
            font_option = st.selectbox(
                'Select Font Style',main.fonts().keys()
            )
        
        with inner_col[2]:
            font_color = st.selectbox(
                'Select Font Color',color
            )

        font_size = st.slider('Adjust Font Size', 40, 100, 60)
        
        edit_vid_btn = st.button('Edit Video')

        if edit_vid_btn:

            ## Save to temp file ##
            if edit_option == "Edit Only":
                clip = main.open_files(uploaded_file)
            
            elif edit_option == "Crop and Edit":
                clip = main.open_files_and_crop(uploaded_file)


            quotes,due,start_clip = main.txt_split(img_text,clip)

            # applying edited text
            text_clips = main.appling_txt(quotes, fontSize=font_size, color=font_color, due=due, start_clip=start_clip, selected_font=font_option)

            
            # final step isto compose video
            edited_clip = main.compose(clip,text_clips)  

            with st.spinner("Please Wait Video is Processing"):
                edited_clip.write_videofile("edited.mp4", fps=30)
            st.success("Video is Done")
            
            st.balloons()

            file = open('edited.mp4', 'rb') 
            btn = st.download_button(
                label='Download Video',
                data=file,
                file_name="edited.mp4"
            )
                


