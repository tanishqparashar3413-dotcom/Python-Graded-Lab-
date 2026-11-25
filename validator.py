import re


def load_airports(path: str) -> set[str]:
    airports = set()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            airports.add(line)

    return airports


def validate_row(fields: list[str], airports: set[str]) -> str | None:
    # Check 1: Wrong number of fields
    if len(fields) != 6:
        return "WRONG_FIELD_COUNT"

    # Remove spaces from every field
    fields = [field.strip() for field in fields]

    flight_id, origin, destination, departure, arrival, price = fields

    # Check 2: Missing field
    if any(field == "" for field in fields):
        return "MISSING_FIELD"

    # Check 3: Flight ID
    if not re.fullmatch(r"[A-Za-z0-9]{2,8}", flight_id):
        return "INVALID_FLIGHT_ID"

    # Check 4: Origin
    if not re.fullmatch(r"[A-Z]{3}", origin) or origin not in airports:
        return "INVALID_ORIGIN"

    # Check 5: Destination
    if not re.fullmatch(r"[A-Z]{3}", destination) or destination not in airports:
        return "INVALID_DESTINATION"

    # Check 6: Same airport
    if origin == destination:
        return "SAME_ORIGIN_DESTINATION"

    # We'll implement the remaining checks next
    return None