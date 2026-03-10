def main():
    x = convert(input("What's the time? ").strip())

    if 7.0 <= x <= 8.0:
        print("breakfast time")
    elif 12.0 <= x <= 13.0:
        print("lunch time")
    elif 18.0 <= x <= 19.0:
        print("dinner time")
    else:
        print("", end="")


def convert(time_str):
    """
    Convert time string to 24-hour float.
    Supports:
    - H:MM or HH:MM
    - H:MM a.m./p.m. or HH:MM a.m./p.m.
    """
    time_str = time_str.lower().strip()

    # Check if it's a.m. or p.m.
    is_pm = "p.m." in time_str
    is_am = "a.m." in time_str

    # Remove a.m./p.m.
    if is_am:
        time_str = time_str.replace("a.m.", "")
    if is_pm:
        time_str = time_str.replace("p.m.", "")

    # Split hours and minutes
    parts = time_str.split(":")
    hours = float(parts[0])
    minutes = float(parts[1])

    if is_pm and hours != 12:
        hours = hours + 12
    if is_am and hours == 12:
        hours = 0

    # Return time as a float
    return hours + minutes / 60


if __name__ == "__main__":
    main()