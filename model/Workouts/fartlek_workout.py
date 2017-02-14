from model.Workouts.workout import QualityWorkout


class FartlekWorkout(QualityWorkout):
    def __init__(self, raw_details, day_in_week):
        super().__init__(raw_details=raw_details, day_in_week=day_in_week)

    def parse_details(self):
        pass

    def __str__(self):
        return ''
