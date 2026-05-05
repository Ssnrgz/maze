# characters.py

level_data = [
    
    # 1. Bölüm
    {"char": "karakterler/luffy.png", "target": "hedefler/et.png", "name": "Luffy", "time_limit": 90, 
    "start_x": 422, "start_y": 92, "target_x": 86, "target_y": 607, "size": 21},
    
    # 2. Bölüm (Koordinatları buldukça güncelleyebilirsin)
    {"char": "karakterler/zoro.png", "target": "hedefler/kilic.png", "name": "Zoro", "time_limit": 120, 
     "start_x": 26, "start_y": 81, "target_x": 457, "target_y": 596, "size": 21},
     
    # 3. Bölüm
    {"char": "karakterler/nami.png", "target": "hedefler/hazine.png", "name": "Nami", "time_limit": 120, 
     "start_x": 308, "start_y": 42, "target_x": 328, "target_y": 674, "size": 21},
     
    # 4. Bölüm
    {"char": "karakterler/usopp.png", "target": "hedefler/sapan.png", "name": "Usopp", "time_limit": 180, 
     "start_x": 111, "start_y": 72, "target_x": 116, "target_y": 624, "size": 21},
     
    # 5. Bölüm
    {"char": "karakterler/sanji.png", "target": "hedefler/yemek_seti.png", "name": "Sanji", "time_limit": 300, 
     "start_x": 57, "start_y": 110, "target_x": 405, "target_y": 632, "size": 21},
     
    # 6. Bölüm
    {"char": "karakterler/chopper.png", "target": "hedefler/pamuk_seker.png", "name": "Chopper", "time_limit": 360, 
    "start_x": 2, "start_y": 79, "target_x": 467, "target_y": 620, "size": 21},
     
    # 7. Bölüm
    {"char": "karakterler/robin.png", "target": "hedefler/poneglyph.png", "name": "Robin", "time_limit": 420, 
     "start_x": 234, "start_y": 154, "target_x": 246, "target_y": 565, "size": 21},
     
    # 8. Bölüm
    {"char": "karakterler/franky.png", "target": "hedefler/kola.png", "name": "Franky", "time_limit": 480, 
     "start_x": 1, "start_y": 309, "target_x": 483, "target_y": 256, "size": 8},
     
    # 9. Bölüm
    {"char": "karakterler/brook.png", "target": "hedefler/keman.png", "name": "Brook", "time_limit": 540, 
     "start_x": 109, "start_y": 75, "target_x": 440, "target_y": 647, "size": 10},
     
    # 10. Bölüm
    {"char": "karakterler/jinbe.png", "target": "hedefler/gunes_simgesi.png", "name": "Jinbe", "time_limit": 600, 
     "start_x": 187, "start_y": 82, "target_x": 244, "target_y": 638, "size": 10}
]

def get_character_data(level_index):
    """Bulunulan bölüme göre karakter, hedef, süre ve koordinat verisini döndürür."""
    if 0 <= level_index < len(level_data):
        return level_data[level_index]
    return None