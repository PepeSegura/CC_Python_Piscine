def ft_harvest_total():
    total, i = 0, 1
    while i <= 3:
        total += int(input(f"Day {i} harvest: "))
        i += 1
    print(f"Total harvest: {total}")

# ft_harvest_total()
