from enum import StrEnum, auto

rate_base = 34.32  # default min


class TypesStr(StrEnum):
    day_regular = 'day_regular'
    friday_morning_8 = 'friday_morning_8'
    friday_evening_8 = 'friday_evening_8'
    friday_morning_12 = 'friday_morning_12'
    saturday_morning_8 = 'saturday_morning_8'
    saturday_evening_8 = 'saturday_evening_8'
    saturday_morning_12 = 'saturday_morning_12'
    night_regular = 'night_regular'
    friday_night_8 = 'friday_night_8'
    saturday_night_8 = 'saturday_night_8'
    friday_night_12 = 'friday_night_12'
    saturday_night_12 = 'saturday_night_12'
    extra_1h_175 = 'extra_1h_175'
    night_7 = 'night_7'
