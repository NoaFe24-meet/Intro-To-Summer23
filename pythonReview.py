def create_youtube_video(title, description):
	youtube_video={"Title": "title", "Description": "description", "like":0, "dislike":0, "comments":{}}
	return youtube_video

 def like(youtube_video):
 	if "like" in youtube_video
 		youtube_video["like"] +=1 
 	return youtube_video	
def dislike(youtube_video):
 	if "dislike" in youtube_video
 		youtube_video["dislike"] +=1 
 	return youtube_video

def add_comment(youtube_video, username, comment_text):
	youtube_video{'comment'}{username} = comment_text
	return youtube_video

youtube_video= create_youtube_video("Eden dancing", "Eden is dancing lovely")	
print(youtube_video)

youtube_video=like(youtube_video)
print(youtube_video)

youtube_video=dislike(youtube_video)
print(youtube_video)

youtube_video= add_comment(youtube_video,"noa1","She is so gooddddd")
youtube_video= add_comment(youtube_video,"danielle3","not good...")
print(youtube_video)


