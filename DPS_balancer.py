import numpy as np

def variate_gun_stats():
    # Ask for maximal damage
    print("Maximal damage of a gun (write full number, e.g., 43.2): ", end="")
    dmg = abs(float(input()))

    # Ask for fire rate
    print("Gun fire rate (bullets per minute): ", end="")
    fr = abs(float(input()))

    # Calculate Damage per Second
    dps = (dmg * fr) / 60  

    # Ask for damage variation range
    print("Choose the damage variation range (+- value): ", end="")
    diap_dmg = abs(float(input()))
    dmg_min = dmg - diap_dmg
    dmg_max = dmg + diap_dmg

    if dmg_min < 0:
        print("⚠️ The damage range is out of bounds (damage - variation < 0).")

    # Ask for fire rate variation range
    print("Choose the fire rate variation range (+- value): ", end="")
    diap_fr = abs(float(input()))
    fr_min = fr - diap_fr
    fr_max = fr + diap_fr

    if fr_min < 0:
        print("⚠️ The fire rate range is out of bounds (fire rate - variation < 0).")

    # Generate damage variations every 0.05
    list_damage = np.arange(dmg_min, dmg_max, 0.05).tolist()
    
    #print("\n📊 Damage variations:", list_damage)

    print("Choose the step for fire rate (ex: step = 5, fire rate in diapason: 600, 605, 610, 615...): ", end="")
    fr_step = abs(float(input()))

    list_firerate = np.arange(fr_min, fr_max, fr_step).tolist()
    print("\n📊 Damage variations:", list_firerate)