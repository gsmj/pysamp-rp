def color_to_hex(color: int) -> str:
    return f'{{{hex(color)[2:8].upper()}}}'


WHITE: int = 0xFFFFFFFF
DARK_GREEN: int = 0x34C924AA
HIGHLIGHT: int = 0xD53032AA
RED: int = 0xD2042DAA
MASK: int = 0x22222200
DEP: int = 0xFF8282AA
WANTED: int = 0xBC2C2CFF
YELLOW: int = 0xFFFF00AA
ACTION: int = 0xC2A2DAFF
GOV: int = 0x006699FF

# HEX colors

WHITE_HEX = color_to_hex(WHITE)
DARK_GREEN_HEX = color_to_hex(DARK_GREEN)
HIGHLIGHT_HEX = color_to_hex(HIGHLIGHT)
RED_HEX = color_to_hex(RED)
DIALOG_HEX = '{A9C4E4}'
DEP_HEX = color_to_hex(DEP)
WANTED_HEX = color_to_hex(WANTED)
YELLOW_HEX = color_to_hex(YELLOW)
ACTION_HEX = color_to_hex(ACTION)
GOV_HEX = color_to_hex(GOV)
