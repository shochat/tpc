from model.workout import Workout, WorkoutType, Intensity


class IntervalWorkout(Workout):
    def __init__(self, day_in_week, details):
        self.details = details
        self.parse_details()
        super().__init__(self.details['name'], WorkoutType.INTERVALS, Intensity.UN_AEROBIC, day_in_week, self.duration, self.length)

    def parse_details(self):
        dtl = dict()
        dtl['name'] = self.details[0]
        if self.details[1] is not '':
            dtl['Repeat count'] = self.details[1]
        if self.details[2] is not '':
            dtl['Interval distance'] = self.details[2]
        if self.details[3] is not '':
            dtl['Interval time'] = self.details[3]
        if self.details[4] is not '':
            dtl['Interval pace'] = self.details[4]
        if self.details[5] is not '':
            dtl['Recovery distance'] = self.details[5]
        if self.details[6] is not '':
            dtl['Recovery time'] = self.details[6]
        if self.details[7] is not '':
            dtl['Recovery pace'] = self.details[7]
        if self.details[8] is not '':
            dtl['Worm up distance'] = self.details[8]
        if self.details[9] is not '':
            dtl['Cool down distance'] = self.details[9]
        if 'Interval distance' in dtl:
            total_interval = int(dtl['Repeat count']) * (float(dtl['Interval distance']) / 1000)
        else:
            total_interval = (int(dtl['Repeat count']) * int(dtl['Interval time'])) / int(dtl['Interval pace'])
        if 'Recovery distance' in dtl:
            total_recovery = int(dtl['Repeat count']) * int(dtl['Recovery distance'])
        else:
            total_recovery = (int(dtl['Repeat count']) * float(dtl['Recovery time'])) / float(dtl['Recovery pace'])

        self.length = int(dtl['Worm up distance']) + int(dtl['Cool down distance']) + total_interval + total_recovery
        self.duration = self.length * ((float(dtl['Interval pace']) + float(dtl['Recovery pace'])) / 2)
        return dtl

    def __str__(self):
        if 'Interval distance' in self.details:
            main_drill = '{} Km'.format(self.details['Interval distance'])
        else:
            main_drill = '{} Minutes'.format(self.details['Interval time'])
        if 'Recovery distance' in self.details:
            main_recovery = '{} Km'.format(self.details['Recovery distance'])
        else:
            main_recovery = '{} Minutes'.format(self.details['Recovery time'])
        return '*** {} ***\nWorm up for {} KM\nRepeat for {} times:\n\tRun {} in pace {}' \
               '\n\tRecovery run for {} in pace {}\nCool down for {} KM'.format(self.details['name'],
                                                                                self.details['Worm up distance'],
                                                                                self.details['Repeat count'],
                                                                                main_drill, self.details['Interval pace'],
                                                                                main_recovery, self.details['Recovery pace'],
                                                                                self.details['Cool down distance'])
