def print_trip_summary(
    destination,
    country,
    days,
    budget,
    currency,
    travel_month,
    travel_style,
    hotel_cost,
    food_cost,
    transportation_cost,
    miscellaneous_cost
):
    total_estimated_cost = (
        hotel_cost
        + food_cost
        + transportation_cost
        + miscellaneous_cost
    )

    print("=========================")
    print("KelanaAI")
    print("=========================")
    print(f"Destination  : {destination}")
    print(f"Country      : {country}")
    print(f"Days         : {days}")
    print(f"Budget       : {budget} {currency}")
    print(f"Currency     : {currency}")
    print(f"Travel Month : {travel_month}")
    print(f"Style        : {travel_style}")
    print(f"Hotel Cost   : {hotel_cost}")
    print(f"Food Cost    : {food_cost}")
    print(f"Transport    : {transportation_cost}")
    print(f"Misc Cost    : {miscellaneous_cost}")
    print(f"Total Cost   : {total_estimated_cost}")

    if total_estimated_cost > budget:
        print("Budget exceeded.")

    print()

print_trip_summary("Japan", "Japan", 5, 1500, "USD", "December", "Family", 900, 300, 250, 100)
