def variate_gun():
    dmg = print(f'Maximal damage of a gun(write full number for example: 43.2): {abs(input(float))}')
    
    fr = print(f'Gun fire rate(bullets per minute): {abs(input(float))}')
    
    dps = ( float(dmg) * float(fr) ) / 60
    
    diap_dmg = print(f'Choose the diapason in which the damage will be varied(a typed number means +-number from damage){abs(input(float))}')
    
    dmg_min = dmg - diap_dmg 
    dmg_max = dmg + diap_dmg
    if diap_dmg > dmg:
        print("The diapason of damage is out of range(Damage - diapason of damage < 0)")
    
    diap_fr = print(f'Choose the diapason in which the fire rate will be varied(a typed number means +-number from fire rate){abs(input(float))}')
    if diap_fr > fr:
        print("The diapason of fire rate is out of range(Fire rate - diapason of fire rate < 0) ")
