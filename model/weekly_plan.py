import random
from enum import Enum, unique
from model.workouts.fartlek_workout import FartlekWorkout
from model.workouts.interval_workout import IntervalWorkout
from model.workouts.pyramid_workout import PyramidWorkout
from model.workouts.uphill_workout import UphillWorkout
from model.workouts.workout import Workout, WorkoutIntensity, WorkoutType


@unique
class WeeklyIntensity(Enum):
    BASE = 1,
    BUILD = 2,
    STRESS = 3,
    TAPPER = 4


@unique
class RecommendedWorkoutDay(Enum):
    MONDAY = 0,
    TUESDAY = 1,
    WEDNESDAY = 2,
    THURSDAY = 3,
    FRIDAY = 4,
    SATURDAY = 5,
    SUNDAY = 6


class WeeklyPlan:
    def __init__(self, weeks_from_race, is_recovery_week=False, is_with_b_level_race=False, intensity_level=None):
        self.weeksFromRace = weeks_from_race
        self.workouts = list()
        self.weeklyTotal = 0
        self.isRecover = is_recovery_week
        self.isBLevelRace = is_with_b_level_race
        self.intensityLevel = intensity_level

    def add_workout(self, workout):
        self.workouts.append(workout)
        self.weeklyTotal += workout.length

    def add_volume_workout(self, volume_workout_detail):
        if not self.isBLevelRace:
            self.add_workout(Workout(description='Run in steady pace', workout_type=WorkoutType.VOLUME, intensity=WorkoutIntensity.AEROBIC,
                                     day_in_week=RecommendedWorkoutDay.SATURDAY, duration=1,
                                     length=volume_workout_detail[self.weeksFromRace]))

    def add_first_quality_workout(self, quality_workout_detail):
        day_in_week = RecommendedWorkoutDay.MONDAY
        quality_type = random.choice(['intervals', 'pyramid', 'uphill', 'fartlek'])
        if self.isRecover:
            workout_intensity_in_list = 'low'
        elif self.isBLevelRace:
            workout_intensity_in_list = 'medium'
        elif self.weeksFromRace is 3:
            workout_intensity_in_list = 'medium'
        elif self.intensityLevel is WeeklyIntensity.STRESS:
            workout_intensity_in_list = 'high'
        elif self.weeksFromRace > 21:
            workout_intensity_in_list = 'low'
        elif 12 < self.weeksFromRace < 21:
            workout_intensity_in_list = 'medium'
        elif self.intensityLevel is WeeklyIntensity.TAPPER:
            workout_intensity_in_list = 'low'
        else:
            workout_intensity_in_list = 'low'
        optional_workouts = quality_workout_detail[quality_type][workout_intensity_in_list]
        if quality_type is 'intervals':
            self.add_workout(IntervalWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))
        elif quality_type is 'pyramid':
            self.add_workout(PyramidWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))
        elif quality_type is 'uphill':
            self.add_workout(UphillWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))
        elif quality_type is 'fartlek':
            self.add_workout(FartlekWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))

    def add_tempo_workout(self, volume_workout_detail):
        distance = max(volume_workout_detail[self.weeksFromRace] - 16, 8)
        description = 'Worm up for 10 minutes\nRun {} KM in race target pace\nCool down for 10 minutes'
        self.add_workout(Workout(description=description, workout_type=WorkoutType.TEMPO, intensity=WorkoutIntensity.TENSED,
                                 day_in_week=RecommendedWorkoutDay.WEDNESDAY, duration=1, length=distance))

    def add_lite_volume_workout(self):
        self.add_workout(Workout(description='Run in steady pace for recovery', workout_type=WorkoutType.LITE_VOLUME, intensity=WorkoutIntensity.LITE,
                                 day_in_week=RecommendedWorkoutDay.FRIDAY, duration=1, length=10))

    def add_second_quality_workout(self, quality_workout_detail):
        day_in_week = RecommendedWorkoutDay.THURSDAY
        quality_type = random.choice(['intervals', 'pyramid', 'uphill', 'fartlek'])
        optional_workouts = quality_workout_detail[quality_type]['low']
        if quality_type is 'intervals':
            self.add_workout(IntervalWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))
        elif quality_type is 'pyramid':
            self.add_workout(PyramidWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))
        elif quality_type is 'uphill':
            self.add_workout(UphillWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))
        elif quality_type is 'fartlek':
            self.add_workout(FartlekWorkout(raw_details=random.choice(optional_workouts), day_in_week=day_in_week))

    def add_second_lite_volume_workout(self):
        self.add_workout(Workout(description='Run in steady pace for recovery', workout_type=WorkoutType.LITE_VOLUME, intensity=WorkoutIntensity.LITE,
                                 day_in_week=RecommendedWorkoutDay.TUESDAY, duration=1, length=10))

    def serialize(self):
        return {
            "weeklyTotal": self.weeklyTotal,
            "isRecovery": self.isRecover,
            "isBLevelRace": self.isBLevelRace,
            "intensity": self.intensityLevel,
            "weeksFromRace": self.weeksFromRace,
            "workouts": list(map(lambda w: w.serialize(), self.workouts))
        }

