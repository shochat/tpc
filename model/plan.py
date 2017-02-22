import datetime
import yaml
from enum import Enum, unique
from model.workouts.workout import Workout, WorkoutType, WorkoutIntensity
from model.weekly_plan import WeeklyPlan, WeeklyIntensity, RecommendedWorkoutDay


@unique
class RaceDistance(Enum):
    MARATHON = 42.2,
    HALF_MARATHON = 21.1,
    KM_10 = 10


class Plan:
    def __init__(self, user_detail):
        self.race_date = user_detail.race_date
        self.race_day = self.race_date.weekday
        self.race_distance = user_detail.race_distance
        self.target_time = user_detail.target_time
        self.shape_level = user_detail.shape_level
        self.weekly_training_days = user_detail.weekly_training_days
        self.full_weeks_till_race = self.calculate_full_weeks_till_race()
        self.weekly_plan_list = list()
        self.validate_goal_is_reachable()
        for week_number in range(0, self.full_weeks_till_race, 1):
            self.weekly_plan_list.append(WeeklyPlan(week_number))
        self.quality_workout_detail = yaml.load(open('resources/quality-main.yaml', 'r'))
        self.volume_run_detail = yaml.load(open('resources/weekly-volume-workout-distances.yaml', 'r'))

    def create(self):
        self.insert_b_level_races_or_tests()
        self.set_recovery_week()
        self.set_weekly_workout_intensity()
        for wp in self.weekly_plan_list:
            if self.race_distance is RaceDistance.MARATHON:
                wp.add_volume_workout(self.volume_run_detail['marathon'])
                wp.add_first_quality_workout(self.quality_workout_detail['marathon'])
            elif self.race_distance is RaceDistance.HALF_MARATHON:
                wp.add_volume_workout(self.volume_run_detail['half-marathon'])
                wp.add_first_quality_workout(self.quality_workout_detail['half-marathon'])
            wp.add_lite_volume_workout()

            if self.weekly_training_days > 4:
                if self.race_distance is RaceDistance.MARATHON:
                    wp.add_second_quality_workout(self.quality_workout_detail['marathon'])
                elif self.race_distance is RaceDistance.HALF_MARATHON:
                    wp.add_second_quality_workout(self.quality_workout_detail['half-marathon'])
            if self.weekly_training_days > 5:
                wp.add_second_lite_volume_workout()

    def calculate_full_weeks_till_race(self):
        today = datetime.date.today()
        if today.weekday() == 0:
            first_sunday_from_today = today + datetime.timedelta(days=6)
        elif today.weekday() == 1:
            first_sunday_from_today = today + datetime.timedelta(days=5)
        elif today.weekday() == 2:
            first_sunday_from_today = today + datetime.timedelta(days=4)
        elif today.weekday() == 3:
            first_sunday_from_today = today + datetime.timedelta(days=3)
        elif today.weekday() == 4:
            first_sunday_from_today = today + datetime.timedelta(days=2)
        elif today.weekday() == 5:
            first_sunday_from_today = today + datetime.timedelta(days=1)
        else:
            first_sunday_from_today = today
        return (self.race_date - first_sunday_from_today).days // 7

    def validate_goal_is_reachable(self):
        pass

    def insert_b_level_races_or_tests(self):
        if self.race_distance is RaceDistance.MARATHON:
            self.add_marathon_b_races()
        elif self.race_distance.value is RaceDistance.HALF_MARATHON:
            self.add_half_marathon_b_races()

    def set_recovery_week(self):
        for i in range(6, self.full_weeks_till_race, 3):
            self.weekly_plan_list[i].is_recovery_week = True

    def set_weekly_workout_intensity(self):
        tapper_weeks = list(filter((lambda x: x.weeks_from_race < 3), self.weekly_plan_list))
        for week in tapper_weeks:
            week.intensity_level = WeeklyIntensity.TAPPER
        stress_weeks = list(filter((lambda x: 3 <= x.weeks_from_race < 12), self.weekly_plan_list))
        for week in stress_weeks:
            week.intensity_level = WeeklyIntensity.STRESS
        build_weeks = list(filter((lambda x: 12 <= x.weeks_from_race < 17), self.weekly_plan_list))
        for week in build_weeks:
            week.intensity_level = WeeklyIntensity.BUILD
        base_weeks = list(filter((lambda x: x.weeks_from_race >= 17), self.weekly_plan_list))
        for week in base_weeks:
            week.intensity_level = WeeklyIntensity.BASE

    def add_marathon_b_races(self):
        day_in_week = RecommendedWorkoutDay.VOLUME
        last_b_race_weekly_plan = self.weekly_plan_list[5]
        last_b_race_weekly_plan.add_workout(Workout(description='Last B level race', workout_type=WorkoutType.RACE_OR_TEST,
                                                    intensity=WorkoutIntensity.VERY_INTENSE, day_in_week=day_in_week, duration=2,
                                                    length=21))
        last_b_race_weekly_plan.is_with_b_level_race = True
        last_b_race_weekly_plan.is_recovery_week = False

        before_pressure_raise_b_race_weekly_plan = self.weekly_plan_list[11]
        before_pressure_raise_b_race_weekly_plan.add_workout(Workout(
            description='Before tense B level race', workout_type=WorkoutType.RACE_OR_TEST, intensity=WorkoutIntensity.VERY_INTENSE,
            day_in_week=day_in_week, duration=2, length=21))
        before_pressure_raise_b_race_weekly_plan.is_with_b_level_race = True
        before_pressure_raise_b_race_weekly_plan.is_recovery_week = False

        if self.full_weeks_till_race > 17:
            baseline_b_race_weekly_plan = self.weekly_plan_list[17]
            baseline_b_race_weekly_plan.add_workout(Workout(
                description='Baseline B level race', workout_type=WorkoutType.RACE_OR_TEST, intensity=WorkoutIntensity.VERY_INTENSE,
                day_in_week=day_in_week, duration=2, length=21))
            baseline_b_race_weekly_plan.is_with_b_level_race = True
            baseline_b_race_weekly_plan.is_recovery_week = False

    def add_half_marathon_b_races(self):
        day_in_week = RecommendedWorkoutDay.VOLUME
        last_b_race_weekly_plan = self.weekly_plan_list[5]
        last_b_race_weekly_plan.add_workout(Workout(description='Last B level race', workout_type=WorkoutType.RACE_OR_TEST,
                                                    intensity=WorkoutIntensity.VERY_INTENSE, day_in_week=day_in_week, duration=2,
                                                    length=15))
        last_b_race_weekly_plan.is_with_b_level_race = True
        last_b_race_weekly_plan.is_recovery_week = False

        before_pressure_raise_b_race_weekly_plan = self.weekly_plan_list[11]
        before_pressure_raise_b_race_weekly_plan.add_workout(Workout(
            description='Before tense B level race', workout_type=WorkoutType.RACE_OR_TEST, intensity=WorkoutIntensity.VERY_INTENSE,
            day_in_week=day_in_week, duration=2, length=15))
        before_pressure_raise_b_race_weekly_plan.is_with_b_level_race = True
        before_pressure_raise_b_race_weekly_plan.is_recovery_week = False

        if self.full_weeks_till_race > 17:
            baseline_b_race_weekly_plan = self.weekly_plan_list[17]
            baseline_b_race_weekly_plan.add_workout(Workout(
                description='Baseline B level race', workout_type=WorkoutType.RACE_OR_TEST, intensity=WorkoutIntensity.VERY_INTENSE,
                day_in_week=day_in_week, duration=2, length=10))
            baseline_b_race_weekly_plan.is_with_b_level_race = True
            baseline_b_race_weekly_plan.is_recovery_week = False

