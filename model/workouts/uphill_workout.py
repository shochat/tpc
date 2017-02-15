from model.workouts.workout import QualityWorkout, WorkoutType


class UphillWorkout(QualityWorkout):
    def __init__(self, raw_details, day_in_week):
        super().__init__(raw_details=raw_details, day_in_week=day_in_week, workout_type=WorkoutType.UPHILL)
        if 'Uphill distance' in self.details:
            main_drill = '{} m'.format(self.details['Uphill distance'])
        else:
            main_drill = '{} minutes'.format(self.details['Uphill time'])
        self.description =  '{} Uphill' \
                            '\nWorm up for {} KM' \
                            '\nRepeat for {} times:' \
                            '\n\tRun {} uphill in pace {}' \
                            '\n\tRest jogging downhill' \
                            '\nCool down for {}'.format(self.details['name'],
                                                        self.details['Worm up distance'],
                                                        self.details['repeat_count'],
                                                        main_drill,
                                                        self.details['Uphill pace'],
                                                        self.details['Cool down distance'])

    def parse_details(self):
        self.details['name'] = self.raw_details[0]
        self.details['repeat_count'] = self.raw_details[1]
        if self.raw_details[2] is not '':
            self.details['Uphill distance'] = self.raw_details[2]
        if self.raw_details[3] is not '':
            self.details['Uphill time'] = self.raw_details[3]
        if self.raw_details[4] is not '':
            self.details['Uphill pace'] = self.raw_details[4]
        if self.raw_details[5] is not '':
            self.details['Worm up distance'] = self.raw_details[5]
        if self.raw_details[6] is not '':
            self.details['Cool down distance'] = self.raw_details[6]
        if 'Uphill distance' in self.details:
            total_workout = 2 * int(self.details['repeat_count']) * float(self.details['Uphill distance']) / 1000
        else:
            total_workout = 2 * int(self.details['repeat_count']) * float((self.details['Uphill time'] / float(self.details['Uphill pace'])))
        self.length = total_workout + int(self.details['Worm up distance']) + int(self.details['Cool down distance'])
        self.duration = self.length * float(self.details['Uphill pace']) * 1.5
