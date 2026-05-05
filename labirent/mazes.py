# mazes.py
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt

maze_images = [
    "labirentler/labirent_1.png",
    "labirentler/labirent_2.png",
    "labirentler/labirent_3.png",
    "labirentler/labirent_4.png",
    "labirentler/labirent_5.png",
    "labirentler/labirent_6.png",
    "labirentler/labirent_7.png",
    "labirentler/labirent_8.png",
    "labirentler/labirent_9.png",
    "labirentler/labirent_10.png"
]

maze_qimages = {}

def get_maze_image(level_index):
    if 0 <= level_index < len(maze_images):
        return maze_images[level_index]
    return None

def get_maze_qimage(level_index, width=500, height=750):
    if level_index not in maze_qimages:
        img_path = get_maze_image(level_index)
        if img_path:
            image = QImage(img_path).convertToFormat(QImage.Format_RGB32)
            image = image.scaled(width, height, Qt.IgnoreAspectRatio, Qt.FastTransformation)
            maze_qimages[level_index] = image
    return maze_qimages.get(level_index)

def is_wall_collision(level_index, new_x, new_y, char_width=21, char_height=21):
    image = get_maze_qimage(level_index)
    if image is None:
        return False
    
    # OYUNU KURTARACAK SİHİRLİ DOKUNUŞ: Çarpışma alanını sadece 2 piksel yapıyoruz!
    # Karakterin boyutu (10 veya 21) ne olursa olsun, sadece merkez noktası duvara değerse duracak.
    hitbox_size = 2 
    
    margin_x = (char_width - hitbox_size) // 2
    margin_y = (char_height - hitbox_size) // 2
    
    start_x = int(new_x + margin_x)
    end_x = int(new_x + char_width - margin_x)
    start_y = int(new_y + margin_y)
    end_y = int(new_y + char_height - margin_y)

    if start_x < 0 or start_y < 0 or end_x >= image.width() or end_y >= image.height():
        return True 

    points = []
    for x in range(start_x, end_x + 1):
        points.append((x, start_y)) 
        points.append((x, end_y))   
    for y in range(start_y, end_y + 1):
        points.append((start_x, y)) 
        points.append((end_x, y))   

    for cx, cy in points:
        pixel_color = image.pixelColor(cx, cy)
        # Beyaz olmayan her şeyi duvar say
        if pixel_color.red() < 220 or pixel_color.green() < 220 or pixel_color.blue() < 220:
            return True 

    return False