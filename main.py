import sys
import os


class Varimarkable:
    """
    - Set global switch
    - Set dye begin and end point
    - Set single line color
    - Get color tag and reset tag
    """

    SWITCH = True

    RESET = '\x1b[0m'

    FG = '38'
    BG = '48'

    @staticmethod
    def hex_to_rgb(color: str) -> tuple:
        """
        #ffffff -> (255, 255, 255)
        """
        color = color.strip('#') if color.startswith('#') else color
        if len(color) != 6:
            raise ValueError('Hex color tag length must equals 6 without "#".')
        return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)

    @classmethod
    def _format(cls, fg, bg):
        fg_tag = f'\x1b[{cls.FG};2;{fg[0]};{fg[1]};{fg[2]}m' if fg else str()
        bg_tag = f'\x1b[{cls.BG};2;{bg[0]};{bg[1]};{bg[2]}m' if bg else str()
        return f'{fg_tag}{bg_tag}'

    @staticmethod
    def _is_hex(data):
        if not isinstance(data, str):
            return False
        if not data.startswith('#'):
            return False
        if len(data) != 7:
            return False
        for character in data.strip('#').upper():
            if character.isdigit():
                continue
            if character in ['A', 'B', 'C', 'D', 'E', 'F']:
                continue
            return False
        return True

    @classmethod
    def get_tag(cls, fg=None, bg=None):
        if not cls.SWITCH:
            return str()
        if fg is None and bg is None:
            return cls.RESET
        fg_rgb = cls.hex_to_rgb(fg) if cls._is_hex(fg) else fg
        bg_rgb = cls.hex_to_rgb(bg) if cls._is_hex(bg) else bg
        return cls._format(fg=fg_rgb, bg=bg_rgb)

    @classmethod
    def dye(cls, line, fg=None, bg=None):
        tag = cls.get_tag(fg=fg, bg=bg)
        reset = cls.RESET if cls.SWITCH else str()
        print(f'{tag}{line}{reset}')

    @classmethod
    def set_color(cls, fg=None, bg=None):
        tag = cls.get_tag(fg=fg, bg=bg)
        print(tag)

    @classmethod
    def rest_color(cls):
        if not cls.SWITCH:
            return None
        print(cls.RESET)


if __name__ == '__main__':
#     Varimarkable.SWITCH = False
    Varimarkable.dye(line='hello', fg='#32efef', bg=None)
    Varimarkable.set_color(fg='#ad2e2e')
    print('Hey, how have you been?')
    print(98)
    Varimarkable.rest_color()
    print('reseted')
