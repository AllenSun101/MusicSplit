from pytube import YouTube 
import os 

def convert_yt_to_mp3(link):

    # url input from user 
    yt = YouTube(link) 
    
    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 
    
    # Change this to configure downloadable link in production
    destination = './media'
  
    # download the file 
    out_file = video.download(output_path=destination) 
  
    # save the file 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 

    relative_path = os.path.relpath(new_file, "backend")
    relative_path = relative_path.replace('\\', '/')

    return relative_path


# print(convert_yt_to_mp3("https://www.youtube.com/watch?v=C-z-IckrQK8"))