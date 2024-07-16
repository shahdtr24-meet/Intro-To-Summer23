def create_youtube_video(title,description):
	hhh ={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return hhh

title=input("give me a title")
description=input("give me a description")
youtube_video=create_youtube_video(title,description)

def like(youtube_video):
	if "likes" in youtube_video: 
		youtube_video["likes"] += 1
		return youtube_video
def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] +=1 
		return youtube_video
username=input("what's the name of the user")
comment_text=input("what's the comment")
def add_comment(youtube_video ,username ,comment_text):
	youtube_video["comments"][username]=comment_text

title=input("give me a title")
description=input("give me a description")
new_vid = create_youtube_video(title,description)
for i in range (496): 
	like(new_vid)