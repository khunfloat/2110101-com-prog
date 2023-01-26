def choose(stu1, stu2):
    a_id, a_gpax, a_com, a_cal1, a_cal2 = stu1
    b_id, b_gpax, b_com, b_cal1, b_cal2 = stu2

    grade_mapper = {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 1,
        'F': 0
    }

    a_gpax = float(a_gpax)
    b_gpax = float(b_gpax)

    a_com = grade_mapper[a_com]
    b_com = grade_mapper[b_com]

    a_cal1 = grade_mapper[a_cal1]
    b_cal1 = grade_mapper[b_cal1]

    a_cal2 = grade_mapper[a_cal2]
    b_cal2 = grade_mapper[b_cal2]

    a_is_pass = (a_com == 4) and (a_cal1 >= 2) and (a_cal2 >= 2)
    b_is_pass = (b_com == 4) and (b_cal1 >= 2) and (b_cal2 >= 2)


    if a_is_pass and b_is_pass:

        if a_gpax > b_gpax:
            return [a_id]
        elif b_gpax > a_gpax:
            return [b_id]
        else:
            if a_cal1 > b_cal1:
                return [a_id]
            elif b_cal1 > a_cal1:
                return [b_id]
            else:
                if a_cal2 > b_cal2:
                    return [a_id]
                elif b_cal2 > a_cal2:
                    return [b_id]
                else:
                    return [a_id, b_id]


    elif a_is_pass and not b_is_pass:
        return [a_id]

    elif b_is_pass and not a_is_pass:
        return [b_id]

    elif not a_is_pass and not b_is_pass:
        return []

exec(input())