import random
from enum import Enum, unique

from model.pyramid_workout import PyramidWorkout

from model.Workouts.interval_workout import IntervalWorkout


@unique
class WeeklyIntensity(Enum):
    BASE = 1,
    BUILD = 2,
    STRESS = 3,
    TAPPER = 4


class WeeklyPlan:
    def __init__(self, weeks_from_race, is_recovery_week=False, is_with_b_level_race=False, intensity_level=None):
        self.weeks_from_race = weeks_from_race
        self.workouts = list()
        self.weekly_total = 0
        self.is_recovery_week = is_recovery_week
        self.is_with_b_level_race = is_with_b_level_race
        self.intensity_level = intensity_level

    def add_workout(self, workout):
        self.workouts.append(workout)
        self.weekly_total += workout.length

    def add_first_quality_workout(self, quality_workout_detail):
        day_in_week = 1
        quality_type = random.choice(['intervals', 'pyramid'])  #, 'fartlek', 'uphill'])
        if self.is_recovery_week:
            workout_intensity_in_list = 'low'
        elif self.is_with_b_level_race:
            workout_intensity_in_list = 'medium'
        elif self.weeks_from_race is 3:
            workout_intensity_in_list = 'medium'
        elif self.intensity_level is WeeklyIntensity.STRESS:
            workout_intensity_in_list = 'high'
        elif self.weeks_from_race > 21:
            workout_intensity_in_list = 'low'
        elif 12 < self.weeks_from_race < 21:
            workout_intensity_in_list = 'medium'
        elif self.intensity_level is WeeklyIntensity.TAPPER:
            workout_intensity_in_list = 'low'
        else:
            workout_intensity_in_list = 'low'
        optional_workouts = quality_workout_detail[quality_type][workout_intensity_in_list]
        if quality_type is 'intervals':
            self.add_workout(IntervalWorkout(day_in_week, random.choice(optional_workouts)))
        elif quality_type is 'pyramid':
            self.add_workout(PyramidWorkout(day_in_week, random.choice(optional_workouts)))