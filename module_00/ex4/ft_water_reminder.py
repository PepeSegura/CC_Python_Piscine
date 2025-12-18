def ft_water_reminder():
    days_without_water = int(input("Days since last watering: "))
    if days_without_water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

# ft_water_reminder()
