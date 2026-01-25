import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Tap, Delay

keyboard = KMKKeyboard()

Keyboard.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4)
Keyboard.row_pins = (board.GP5, board.GP6, board.GP7, board.GP8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
def open_app(app_name):
    return [
        Tap(KC.LGUI(KC.R)),
        Delay(10),
        tap(app_name)
        Tap(KC.ENTER),
        Delay(1000)
    ]
macros = Macros()
keyboard.modules.append(macros)

Kids_class = kc.Macro(
    open_app("chrome"),
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "youtube.com",
    tap(kc.enter),
    delay(1000),
    for i in range(4):
        tap(kc.tab),
    "Dr Binocs",
    tap(kc.enter),
    tap(kc.lctl(kc.t))
    "ide.mblock.cc"
    tap(kc.enter)
)

Spike_Prime = kc.Macro(
    open_app("C:\\Users\\nagar\\OneDrive\\Desktop\\SPIKE - Shortcut.lnk"),
    open_app("chrome"),
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "meet.google.com/mcc-ednj-mzv"
    tap(kc.enter),
    delay(1000),
)

Wedo 2_0 = kc.Macro(
    open_app("Wedo"),
    open_app("chrome"),
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "youtube.com",
    tap(kc.enter),
    delay(1000),
    for i in range(4):
        tap(kc.tab),
    "dr binocs",
    tap(kc.enter),
)
    
Closeallapps = kc.Macro(
    press(kc.lalt)
    tap(kc.f4),
    delay(500),
    tap(kc.f4),
    delay(500),
    release(kc.lalt)
)

Science_mode = kc.Macro(
    open_app("chrome"),
    for i in range(10):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    for i in range(10):
        tap(kc.tab),
    tap(kc.enter),
    delay(1000),
    open_app("spotify"),
)

Physics_mode = kc.Macro(
    open_app("chrome"),
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "https://brightspace.carleton.ca/d2l/login?noRedirect=1",
    tap(kc.enter),
    delay(1000),
    for i in range(2):
        tap(kc.tab),
    tap(kc.enter),
    delay(1000),
    for i in range(11):
        tap(kc.tab),
    tap(kc.enter),
    delay(1000),
    open_app("spotify"),
)

Fusion360 = kc.Macro(
    open_app("C:\\Users\\nagar\\OneDrive\\Desktop\\Autodesk Fusion.lnk"),
    open_app("Chrome"),
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "hackclub.com",
    tap(kc.enter),
    delay(1000),
    open_app("spotify"),
)

close_other_tabs = kc.Macro(
    tap(kc.app),
    delay(100),
    tap(kc.o),
    tap(kc.enter)
)

kicad_open=kc.Macro(
    open_app("C:\\Users\\nagar\\OneDrive\\Desktop\\KiCad.lnk")
    open_app("spotify"),
    open_app("chrome"),
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "hackclub.com",
    tap(kc.enter),
    delay(1000)
)

vs_code_open=kc.Macro(
    open_app("C:\\Users\\nagar\\OneDrive\\Desktop\\Visual Studio Code.lnk")
    open_app("spotify"),
    open_app("chrome"),
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "hackclub.com",
    tap(kc.enter),
    delay(1000)
)

main = kc.Macro(
    open_app("chrome")
    for i in range(13):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "chat.openai.com",
    tap(kc.enter),
    open_app("spotify"),
    open_app("chrome"),
    for i in range(10):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "classroom.google.com",
    tap(kc.enter),
    open_app("C:\\Users\\nagar\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")

)
classroom = kc.Macro(
    open_app("chrome"),
    for i in range(10):
        tap(kc.tab),
    tap(kc.enter),
    tap(kc.lctl(kc.t)),
    "classroom.google.com",
    tap(kc.enter),
    delay(1000),
    open_app("spotify"),
)

SHUTDOWN_PC = KC.MACRO(
    Tap(KC.LGUI(KC.R)),
    Delay(200),
    "shutdown -s -t 00",
    Tap(KC.ENT)
)
Copy=kc.Macro(
    tap(kc.lctl(kc.c))
)

Paste=kc.Macro(
    tap(kc.lctl(kc.v))
)

reverse = kc.Macro(
    tap(kc.lctl(kc.z))
)
forward = kc.Macro(
    tap(kc.lctl(kc.y))
)
keyboard.keymap = [
    [    
        Closeallapps, Kids_class, Spike_Prime, Wedo 2_0,
        close_other_tabs, classroom, Physics_mode, Fusion360,   
        SHUTDOWN_PC, kicad_open, vs_code_open, main,   
        forward, reverse, Copy, Paste  
    ]
]
