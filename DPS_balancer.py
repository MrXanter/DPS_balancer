import numpy as np
import os

def paginate_results(results, page_size=50):
    total_pages = (len(results) + page_size - 1) // page_size
    current_page = 1
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal screen
        start_idx = (current_page - 1) * page_size
        end_idx = start_idx + page_size
        
        print(f"Page {current_page}/{total_pages}\n")
        for i, result in enumerate(results[start_idx:end_idx], start=start_idx + 1):
            print(f'✨ Variation of the gun stats №{i}:')
            print(f'  Damage: {result[0]} 🔥')
            print(f'  Fire rate: {result[1]} 🕹️\n')
            dps = result[0] * result[1] / 60
            print(f'  DPS: {dps} ⚔️\n')

        print("\n[N] Next | [P] Previous | [Q] Quit")
        choice = input("Select an option: ").strip().lower()

        if choice == 'n' and current_page < total_pages:
            current_page += 1
        elif choice == 'p' and current_page > 1:
            current_page -= 1
        elif choice == 'q':
            break

def variate_gun_stats():
    # Ask for maximal damage
    print("Damage of a gun (write full number, e.g., 43.2): ", end="")
    dmg = abs(float(input().replace(",", ".")))

    # Ask for fire rate
    print("Gun fire rate (bullets per minute): ", end="")
    fr = abs(float(input().replace(",", ".")))

    # Calculate Damage per Second
    dps = (dmg * fr) / 60
    print(f'DPS with given default stats: {dps}\n\n')
          
    while True:  
        print("Do you want to type your own difference in DPS or strict (gonna vary in range of +-10 DPS) number of DPS?\n"
              "Answer 'difference' or 'strict': ", end="")  
        answ = input().strip().lower()

        if answ in ["difference", "strict"]:  
            break
        print("❌ Undetermined answer. Please choose 'difference' or 'strict'.") 
    
    if answ == "difference":
        print("\n")
        print("You have chosen 'difference'.\n"
              "Example: DPS = 671.12, diapason = 40 → final DPS range: (DPS - 40) to (DPS + 40)")
        print("Choose the diapason in which the DPS will be varied: ", end="")
        diap_dps = abs(float(input().replace(",", ".")))
        dps_min, dps_max = dps - diap_dps, dps + diap_dps
    else:
        dps_min, dps_max = dps - 10, dps + 10
    
    # Ask for damage variation range
    print("Choose the damage variation range (+- value): ", end="")
    diap_dmg = abs(float(input().replace(",", ".")))
    dmg_min, dmg_max = max(0, dmg - diap_dmg), dmg + diap_dmg
    
    # Generate damage variations every 0.1  
    list_damage = np.arange(dmg_min, dmg_max, 0.1).tolist()

    # Ask for fire rate variation range
    print("Choose the fire rate variation range (+- value): ", end="")
    diap_fr = abs(float(input().replace(",", ".")))
    fr_min, fr_max = max(0, fr - diap_fr), fr + diap_fr

    # Ask for fire rate step
    print("Choose the step for fire rate (ex: step = 5, fire rate in range: 600, 605, 610...): ", end="")
    fr_step = abs(float(input().replace(",", ".")))
    list_firerate = np.arange(fr_min, fr_max, fr_step).tolist()

    unique_variations = set()  # Store unique (damage, fire rate) pairs
    variations_list = []  # Store results for pagination
    
    for dmg_value in list_damage:
        for fr_value in list_firerate:
            dps_calculated = dmg_value * fr_value / 60
            if dps_min <= dps_calculated <= dps_max:
                variation = (round(dmg_value, 2), round(fr_value, 2))
                if variation not in unique_variations:
                    unique_variations.add(variation)
                    variations_list.append(variation)
    
    paginate_results(variations_list)

variate_gun_stats()
