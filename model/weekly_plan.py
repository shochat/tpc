class WeeklyPlan:
    def __init__(self, weeks_from_race, is_recovery_week=False, is_with_b_level_race=False):
        self.weeks_from_race = weeks_from_race
        self.workouts = list()
        self.weekly_total = 0
        self.is_recovery_week = is_recovery_week
        self.is_with_b_level_race = is_with_b_level_race

    def add_workout(self, workout):
        self.workouts.append(workout)
        self.weekly_total += workout.length
