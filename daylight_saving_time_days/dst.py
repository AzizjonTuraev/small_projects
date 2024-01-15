import pytz
import datetime

def dst_days(gewuenschtes_jahr = datetime.datetime.now().year, timezone = "Europe/Berlin"):

    tz_timezone = pytz.timezone(timezone)
    end_winter_time = datetime.datetime(year=gewuenschtes_jahr, month=4, day=1)
    end_summer_time = datetime.datetime(year=gewuenschtes_jahr, month=11, day=1)

    for i in range(8):
        end_winter_time = end_winter_time - datetime.timedelta(days=1)
        if end_winter_time.weekday() == 6:
            break
    for i in range(8):
        end_summer_time = end_summer_time - datetime.timedelta(days=1)
        if end_summer_time.weekday() == 6:
            break

    localized_end_winter_time = tz_timezone.localize(end_winter_time)
    localized_end_summer_time = tz_timezone.localize(end_summer_time)
    return localized_end_winter_time, localized_end_summer_time