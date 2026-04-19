from typing import TypedDict


class InputFileError(Exception):
    pass


class Config(TypedDict, total=False):
    WIDTH: int
    HEIGHT: int
    ENTRY: tuple[int, int]
    EXIT: tuple[int, int]
    OUTPUT_FILE: str
    PERFECT: bool
    SEED: int
    ALGORITHM: str
    DISPLAY_MODE: str


def parse_bool(value: str) -> bool:
    if value == "True":
        return True
    if value == "False":
        return False
    raise InputFileError(f"invalid boolean value: {value}")


def parse_coords(value: str) -> tuple[int, int]:
    try:
        coords = tuple(value.strip("()").split(","))
        coords = (int(coords[0]), int(coords[1]))
        if len(coords) != 2:
            raise InputFileError(f"invalid coordinates: {value}")
        x, y = coords
    except ValueError as exc:
        raise InputFileError(f"invalid coordinates: {value}") from exc
    return (x, y)


def load_config(file_name: str) -> Config:
    raw: dict[str, str] = {}
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    raise InputFileError(f"line {line_number}: missing '='")
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()
                raw[key] = value
    except FileNotFoundError as exc:
        raise InputFileError(f"file not found: {file_name}") from exc
    required_keys = {
        "WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"
        }
    missing = required_keys - raw.keys()
    if missing:
        raise InputFileError(
            f"input file is missing mandatory parameters: "
            f"{', '.join(sorted(missing))}"
        )
    try:
        width = int(raw["WIDTH"])
        height = int(raw["HEIGHT"])
        exit_ = parse_coords(raw["EXIT"])
        entry = parse_coords(raw["ENTRY"])
        output_file = raw["OUTPUT_FILE"]
        perfect = parse_bool(raw["PERFECT"])
        seed: int | None = None
        if "SEED" in raw:
            seed = int(raw["SEED"])
        algorithm: str | None = raw.get("ALGORITHM")
        display_mode: str | None = raw.get("DISPLAY_MODE")
    except ValueError as exc:
        raise InputFileError("WIDTH and HEIGHT must be integers") from exc
    if width <= 0 or height <= 0:
        print(width)
        raise InputFileError("WIDTH and HEIGHT must be positive")
    if entry == exit_:
        raise InputFileError("ENTRY and EXIT must be different")
    if not (0 <= entry[0] < width and 0 <= entry[1] < height):
        raise InputFileError("ENTRY is out of maze bounds")
    if not (0 <= exit_[0] < width and 0 <= exit_[1] < height):
        raise InputFileError("EXIT is out of maze bounds")
    config: Config = {
        "WIDTH": width,
        "HEIGHT": height,
        "ENTRY": entry,
        "EXIT": exit_,
        "OUTPUT_FILE": output_file,
        "PERFECT": perfect,
    }
    if seed is not None:
        config["SEED"] = seed
    if algorithm is not None:
        config["ALGORITHM"] = algorithm
    if display_mode is not None:
        config["DISPLAY_MODE"] = display_mode
    return config
