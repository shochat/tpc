from model.workouts.workout import QualityWorkout, WorkoutType


class FartlekWorkout(QualityWorkout):
    def __init__(self, raw_details, day_in_week):
        super().__init__(raw_details=raw_details, day_in_week=day_in_week, workout_type=WorkoutType.FARTLEK)

    def parse_details(self):
        self.details['name'] = self.raw_details[0]
        if self.raw_details[1] is not '':
            self.details['Repeat count'] = int(self.raw_details[1])
        if self.raw_details[2] is not '':
            self.details['Main drill distances'] = [float(x) for x in self.raw_details[2].split('-')]
        if self.raw_details[3] is not '':
            self.details['Main drill times'] = [float(x) for x in self.raw_details[3].split('-')]
        if self.raw_details[4] is not '':
            self.details['Main drill paces'] = [float(x) for x in self.raw_details[4].split('-')]
        if self.raw_details[5] is not '':
            self.details['Worm up distance'] = int(self.raw_details[5])
        if self.raw_details[6] is not '':
            self.details['Cool down distance'] = int(self.raw_details[6])

        if 'Main drill distances' in self.details:
            total_workout = self.details['Repeat count'] * sum(self.details['Main drill distances']) / 1000
        else:
            total_workout = self.details['Repeat count'] * sum(
                float([time / pace for time, pace in zip(self.details['Main drill times'], self.details['Main drill paces'])]))

        self.length = self.details['Worm up distance'] + self.details['Cool down distance'] + total_workout

        self.duration = self.length * (sum(self.details['Main drill paces']) / len(self.details['Main drill paces']))

    def __str__(self):
        if 'Main drill distances' in self.details:
            main_drill = '{} KM'.format(self.details['Main drill distances'])
        else:
            main_drill = '{} Minutes'.format(self.details['Main drill times'])

        return '*** {} ***' \
               '\nWorm up for {} KM' \
               '\nRepeat for {} times:' \
               '\n\tRun {} in pace {} (NO RECOVERY BETWEEN SETS)' \
               '\nCool down for {} KM'.format(self.details['name'],
                                              self.details['Worm up distance'],
                                              self.details['Repeat count'],
                                              main_drill,
                                              self.details['Main drill paces'],
                                              self.details['Cool down distance']
                                              )
