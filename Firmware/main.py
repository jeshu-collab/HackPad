code = """import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

# Initialize the keyboard
keyboard = KMKKeyboard()

# Add standard modules
keyboard.modules.append(Layers())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# --- SWITCH MATRIX SETUP ---
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- ENCODER SETUP ---
encoder_handler.pins = ((board.GP26, board.GP27, board.GP28, False),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]

# --- RGB LED SETUP (SK6812MINI-E) ---
# Replace board.GP29 with your actual LED data pin from KiCad
rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=9, # Number of LEDs in your matrix
    val_limit=100, # Brightness limit
    hue_default=0,
    sat_default=255,
    val_default=100
)
keyboard.extensions.append(rgb)

# --- OLED DISPLAY SETUP (128x32) ---
# Replace GP7 (SDA) and GP6 (SCL) with your actual I2C pins
i2c_bus = busio.I2C(board.GP7, board.GP6)
display_driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Hackpad Ready!', x=0, y=0, y_anchor='M'),
    ],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    return_to_base=True
)
keyboard.extensions.append(display)

# --- KEYMAP ---
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9
    ]
]

if __name__ == '__main__':
    keyboard.go()
"""

with open("main.py", "w") as f:
    f.write(code)

print("Hello")