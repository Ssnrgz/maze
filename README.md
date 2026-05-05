# 🏴‍☠️ Hasır Şapka Labirent Macerası 
(One Piece Maze Game)

Python ve **PyQt5** kullanılarak geliştirilmiş, 10 farklı zorluk seviyesinden oluşan heyecan verici bir labirent oyunudur. Oyuncular, her bölümde farklı bir "Hasır Şapka" korsanını kontrol ederek kısıtlı süre içinde kendi hedefine (örneğin Luffy'yi ete, Zoro'yu kılıcına) ulaştırmaya çalışır.

## 🌟 Özellikler

* **10 Farklı Bölüm:** Kolaydan zora doğru giden, son bölümlerde aşırı dar yollara sahip zorlayıcı labirent tasarımları.
* **Dinamik Çarpışma Motoru (Hitbox):** Karakterlerin dar yollardan geçebilmesi için görsel boyutundan bağımsız, dinamik olarak hesaplanan merkez odaklı (2 piksel) kusursuz çarpışma algılama sistemi.
* **Otomatik Ölçeklendirme:** Tam ekran (`FullScreen`) çalışan ve ekran çözünürlüğü ne olursa olsun labirenti orantılı (`KeepAspectRatio`) bir şekilde büyüten profesyonel QGraphicsView altyapısı.
* **Zamanlayıcı ve Skor Kaydı:** Her bölüm için özel olarak belirlenmiş süre sınırları. Başarıyla tamamlanan bölümlerin süresi ve oyuncu adı `skorlar.txt` dosyasına otomatik olarak kaydedilir.
* **Akıcı Kontroller:** Klavye (W, A, S, D veya Yön Okları) ve arayüzdeki yön butonları ile kesintisiz hareket imkanı.

## 📂 Dosya Yapısı

Oyunun kaynak kodları modüler bir yapıda tasarlanmıştır (Clean Code):

* `main.py`: Oyunun ana döngüsünü, kullanıcı arayüzünü (UI) ve sahne (Scene) yönetimini barındırır.
* `mazes.py`: Labirent resimlerinin yüklenmesi ve duvara çarpma (Collision) mantığının işlendiği fizik motoru.
* `characters.py`: Karakterlerin boyutlarını, başlangıç/bitiş koordinatlarını ve süre limitlerini tutan veri dosyası.
* `movement.py`: Klavye girdilerini (W, A, S, D) x ve y eksenindeki piksel hareketlerine dönüştüren motor.
* **Klasörler:** `karakterler/` (Karakter ikonları), `hedefler/` (Hedef ikonları) ve `labirentler/` (Labirent haritaları).

## 🎮 Kontroller

* **İleri / Yukarı:** `W` veya `Yukarı Ok`
* **Geri / Aşağı:** `S` veya `Aşağı Ok`
* **Sol:** `A` veya `Sol Ok`
* **Sağ:** `D` veya `Sağ Ok`
* **Oyundan Çıkış:** `ESC`

## 🚀 Kurulum ve Çalıştırma

Oyunu kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

**1. Depoyu Klonlayın:**
```bash
git clone https://github.com/Ssnrgz/maze.git
cd labirent

2. Gerekli Kütüphaneleri Kurun:
Oyun PyQt5 kütüphanesine ihtiyaç duyar. Yüklemek için:
pip install PyQt5
(Linux/Ubuntu kullanıcıları pip3 install PyQt5 veya sudo apt install python3-pyqt5 komutlarını kullanabilirler.)

3. Oyunu Başlatın:
python3 main.py

---------------------------------------------------------------------------

### 🇬🇧 İngilizce README.md (English Version)

```markdown
# 🏴‍☠️ Straw Hat Maze Adventure (One Piece Maze Game)

Developed using Python and **PyQt5**, this is an exciting maze game consisting of 10 different difficulty levels. Players control a different "Straw Hat" pirate in each level, trying to navigate them to their specific target (e.g., Luffy to meat, Zoro to his swords) within a limited time.

## 🌟 Features

* **10 Different Levels:** Progressively challenging maze designs, featuring extremely narrow paths in the final stages.
* **Dynamic Collision Engine (Hitbox):** A flawless, center-focused (2-pixel) dynamic collision detection system that allows characters to pass through narrow paths regardless of their visual size.
* **Auto-Scaling:** Runs in `FullScreen` mode and utilizes a professional QGraphicsView infrastructure to scale the maze proportionally (`KeepAspectRatio`) regardless of screen resolution.
* **Timer and Score Tracking:** Custom time limits for each level. Successful completion times and player names are automatically saved to `skorlar.txt`.
* **Smooth Controls:** Seamless movement via keyboard (W, A, S, D or Arrow Keys) or on-screen directional buttons.

## 📂 File Structure

The source code is designed with a modular architecture (Clean Code):

* `main.py`: Handles the main game loop, User Interface (UI), and Scene management.
* `mazes.py`: The physics engine responsible for loading maze images and processing wall collisions.
* `characters.py`: Data file containing character sizes, start/end coordinates, and time limits.
* `movement.py`: The engine that translates keyboard inputs (W, A, S, D) into pixel movements on the x and y axes.
* **Folders:** `karakterler/` (Character icons), `hedefler/` (Target icons), and `labirentler/` (Maze maps).

## 🎮 Controls

* **Up:** `W` or `Up Arrow`
* **Down:** `S` or `Down Arrow`
* **Left:** `A` or `Left Arrow`
* **Right:** `D` or `Right Arrow`
* **Quit Game:** `ESC`

## 🚀 Installation and Usage

Follow these steps to run the game on your local machine.

**1. Clone the Repository:**
```bash
git clone https://github.com/Ssnrgz/maze.git
cd hasir-sapka-labirent

2. Install Required Libraries:
The game requires the PyQt5 library. To install it:
pip install PyQt5
(Linux/Ubuntu users can use the pip3 install PyQt5 or sudo apt install python3-pyqt5 commands.)

3. Launch the Game:
python3 main.py
