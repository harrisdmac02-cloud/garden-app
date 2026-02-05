"""
garden_advice.py - Core logic for seasonal gardening advice

Provides monthly and seasonal gardening tips.
Supports both Northern and Southern Hemispheres using a simple 6-month offset.
Loads tips from tips.json if available.
"""

import datetime
import json
import os
from typing import Literal

# Seasons (month → season name) — based on Northern Hemisphere
SEASONS = {
    1: "Winter", 2: "Winter", 3: "Spring",
    4: "Spring", 5: "Spring", 6: "Summer",
    7: "Summer", 8: "Summer", 9: "Autumn",
    10: "Autumn", 11: "Autumn", 12: "Winter"
}

# Hemisphere month shift
HEMISPHERE_SHIFT: dict[Literal["north", "south"], int] = {
    "north": 0,
    "south": 6
}

# ────────────────────────────────────────────────
# Load tips from external JSON file
# ────────────────────────────────────────────────
TIPS_FILE = "tips.json"
MONTHLY_TIPS: dict[int, str] = {}

if os.path.exists(TIPS_FILE):
    try:
        with open(TIPS_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            MONTHLY_TIPS = {int(k): str(v).strip() for k, v in raw_data.items()}
        print(f"Loaded {len(MONTHLY_TIPS)} tips from {TIPS_FILE}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {TIPS_FILE}: {e}")
    except Exception as e:
        print(f"Error loading {TIPS_FILE}: {e}")
else:
    print(f"Warning: {TIPS_FILE} not found in {os.getcwd()}")

# Minimal fallback in case of missing / broken file
if not MONTHLY_TIPS:
    print("Using fallback tips.")
    MONTHLY_TIPS = {
        1: "Protect sensitive plants from frost. Plan ahead.",
        7: "Water deeply and mulch in warm weather.",
        12: "Plan next year's garden and order seeds."
    }


def adjust_month(month: int, hemisphere: Literal["north", "south"] = "north") -> int:
    """
    Apply hemisphere offset to month number (1–12 → 1–12).
    Northern = no change, Southern = +6 months (mod 12).
    """
    shift = HEMISPHERE_SHIFT.get(hemisphere.lower(), 0)
    return ((month - 1 + shift) % 12) + 1


def get_season(month: int, hemisphere: Literal["north", "south"] = "north") -> str:
    """Get season name for a given month and hemisphere."""
    adjusted = adjust_month(month, hemisphere)
    return SEASONS.get(adjusted, "Unknown")


def get_monthly_tip(
    month: int | None = None,
    hemisphere: Literal["north", "south"] = "north"
) -> str:
    """
    Get gardening tip for the given (or current) month and hemisphere.
    Uses tips.json data + month offset for Southern Hemisphere.
    """
    if month is None:
        month = datetime.date.today().month

    adjusted_month = adjust_month(month, hemisphere)
    return MONTHLY_TIPS.get(
        adjusted_month,
        f"No specific tip available for adjusted month {adjusted_month}."
    )


def get_gardening_advice(
    hemisphere: Literal["north", "south"] = "north"
) -> dict:
    """
    Return current gardening advice bundle.

    Returns:
        Dict with month, season, tip, hemisphere, year, etc.
    """
    today = datetime.date.today()
    current_month = today.month
    adjusted_month = adjust_month(current_month, hemisphere)

    return {
        "month_name": today.strftime("%B"),
        "month_number": current_month,
        "adjusted_month": adjusted_month,
        "season": get_season(current_month, hemisphere),
        "tip": get_monthly_tip(current_month, hemisphere),
        "hemisphere": hemisphere.capitalize(),
        "year": today.year
    }


# ────────────────────────────────────────────────
# Demo / Testing
# ────────────────────────────────────────────────
if __name__ == "__main__":
    today = datetime.date.today()
    print(f"Current date: {today.strftime('%Y-%m-%d')}\n")

    for hem in ["north", "south"]:
        advice = get_gardening_advice(hem)  # type: ignore
        print(f"[{hem.upper()}] {advice['month_name']} {advice['year']}")
        print(f"  Season          : {advice['season']}")
        print(f"  Gardening tip   : {advice['tip']}")
        print("  ────────────────────────────────────────\n")