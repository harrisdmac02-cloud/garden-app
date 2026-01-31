"""
garden_advice.py - Core logic for seasonal gardening advice

Provides basic monthly/seasonal gardening tips.
Currently Northern Hemisphere focused; future versions may add Southern Hemisphere support.
"""

import datetime

# Hardcoded seasons (Northern Hemisphere)
SEASONS = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

# Very basic example tips – replace with richer content or database
MONTHLY_TIPS = {
    1: "Protect sensitive plants from frost. Plan your spring garden layout.",
    2: "Start seeds indoors for tomatoes, peppers. Prune dormant trees.",
    3: "Plant cool-season crops: lettuce, spinach, peas. Prepare beds.",
    4: "Sow carrots, beets, radishes. Plant perennials and shrubs.",
    5: "Transplant seedlings outside. Mulch to retain moisture.",
    6: "Harvest early crops. Water consistently during heat.",
    7: "Deadhead flowers. Watch for pests in hot weather.",
    8: "Harvest summer vegetables. Plant fall crops like kale.",
    9: "Plant spring bulbs. Clean up garden debris.",
    10: "Divide perennials. Protect plants before first frost.",
    11: "Mulch beds for winter. Clean and store tools.",
    12: "Plan next year's garden. Order seeds early."
}

def get_current_season() -> str:
    """Return current season based on today's month."""
    month = datetime.date.today().month
    return SEASONS.get(month, "Unknown")


def get_monthly_tip(month: int | None = None) -> str:
    """
    Return gardening tip for the given month (1–12).
    Defaults to current month.
    """
    if month is None:
        month = datetime.date.today().month
    return MONTHLY_TIPS.get(month, "No tip available for this month.")


def get_gardening_advice() -> dict:
    """Main function – returns current advice bundle."""
    today = datetime.date.today()
    month_name = today.strftime("%B")
    season = get_current_season()
    tip = get_monthly_tip()

    return {
        "month": month_name,
        "season": season,
        "tip": tip,
        "year": today.year
    }


# Example usage (for testing)
if __name__ == "__main__":
    advice = get_gardening_advice()
    print(f"It's {advice['month']} {advice['year']} – {advice['season']}")
    print(f"Tip: {advice['tip']}")


