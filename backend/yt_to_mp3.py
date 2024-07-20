from pytube import YouTube 
import os 

def yt_to_mp3(link):

    # url input from user 
    yt = YouTube(link) 
    
    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 
    
    # Change this to configure downloadable link in production
    destination = '.'
  
    # download the file 
    out_file = video.download(output_path=destination) 
  
    # save the file 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    
    return True


print(yt_to_mp3("https://www.youtube.com/watch?v=F5TMU6916U8"))