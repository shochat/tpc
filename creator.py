import datetime
from model.plan import Plan, RaceDistance


def main():
    race_date = datetime.date(2017, 6, 11)
    p = Plan(race_date=race_date, race_distance=RaceDistance.MARATHON, time_target=3, shape_level=7, weekly_training_days=6)
    p.create()
    for wp in p.weekly_plan_list:
        print('--- Weekly plan for week {} ---'.format(wp.weeks_from_race))
        print('---  Weekly   total  {}  KM ---'.format(wp.weekly_total))
        for workout in wp.workouts:
            print(workout)

if __name__ == '__main__':
    main()

    # TODO: Check if inserted details enable plan creation according to goal
    # TODO: Set pace in quality workouts according to target pace
    # TODO: improve equation of calculate workout duration
    # TODO: Add description field to workout
    # TODO: Set IntensityLevel for half marathon
    # TODO: Set quality workouts for half marathon
    # TODO: Week start day other than Sunday
    # TODO: calculate target pace and set it into program
    # TODO: Insert logic to perform Uphill workout only during base and build periods
