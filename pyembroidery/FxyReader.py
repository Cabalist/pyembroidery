from .EmbConstant import *
from .ReadHelper import read_int_8, signed8


def read(f, out, settings=None):
    f.seek(0x100)  # GT format with header
    while True:
        stitch_type = STITCH
        b1 = read_int_8(f)
        b2 = read_int_8(f)
        command_byte = read_int_8(f)
        if command_byte is None:
            break
        b1 = signed8(b1)
        b2 = signed8(b2)
        if command_byte == 0x91:
            break
        if (command_byte & 0x01) == 0x01:
            stitch_type = TRIM
        if (command_byte & 0x02) == 0x02:
            stitch_type = COLOR_CHANGE
        if (command_byte & 0x20) == 0x20:
            b1 = -b1
        if (command_byte & 0x40) == 0x40:
            b2 = -b2
        out.add_stitch_relative(stitch_type, b2, b1)
    out.end()