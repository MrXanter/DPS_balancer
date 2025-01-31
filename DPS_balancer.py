import numpy as np

def variate_gun_stats():
    # Ask for maximal damage
    print("Damage of a gun (write full number, e.g., 43.2): ", end="")
    dmg = abs(float(input()))

    # Ask for fire rate
    print("Gun fire rate (bullets per minute): ", end="")
    fr = abs(float(input()))

    # Calculate Damage per Second
    dps = (dmg * fr) / 60
    print(f'DPS with given default stats: {dps}')

    while True:  
        print("Do you want to type your own difference in DPS or strict(gonna vary in range of +-10 DPS) number of DPS?\n"
        "Answer 'difference' or 'strict': ", end="")  
        answ = input().strip().lower()

        if answ in ["difference", "strict"]:  
            break

        print("❌ Undetermined answer. Please choose 'difference' or 'strict'.") 
    
    if answ == "difference":
        print("Choose the diapason in which the DPS will be varied\n" 
              "For ex.: DPS = 670 and you choose diapason 40\n"
              "the final difference in DPS of new gun will be in range of +-40 from its original DPS (DPS - 40 and DPS + 40)", end="")
        diap_dps = abs(float(input()))
        dps_min = dps - diap_dps  # minimal acceptable DPS
        dps_max = dps + diap_dps  # maximal acceptable DPS
    else:
        dps_min = dps - 10  # range of DPS
        dps_max = dps + 10  # range of DPS
    
    # Ask for damage variation range
    print("Choose the damage variation range (+- value): ", end="")
    diap_dmg = abs(float(input()))
    dmg_min = dmg - diap_dmg
    dmg_max = dmg + diap_dmg
    
    if dmg_min < 0:
        print("⚠️ The damage range is out of bounds (damage - variation < 0).")
    
    # Generate damage variations every 0.05
    list_damage = np.arange(dmg_min, dmg_max, 0.05).tolist()

    # Ask for fire rate variation range
    print("Choose the fire rate variation range (+- value): ", end="")
    diap_fr = abs(float(input()))
    fr_min = fr - diap_fr
    fr_max = fr + diap_fr

    if fr_min < 0:
        print("⚠️ The fire rate range is out of bounds (fire rate - variation < 0).")

    # Ask for fire rate step
    print("Choose the step for fire rate (ex: step = 5, fire rate in diapason: 600, 605, 610, 615...): ", end="")
    fr_step = abs(float(input()))

    list_firerate = np.arange(fr_min, fr_max, fr_step).tolist()

    var = 1  # Start counting the variations
    for dmg_value in list_damage:
        for fr_value in list_firerate:
            dps_calculated = dmg_value * fr_value / 60  # Calculate DPS for current variation
            if answ == "strict" and dps_calculated == dps:
                print(f'✨ Variation of the gun stats №{var}:')
                print(f'  Damage: {dmg_value} 🔥')
                print(f'  Fire rate: {fr_value} 🕹️\n')
                var += 1  # Increment the variation number
            elif answ == "difference" and dps_min <= dps_calculated <= dps_max:
                print(f'✨ Variation of the gun stats №{var}:')
                print(f'  Damage: {dmg_value} 🔥')
                print(f'  Fire rate: {fr_value} 🕹️\n')
                var += 1  # Increment the variation number

variate_gun_stats()
