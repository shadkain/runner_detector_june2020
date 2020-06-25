from .color import Color
from pkg.errors import Error


def colorFromString(colorStr: str) -> Color:
    if colorStr == 'black':
        return Color.black()
    if colorStr == 'white':
        return Color.white()
    if colorStr == 'red':
        return Color.red()
    if colorStr == 'green':
        return Color.green()
    if colorStr == 'blue':
        return Color.blue()
    if colorStr == 'yellow':
        return Color.yellow()
    if colorStr == 'magenta':
        return Color.magenta()
    if colorStr == 'cyan':
        return Color.cyan()
    
    raise Error(f'Unknown color "{colorStr}"')