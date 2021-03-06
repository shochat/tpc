from model.workouts.workout import QualityWorkout, WorkoutType


class PyramidWorkout(QualityWorkout):
    def __init__(self, raw_details, day_in_week):
        super().__init__(raw_details=raw_details, day_in_week=day_in_week, workout_type=WorkoutType.PYRAMID)
        if 'Main drill distances' in self.details:
            main_drill = '{} KM'.format(self.details['Main drill distances'])
        else:
            main_drill = '{} Minutes'.format(self.details['Main drill times'])
        if 'Recovery distances' in self.details:
            main_recovery = '{} Km'.format(self.details['Recovery distances'])
        else:
            main_recovery = '{} Minutes'.format(self.details['Recovery times'])

        self.description = '{} Pyramid' \
                           '\nWorm up for {} KM' \
                           '\nRun for {} in pace {}' \
                           '\nRecovery run for {} in pace {} between intervals' \
                           '\nCool down for {} KM'.format(self.details['name'],
                                                          self.details['Worm up distance'],
                                                          main_drill,
                                                          self.details['Main drill paces'],
                                                          main_recovery,
                                                          self.details['Recovery paces'],
                                                          self.details['Cool down distance'])

    def parse_details(self):
        self.details['name'] = self.raw_details[0]
        if self.raw_details[1] is not '':
            self.details['Main drill distances'] = [float(x) for x in self.raw_details[1].split('-')]
        if self.raw_details[2] is not '':
            self.details['Main drill times'] = [float(x) for x in self.raw_details[2].split('-')]
        if self.raw_details[3] is not '':
            self.details['Main drill paces'] = [float(x) for x in self.raw_details[3].split('-')]
        if self.raw_details[4] is not '':
            self.details['Recovery distances'] = [float(x) for x in self.raw_details[4].split('-')]
        if self.raw_details[5] is not '':
            self.details['Recovery times'] = [float(x) for x in self.raw_details[5].split('-')]
        if self.raw_details[6] is not '':
            self.details['Recovery paces'] = [float(x) for x in self.raw_details[6].split('-')]
        if self.raw_details[7] is not '':
            self.details['Worm up distance'] = self.raw_details[7]
        if self.raw_details[8] is not '':
            self.details['Cool down distance'] = self.raw_details[8]
        if 'Main drill distances' in self.details:
            total_pyramid = sum(self.details['Main drill distances'])
        else:
            total_pyramid = sum(
                float([time / pace for time, pace in zip(self.details['Main drill times'], self.details['Main drill paces'])]))
        if 'Recovery distances' in self.details:
            total_recovery = sum(self.details['Recovery distances'])
        else:
            total_recovery = sum(
                float([time / pace for time, pace in zip(self.details['Main drill times'], self.details['Main drill paces'])]))

        self.length = int(self.details['Worm up distance']) + int(self.details['Cool down distance']) + total_pyramid + total_recovery

        self.duration = self.length * (((sum(self.details['Main drill paces']) / len(self.details['Main drill paces'])) +
                                        (sum(self.details['Recovery paces']) / len(self.details['Recovery paces']))) / 2)
