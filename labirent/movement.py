# movement.py
from PyQt5.QtCore import Qt

STEP_SIZE = 1  # Hassas hareket 

def get_next_position(key, x, y):
    """Basılan tuşa (klavye veya buton) göre yeni (X, Y) koordinatını döndürür."""
    if key in (Qt.Key_W, Qt.Key_Up):
        return x, y - STEP_SIZE
    elif key in (Qt.Key_S, Qt.Key_Down):
        return x, y + STEP_SIZE
    elif key in (Qt.Key_A, Qt.Key_Left):
        return x - STEP_SIZE, y
    elif key in (Qt.Key_D, Qt.Key_Right):
        return x + STEP_SIZE, y
    
    return x, y  # Eğer geçersiz bir tuşa basıldıysa eski konumu koru