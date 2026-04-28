'''
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.
'''


def add_time(start, duration, day=None):
    # Extração de dados
    start_time, period = start.split()
    start_hour, start_min = map(int, start_time.split(':'))
    dur_hour, dur_min = map(int, duration.split(':'))

    # Normaliza para 24h
    if period == "PM": start_hour += 12
    if period == "AM" and start_hour == 12: start_hour = 0

    # Soma tudo
    total_min = start_min + dur_min
    final_min = total_min % 60
    total_hour = start_hour + dur_hour + (total_min // 60)
    
    final_hour = total_hour % 24
    days_later = total_hour // 24

    # Volta para 12h
    final_period = "AM" if final_hour < 12 else "PM"
    display_hour = final_hour % 12
    if display_hour == 0: display_hour = 12

    # Formata minutos (com zero à esquerda se necessário)
    display_min = str(final_min).zfill(2)

    # Dia da semana
    day_string = ""
    if day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        new_day = (days.index(day.capitalize()) + days_later) % 7
        day_string = f", {days[new_day]}"

    # Mensagem de dias passados
    later_string = ""
    if days_later == 1: later_string = " (next day)"
    elif days_later > 1: later_string = f" ({days_later} days later)"

    return f"{display_hour}:{display_min} {final_period}{day_string}{later_string}"