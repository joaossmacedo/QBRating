def calculate_qb_rating(attempts: int, completions: int, yards: int,
                        touchdowns: int, interceptions: int) -> float:
    r1 = completion_percentage(attempts, completions)
    r2 = yard_per_attempt(attempts, yards)
    r3 = td_per_attempt(attempts, touchdowns)
    r4 = int_per_attempt(attempts, interceptions)

    return (r1 + r2 + r3 + r4) / 0.06


def completion_percentage(attempts: int, completions: int) -> float:
    value = ((completions / attempts) - 0.3) * 5
    if value < 0:
        return 0
    elif value > 2.375:
        return 2.375
    else:
        return value


def yard_per_attempt(attempts: int, yards: int) -> float:
    value = ((yards / attempts) - 3) * 0.25
    if value < 0:
        return 0
    elif value > 2.375:
        return 2.375
    else:
        return value


def td_per_attempt(attempts: int, touchdowns: int) -> float:
    value = (touchdowns / attempts) * 20
    if value < 0:
        return 0
    elif value > 2.375:
        return 2.375
    else:
        return value


def int_per_attempt(attempts: int, interceptions: int) -> float:
    value = 2.375 - ((interceptions / attempts) * 25)
    if value < 0:
        return 0
    elif value > 2.375:
        return 2.375
    else:
        return value


qb_name = input("Enter the player's name: ")

att = 0
while att <= 0:  # attempts must be a positive number
    try:
        att = int(input("Enter No. of attempts: "))
    except ValueError:
        pass

cmp = -1
while cmp < 0 or cmp > att:  # attempts must be a positive number and smaller than attempts
    try:
        cmp = int(input("Enter No. of completions: "))
    except ValueError:
        pass

yds = 0
if cmp != 0:  # if the qb didn't complete a pass he can't have any yard thrown
    yds = cmp * 99 + 1
    while 99 * cmp < yds or yds < -99 * cmp:  # a pass can't be longer than 99yds
        try:
            yds = int(input("Enter No. of passing yards: "))
        except ValueError:
            pass

# tds must be positive and smaller than complete passes
td = -1
while td < 0 or td > cmp:
    try:
        td = int(input("Enter No. of Touchdowns: "))
    except ValueError:
        pass

inter = -1
while inter < 0 or inter > att - cmp:  # interceptions must be positive and smaller than incomplete passes

    try:
        inter = int(input("Enter No. of Interceptions: "))
    except ValueError:
        pass

qb_rating = calculate_qb_rating(att, cmp, yds, td, inter)

print(qb_name + " passer rating is " + str(qb_rating))