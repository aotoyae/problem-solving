def solution(bandage, health, attacks):
    run_time, heal_per_s, point_heal = bandage
    life = health
    success_count = 0
    time_count = 0
 
    for attack in attacks:
        attack_time, damage = attack

        while time_count < attack_time:
            success_count += 1
            life += heal_per_s
            
            if success_count == run_time:
                success_count = 0
                life += + point_heal

            if life > health: life = health
            time_count += 1 

        life -= damage
        if life <= 0: return -1

        success_count = 0
        time_count += 1

    return life