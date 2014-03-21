import random


def _get_roll_number():
    return random.randrange(1, 7)


def roll(num_defenders, num_attackers):
    print num_defenders, num_attackers
    if not num_defenders or not num_attackers:
        return num_defenders, num_attackers

    defence_dice_num = min(num_defenders, 2)
    attack_dice_num = max(min(num_attackers - 1, 3), 1)
    max_comparisons = min(defence_dice_num, attack_dice_num)

    defence_rolls = [_get_roll_number() for _ in xrange(defence_dice_num)]
    defence_rolls.sort()
    attack_rolls = [_get_roll_number() for _ in xrange(attack_dice_num)]
    attack_rolls.sort()

    for _ in xrange(max_comparisons):
        attack_roll = attack_rolls.pop()
        defence_roll = defence_rolls.pop()

        if attack_roll > defence_roll:
            num_defenders -= 1
        elif attack_roll == defence_roll:
            num_attackers -= 1
        else:
            num_attackers -= 1

    return roll(num_defenders, num_attackers)


def main():
    while True:
        defenders = int(raw_input('Enter number of defenders:'))
        attackers = int(raw_input('Enter number of attackers:'))

        defenders, attackers = roll(defenders, attackers)

        if defenders:
            print 'Defenders win! {num} armies left'.format(num=defenders)
        else:
            print 'Attackers win! {num} armies left'.format(num=attackers)




if __name__ == '__main__':
    main()



