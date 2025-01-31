def variate_gun_stats():
    dmg = abs(float(input("Maximal damage of a gun (write full number, e.g., 43.2): ")))
    fr = abs(float(input("Gun fire rate (bullets per minute): ")))

    dps = (dmg * fr) / 60  # Damage per second

    diap_dmg = abs(float(input("Choose the damage variation range (+- value): ")))
    dmg_min = dmg - diap_dmg
    dmg_max = dmg + diap_dmg

    if dmg_min < 0:
        print("The damage range is out of bounds (damage - variation < 0).")
    
    diap_fr = abs(float(input("Choose the fire rate variation range (+- value): ")))
    fr_min = fr - diap_fr
    fr_max = fr + diap_fr

    if fr_min < 0:
        print("The fire rate range is out of bounds (fire rate - variation < 0).")

    list_damage = []  # Initialize the list
    for i in range(int(dmg_min), int(dmg_max)):  # Convert to int for range
        list_damage.append(i)
    
    print("Damage variations:", list_damage)

