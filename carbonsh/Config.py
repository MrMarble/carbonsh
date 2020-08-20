import urllib.parse

from .constants import themes, controls, languages, fonts, escales
from .utils import hex_to_rgb


def parse_bg(background) -> str:
    if background == '':
        return 'rgba(171, 184, 195, 1)'
    elif background[0] == '#' or '(' not in background:
        return f'rgba{hex_to_rgb(background) + (1,)}'


def int_to_px(number) -> str:
    return f'{number}px'


def int_to_percent(number) -> str:
    return f'{number}%'


class Config:
    _bg: str
    _t: str
    _wt: str
    _l: str
    _ds: bool
    _dsyoff: str
    _dsblur: str
    _wc: bool
    _ln: bool
    _fl: int
    _fm: str
    _fs: str
    _lh: str
    _es: str
    _wm: bool

    def __init__(self, language=languages.AUTO, theme=themes.SETI, font_family=fonts.HACK, font_size=14,
                 line_height=133, background_color='', controls=True, controls_style=controls.NONE, line_numbers=False,
                 first_line_number=1, drop_shadow=True, drop_shadow_offset=20, drop_shadow_blur=68, escale=escales.X2,
                 watermark=False):
        self._bg = parse_bg(background_color)
        self._t = theme
        self._wt = controls_style
        self._l = language
        self._ds = drop_shadow
        self._dsyoff = int_to_px(drop_shadow_offset)
        self._dsblur = int_to_px(drop_shadow_blur)
        self._wc = controls
        self._wa = True  # Auto-adjust with always true
        self._pv = int_to_px(56)  # Vertical padding always 56
        self._ph = int_to_px(56)  # Horizontal padding always 56
        self._ln = line_numbers
        self._fl = first_line_number
        self._fm = font_family
        self._fs = int_to_px(font_size)
        self._lh = int_to_percent(line_height)
        self._si = False  # Square image not working but required
        self._es = escale
        self._wm = watermark

    def __str__(self):
        result = []
        for key, value in vars(self).items():
            result.append(f'{key.lstrip("_")}={value if type(value) is not bool else str(value).lower()}')
        return urllib.parse.quote('&'.join(result), safe='()&=')
