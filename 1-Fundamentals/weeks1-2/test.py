def wages(hours, rate):
    return (((hours - 40) if (hours - 40) > 0 else 0)*rate*1.5) + ((hours - ((hours-40) if (hours - 40) > 0 else 0))*rate)


print(str(wages(45, 10.0)))
