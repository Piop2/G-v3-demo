import io

import eyed3
import pygame

audio = eyed3.load("test/eyed3 test/R.mp3")
audio_album_image_data = audio.tag.images.get("").image_data
origin_album_image = pygame.image.load(io.BytesIO(audio_album_image_data))

# with open("cover.jpg", "rb") as f:
#     origin_album_image = pygame.image.load(io.BytesIO(f.read()))

album_image = pygame.transform.scale(origin_album_image, (500, 500))

print(audio.tag.track_num.count)

# pygame.init()
# display = pygame.display.set_mode((500, 500))
# clock = pygame.Clock()
# pygame.display.set_caption("render album cover")

# running = True
# while running:
#     clock.tick(60)

#     display.blit(album_image, (0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.update()

# pygame.quit()
