import eyed3
from eyed3.id3.frames import IMAGE_FID

audio = eyed3.load("R.mp3")
# with open("cover", "wb") as f:
#     f.write(audio.tag.images._fs[IMAGE_FID][0].image_data) # binary image data

audio_image = audio.tag.images
# print(audio_image.get('').image_data)
