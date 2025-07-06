#!/usr/bin/env python3
"""
Check which half-day trading dates fall on weekends and need to be removed.
"""

import sys
from pathlib import Path
from datetime import datetime, date

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from cn_stock_holidays.common import int_to_date


def check_weekend_half_days():
    """Check which half-day trading dates fall on weekends."""
    data_file = Path("cn_stock_holidays/data_hk.txt")

    weekend_half_days = []
    valid_half_days = []

    with open(data_file, "r") as f:
        for line in f:
            line = line.strip()
            if line.endswith(",h"):
                date_str = line[:-2]  # Remove ',h' suffix
                try:
                    date_obj = int_to_date(int(date_str))
                    weekday = date_obj.weekday()  # 0=Monday, 6=Sunday

                    if weekday >= 5:  # Saturday (5) or Sunday (6)
                        weekend_half_days.append((date_str, date_obj, weekday))
                    else:
                        valid_half_days.append((date_str, date_obj, weekday))
                except ValueError as e:
                    print(f"Error parsing date {date_str}: {e}")

    print("=== Weekend Half-Day Trading Days (Need to be removed) ===")
    for date_str, date_obj, weekday in weekend_half_days:
        weekday_name = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ][weekday]
        print(f"{date_str} -> {date_obj} ({weekday_name})")

    print(f"\nTotal weekend half-days: {len(weekend_half_days)}")

    print("\n=== Valid Half-Day Trading Days ===")
    for date_str, date_obj, weekday in valid_half_days[:10]:  # Show first 10
        weekday_name = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ][weekday]
        print(f"{date_str} -> {date_obj} ({weekday_name})")

    if len(valid_half_days) > 10:
        print(f"... and {len(valid_half_days) - 10} more")

    print(f"\nTotal valid half-days: {len(valid_half_days)}")

    return weekend_half_days, valid_half_days


def remove_weekend_half_days():
    """Remove weekend half-day trading days from the data file."""
    data_file = Path("cn_stock_holidays/data_hk.txt")
    backup_file = Path("cn_stock_holidays/data_hk.txt.backup")

    # Create backup
    import shutil

    shutil.copy2(data_file, backup_file)
    print(f"Created backup: {backup_file}")

    weekend_half_days, valid_half_days = check_weekend_half_days()

    if not weekend_half_days:
        print("No weekend half-days found. No changes needed.")
        return

    # Read all lines
    with open(data_file, "r") as f:
        lines = f.readlines()

    # Filter out weekend half-days
    weekend_half_day_strings = {f"{date_str},h" for date_str, _, _ in weekend_half_days}

    filtered_lines = []
    removed_count = 0

    for line in lines:
        line_stripped = line.strip()
        if line_stripped in weekend_half_day_strings:
            removed_count += 1
            print(f"Removing: {line_stripped}")
        else:
            filtered_lines.append(line)

    # Write back the filtered content
    with open(data_file, "w") as f:
        f.writelines(filtered_lines)

    print(f"\nRemoved {removed_count} weekend half-day trading days.")
    print(f"Updated {data_file}")


if __name__ == "__main__":
    print("Checking weekend half-day trading days...")
    print("=" * 60)

    weekend_half_days, valid_half_days = check_weekend_half_days()

    if weekend_half_days:
        print(
            f"\nFound {len(weekend_half_days)} weekend half-days that need to be removed."
        )
        response = input("\nDo you want to remove them? (y/N): ")
        if response.lower() in ["y", "yes"]:
            remove_weekend_half_days()
        else:
            print("No changes made.")
    else:
        print("\nNo weekend half-days found. Data is already correct.")
