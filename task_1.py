time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_values = time_string.split(',')
total_minutes = 0


for value in time_values:
    parts = value.split()

    minutes_in_value = 0

    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            minutes_in_value += hours * 60

        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            minutes_in_value += minutes

        elif 's' in part:
            seconds = int(part.replace('s', ''))
            minutes_in_value += seconds // 60

    total_minutes += minutes_in_value


print(f"Общее количество минут: {total_minutes}")