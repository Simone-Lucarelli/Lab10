from dataclasses import dataclass


@dataclass
class Border:
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int

    def __str__(self):
        return f"{self.state1no} - {self.state2no}"