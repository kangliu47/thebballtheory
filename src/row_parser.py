from bs4.element import Tag
from typing import Dict, List, Optional, Tuple

HEADERS = [
    "R#",
    "ADP",
    "PLAYER",
    "POS",
    "TEAM",
    "GP",
    "MPG",
    "FG%",
    "FT%",
    "3PM",
    "PTS",
    "TREB",
    "AST",
    "STL",
    "BLK",
    "TOTAL",
]


def extract_row_data(row: Tag, headers: List[str] = HEADERS) -> Dict[str, str]:
    """Extracts data from a single row element and returns a dictionary."""
    cols = row.find_all("td")
    row_data = {}

    for i, col in enumerate(cols):
        if i < len(headers):
            header = headers[i]
            if header in ["FG%", "FT%"]:
                percentage_data = extract_percentage_with_made_attempted(col, header)
                row_data.update(percentage_data)
            else:
                value = extract_primary_value(col)
                row_data[header] = value

            if header in ["FG%", "FT%", "3PM", "PTS", "TREB", "AST", "STL", "BLK"]:
                z_score_value = extract_z_score(col)
                if z_score_value:
                    row_data[f"{header}_z_score"] = z_score_value

    return row_data


def extract_primary_value(col: Tag) -> str:
    """Extracts the primary value from a column while ignoring non-primary spans and irrelevant information."""
    anchor = col.find("a")
    if anchor:
        return anchor.text.strip()

    spans = col.find_all("span", class_=False)
    if spans:
        return spans[0].text.strip()

    return col.text.strip()


def extract_percentage_with_made_attempted(col: Tag, header: str) -> Dict[str, str]:
    """Extracts percentage value and additional stats (made/attempted) from a column."""
    result = {}
    primary_value = extract_primary_percentage_value(col)
    if primary_value:
        result[header] = primary_value

    made, attempted = extract_made_attempted(col)
    if made and attempted:
        stat_prefix = header[:2]
        result[f"{stat_prefix}M"] = made
        result[f"{stat_prefix}A"] = attempted

    return result


def extract_primary_percentage_value(col: Tag) -> Optional[str]:
    """Extracts the primary percentage value from a column."""
    # Find the first span element that contains the primary percentage value.
    primary_span = col.find("span", class_="float-start")
    if primary_span:
        return primary_span.text.strip()

    # If no span with class 'float-start' is found, try to find the first span
    # that might be relevant.
    spans = col.find_all("span")
    if spans:
        return spans[0].text.strip()

    return None


def extract_made_attempted(col: Tag) -> Tuple[Optional[str], Optional[str]]:
    """Extracts the made and attempted values from a column."""
    extra_span = col.find("span", class_="float-end small")
    if extra_span:
        extra_values = extra_span.text.strip().strip("()")
        if "/" in extra_values:
            made, attempted = extra_values.split("/")
            return made.strip(), attempted.strip()
    return None, None


def extract_z_score(col: Tag) -> Optional[str]:
    """Extracts the z-score from a column if present."""
    z_score_span = col.find("span", {"class": "badge"})
    if z_score_span:
        return z_score_span.text.strip()
    return None
