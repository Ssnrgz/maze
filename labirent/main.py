# main.py
import sys
import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QInputDialog, QGridLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QRectF, Qt
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem

import characters
import mazes
import movement

class OnePieceMazeGame(QMainWindow):
    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.setWindowTitle("Hasır Şapka Labirent Macerası")
        self.setMinimumSize(900, 700) 

        self.setStyleSheet("QLabel { font-size: 16px; font-weight: bold;} QPushButton { font-size: 14px; font-weight: bold; }")

        self.current_level = 0
        self.time_elapsed = 0
        self.time_limit = 0
        
        self.char_size = 21
        self.target_size = 21
        
        self.char_x = 0
        self.char_y = 0

        self.init_ui()
        self.load_level()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout(self.central_widget)

        self.info_layout = QHBoxLayout()
        self.player_label = QLabel(f"Kaptan: {self.player_name}")
        self.level_label = QLabel("Bölüm: 1")
        self.timer_label = QLabel("Süre: 0 / 0 sn")
        
        self.level_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.info_layout.addWidget(self.player_label)
        self.info_layout.addWidget(self.level_label)
        self.info_layout.addWidget(self.timer_label)
        self.main_layout.addLayout(self.info_layout)
        self.main_layout.addSpacing(10)

        self.content_layout = QHBoxLayout()

        self.maze_layout = QVBoxLayout()
        
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setStyleSheet("background: transparent; border: 2px solid #555;")
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.maze_item = QGraphicsPixmapItem()
        self.scene.addItem(self.maze_item)

        self.target_item = QGraphicsPixmapItem()
        self.scene.addItem(self.target_item)

        self.char_item = QGraphicsPixmapItem()
        self.scene.addItem(self.char_item)

        self.maze_layout.addWidget(self.view, stretch=1)

        # Koordinat yazısı kaldırıldı, sadece oyundan çıkış uyarısı eklendi
        self.exit_hint_label = QLabel("Oyundan Çıkış: ESC")
        self.exit_hint_label.setAlignment(Qt.AlignCenter)
        self.exit_hint_label.setStyleSheet("color: gray; font-size: 14px; font-weight: normal;")
        self.maze_layout.addWidget(self.exit_hint_label)

        self.content_layout.addLayout(self.maze_layout, stretch=4) 
        
        self.controls_layout = QGridLayout()
        self.controls_layout.setSpacing(5) 
        
        self.btn_up = QPushButton("Yukarı (W)")
        self.btn_down = QPushButton("Aşağı (S)")
        self.btn_left = QPushButton("Sol (A)")
        self.btn_right = QPushButton("Sağ (D)")

        self.btn_up.setFocusPolicy(Qt.NoFocus)
        self.btn_down.setFocusPolicy(Qt.NoFocus)
        self.btn_left.setFocusPolicy(Qt.NoFocus)
        self.btn_right.setFocusPolicy(Qt.NoFocus)

        btn_width, btn_height = 90, 60
        self.btn_up.setFixedSize(btn_width, btn_height)
        self.btn_down.setFixedSize(btn_width, btn_height)
        self.btn_left.setFixedSize(btn_width, btn_height)
        self.btn_right.setFixedSize(btn_width, btn_height)

        self.btn_up.clicked.connect(lambda _: self.handle_movement(Qt.Key_W))
        self.btn_down.clicked.connect(lambda _: self.handle_movement(Qt.Key_S))
        self.btn_left.clicked.connect(lambda _: self.handle_movement(Qt.Key_A))
        self.btn_right.clicked.connect(lambda _: self.handle_movement(Qt.Key_D))

        self.controls_layout.addWidget(self.btn_up, 0, 1)
        self.controls_layout.addWidget(self.btn_left, 1, 0)
        self.controls_layout.addWidget(self.btn_down, 1, 1)
        self.controls_layout.addWidget(self.btn_right, 1, 2)

        self.right_panel = QVBoxLayout()
        self.right_panel.addStretch()
        self.right_panel.addLayout(self.controls_layout)
        self.right_panel.addStretch()

        self.content_layout.addLayout(self.right_panel, stretch=1)

        self.main_layout.addLayout(self.content_layout, stretch=1)

    def resizeEvent(self, event):
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        super().resizeEvent(event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape:
            self.close()
        self.handle_movement(key)

    def handle_movement(self, key):
        new_x, new_y = movement.get_next_position(key, self.char_x, self.char_y)
        if new_x != self.char_x or new_y != self.char_y:
            self.try_move(new_x, new_y)

    def try_move(self, new_x, new_y):
        step_x = 1 if new_x > self.char_x else -1 if new_x < self.char_x else 0
        step_y = 1 if new_y > self.char_y else -1 if new_y < self.char_y else 0
        
        temp_x, temp_y = self.char_x, self.char_y
        distance = max(abs(new_x - self.char_x), abs(new_y - self.char_y))
        
        for _ in range(distance):
            next_x = temp_x + step_x
            next_y = temp_y + step_y
            if mazes.is_wall_collision(self.current_level, next_x, next_y, self.char_size, self.char_size):
                break 
            temp_x = next_x
            temp_y = next_y
            
        self.char_x = temp_x
        self.char_y = temp_y
        self.update_char_position()
        self.check_target_reached()

    def load_level(self):
        char_data = characters.get_character_data(self.current_level)
        original_qimage = mazes.get_maze_qimage(self.current_level)

        if not char_data or not original_qimage:
            self.timer.stop()
            QMessageBox.information(self, "Tebrikler!", f"İnanılmazsın {self.player_name}! Tüm bölümleri tamamladın!")
            self.close()
            return

        self.time_limit = char_data["time_limit"]
        self.level_label.setText(f"Bölüm: {self.current_level + 1} - {char_data['name']}")
        self.timer_label.setText(f"Süre: 0 / {self.time_limit} sn")
        
        self.char_size = char_data.get("size", 24)
        self.target_size = self.char_size
        
        self.scene.setSceneRect(0, 0, original_qimage.width(), original_qimage.height())

        self.maze_item.setPixmap(QPixmap.fromImage(original_qimage))
        self.char_item.setPixmap(QPixmap(char_data["char"]).scaled(self.char_size, self.char_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        self.target_item.setPixmap(QPixmap(char_data["target"]).scaled(self.target_size, self.target_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))

        self.char_x = char_data["start_x"]
        self.char_y = char_data["start_y"]
        self.target_item.setPos(char_data["target_x"], char_data["target_y"])
        
        self.update_char_position()
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def update_timer(self):
        self.time_elapsed += 1
        self.timer_label.setText(f"Süre: {self.time_elapsed} / {self.time_limit} sn")

        if self.time_elapsed >= self.time_limit:
            self.timer.stop()
            QMessageBox.critical(self, "Süre Doldu!", f"SÜRE DOLDU!\nBelirlenen {self.time_limit} saniyeyi aştın ve kaybettin. Bölüm yeniden başlıyor!")
            self.restart_level()

    def restart_level(self):
        self.time_elapsed = 0
        self.timer.start()
        self.load_level()

    def check_target_reached(self):
        char_rect = QRectF(self.char_x, self.char_y, self.char_size, self.char_size)
        target_rect = QRectF(self.target_item.x(), self.target_item.y(), self.target_size, self.target_size)

        if char_rect.intersects(target_rect):
            self.level_passed()

    def update_char_position(self):
        self.char_item.setPos(self.char_x, self.char_y)

    def save_score(self):
        char_name = characters.get_character_data(self.current_level)["name"]
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("skorlar.txt", "a", encoding="utf-8") as file:
            record = f"[{date_str}] Oyuncu: {self.player_name} | Bölüm: {self.current_level + 1} | Karakter: {char_name} | Süre: {self.time_elapsed} saniye\n"
            file.write(record)

    def level_passed(self):
        self.timer.stop()
        self.save_score()
        char_name = characters.get_character_data(self.current_level)["name"]
        QMessageBox.information(self, "Başarılı!", f"Süper! {char_name} hedefine ulaştı!\nÇözüm Süren: {self.time_elapsed} saniye.\nSkorun kaydedildi.")
        self.current_level += 1
        self.time_elapsed = 0
        self.timer.start()
        self.load_level()

def get_player_name():
    app = QApplication(sys.argv)
    text, ok = QInputDialog.getText(None, 'Oyuncu Girişi', 'Maceraya başlamak için adını gir:')
    if ok and text:
        return text, app
    else:
        sys.exit()

if __name__ == '__main__':
    player_name, app = get_player_name()
    window = OnePieceMazeGame(player_name)
    window.showFullScreen() 
    sys.exit(app.exec_())