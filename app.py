import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="광고 킬러 MP3", page_icon="🎵")
st.title("🎵 유튜브 MP3 하나만 쏙! (광고 제거)")

# 입력창
url = st.text_input("유튜브 링크 붙여넣기 👇")

if st.button("변환하기 🚀"):
    if url:
        with st.spinner("딱 하나만 골라내는 중..."):
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}],
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': True,  # ✨ 핵심! 재생목록 무시하고 딱 1개만 받기
                'quiet': True,
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    file_name = f"{ydl.prepare_filename(info).rsplit('.', 1)[0]}.mp3"
                    
                st.success(f"변환 끝! : {info.get('title')}")
                
                with open(file_name, "rb") as file:
                    st.download_button("💾 내 폰/컴퓨터에 저장", file, file_name=file_name, mime="audio/mpeg")
                    
            except Exception as e:
                st.error(f"에러 발생: {e}")