"""Bay sensor firmware for Faircurrent Energy"""

class BayFirmware:
    """Internal service for bay-firmware."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(BayFirmware().status())
