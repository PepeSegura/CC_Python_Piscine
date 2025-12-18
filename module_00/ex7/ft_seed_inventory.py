def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit_str = "Unknown unit type"
    if unit == "packets":
        unit_str = f"{quantity} packets available"
    if unit == "grams":
        unit_str = f"{quantity} grams total"
    if unit == "area":
        unit_str = f"covers {quantity} square meters"
    print(f"{seed_type.capitalize()} seeds: {unit_str}")

# ft_seed_inventory("tomato", 15, "packets")
# ft_seed_inventory("carrot", 8, "grams")
# ft_seed_inventory("lettuce", 12, "area")
