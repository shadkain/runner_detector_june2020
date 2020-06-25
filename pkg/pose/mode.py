import enum
from pkg.errors import Error


class Mode(enum.Enum):
    COCO = 'COCO'
    MPI = 'MPI'

    def __json__(self):
        return self.value

    @property
    def lower(self) -> str:
        return self.value.lower()

    @staticmethod
    def fromString(modeStr: str):
        if modeStr.upper() == 'COCO':
            return Mode.COCO
        elif modeStr.upper() == 'MPI':
            return Mode.MPI
        else:
            raise Error(f'Unknown mode: "{modeStr.upper()}"')