def ft_count_harvest_recursive(day=0, end=int(input("Days until harvest: "))):
    if day == end:
        print("Harvest time!")
        return
    print(f"Day {day + 1}")
    ft_count_harvest_recursive(day + 1, end)

# ft_count_harvest_recursive()
