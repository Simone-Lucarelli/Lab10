from dataclasses import dataclass


@dataclass
class Country:
    ccode: int
    stateAbb: str
    stateName: str

    def __str__(self):
        return f"{self.stateAbb} {self.stateName}"

    def __repr__(self):
        return f"{self.stateAbb} {self.stateName}"

    def __hash__(self):
        return hash(self.ccode)