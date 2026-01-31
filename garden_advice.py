"""
garden_advice.py - Core logic for seasonal gardening advice

Provides monthly and seasonal gardening tips.
Supports both Northern and Southern Hemispheres (approximate shift-based method).
"""

from __future__ import annotations
import datetime
from typing import Literal

# Seasons - Northern Hemisphere (month → season)
SEASONS_NH = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

# Basic monthly tips (Northern Hemisphere reference)
# For Southern Hemisphere we apply a 6-month offset
MONTHLY_TIPS_NH = {
    1: "Protect sensitive plants from frost. Plan your spring garden layout.",
    2: "Start seeds indoors for tomatoes, peppers. Prune dormant trees and shrubs.",
    3: "Plant cool-season crops: lettuce, spinach, peas, radishes. Prepare beds.",
    4: "Sow carrots, beets, direct-seed beans. Plant perennials and new shrubs.",
    5: "Transplant seedlings outdoors after last frost. Mulch to retain moisture.",
    6: "Harvest early crops. Water consistently — especially during heat waves.",
    7: "Deadhead flowers regularly. Watch for pests and fungal issues in humidity.",
    8: "Harvest peak summer vegetables. Plant fall crops (kale, broccoli, etc.).",
    9: "Plant spring-flowering bulbs. Clean up garden debris and compost.",
    10: "Divide overcrowded perennials. Protect tender plants before first frost.",
    11: "Apply winter mulch. Clean and store tools. Order seeds for next year.",
    12: "Rest and plan next year's garden. Review notes from this season."
}

HEMISPHERE_SHIFT_MONTHS: dict[Literal["north", "south"], int] = {
    "north": 0,
    "south": 6
}


def adjust_month(month: int, hemisphere: Literal["north", "south"] = "north") -> int:
    """
    Shift month number according to hemisphere (simple 6-month offset for south).
    Result is always in range 1–12.
    """
    shift = HEMISPHERE_SHIFT_MONTHS.get(hemisphere.lower(), 0)
    return ((month - 1 + shift) % 12) + 1


def get_season(month: int, hemisphere: Literal["north", "south"] = "north") -> str:
    """Return season name for given month and hemisphere."""
    adjusted_month = adjust_month(month, hemisphere)
    return SEASONS_NH.get(adjusted_month, "Unknown")


def get_monthly_tip(
    month: int | None = None,
    hemisphere: Literal["north", "south"] = "north"
) -> str:
    """
    Return gardening tip for the given (or current) month and hemisphere.
    Uses Northern Hemisphere tips + month offset for Southern Hemisphere.
    """
    if month is None:
        month = datetime.date.today().month

    adjusted_month = adjust_month(month, hemisphere)
    return MONTHLY_TIPS_NH.get(
        adjusted_month,
        "No specific tip available for this month."
    )


def get_gardening_advice(
    hemisphere: Literal["north", "south"] = "north"
) -> dict[str, str | int]:
    """
    Main function: Returns a dictionary with current gardening advice.

    Args:
        hemisphere: "north" (default) or "south"

    Returns:
        Dict with month name, season, tip, and year
    """
    today = datetime.date.today()
    current_month = today.month

    return {
        "month": today.strftime("%B"),
        "month_number": current_month,
        "season": get_season(current_month, hemisphere),
        "tip": get_monthly_tip(current_month, hemisphere),
        "hemisphere": hemisphere.capitalize(),
        "year": today.year
    }


# ────────────────────────────────────────────────
#                  Demo / Testing
# ────────────────────────────────────────────────

if __name__ == "__main__":
    today = datetime.date.today()
    print(f"Current date: {today.strftime('%Y-%m-%d')}\n")

    for hem in ["north", "south"]:
        advice = get_gardening_advice(hem)
        print(f"┌─ {advice['hemisphere']} Hemisphere ───────────────────────┐")
        print(f"  Month     : {advice['month']} {advice['year']}")
        print(f"  Season    : {advice['season']}")
        print(f"  Gardening tip:")
        print(f"    → {advice['tip']}")
        print("└───────────────────────────────────────────────────────┘\n")