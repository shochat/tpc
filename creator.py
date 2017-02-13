import datetime
import yaml
from model.interval_workout import IntervalWorkout
from model.plan import Plan, RaceDistance


def main():
    race_date = datetime.date(2017, 6, 11)
    p = Plan(race_date=race_date, race_distance=RaceDistance.MARATHON, time_target=1.5, shape_level=7, weekly_training_days=4)
    p.create()

if __name__ == '__main__':
    with open('resources/quality-main.yaml', 'r') as data:
        details = yaml.load(data)['intervals']

    iwo = IntervalWorkout(3, details[1].split(','))
    print(iwo)
    # main()

    # TODO: Check if inserted details enable plan creation according to goal
    # TODO: Set pace in quality workouts according to target pace
