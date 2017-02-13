from model.workout import Workout, WorkoutType, Intensity


class IntervalWorkout(Workout):
    def __init__(self, day_in_week, raw_details):
        self.raw_details = raw_details
        self.details = dict()
        self.parse_details()
        super().__init__(self.details['name'], WorkoutType.INTERVALS, Intensity.UN_AEROBIC, day_in_week, self.duration, self.length)

    def parse_details(self):
        self.details['name'] = self.raw_details[0]
        if self.raw_details[1] is not '':
            self.details['Repeat count'] = self.raw_details[1]
        if self.raw_details[2] is not '':
            self.details['Interval distance'] = self.raw_details[2]
        if self.raw_details[3] is not '':
            self.details['Interval time'] = self.raw_details[3]
        if self.raw_details[4] is not '':
            self.details['Interval pace'] = self.raw_details[4]
        if self.raw_details[5] is not '':
            self.details['Recovery distance'] = self.raw_details[5]
        if self.raw_details[6] is not '':
            self.details['Recovery time'] = self.raw_details[6]
        if self.raw_details[7] is not '':
            self.details['Recovery pace'] = self.raw_details[7]
        if self.raw_details[8] is not '':
            self.details['Worm up distance'] = self.raw_details[8]
        if self.raw_details[9] is not '':
            self.details['Cool down distance'] = self.raw_details[9]
        if 'Interval distance' in self.details:
            total_interval = int(self.details['Repeat count']) * (float(self.details['Interval distance']) / 1000)
        else:
            total_interval = (int(self.details['Repeat count']) * int(self.details['Interval time'])) / int(
                self.details['Interval pace'])
        if 'Recovery distance' in self.details:
            total_recovery = int(self.details['Repeat count']) * int(self.details['Recovery distance'])
        else:
            total_recovery = (int(self.details['Repeat count']) * float(self.details['Recovery time'])) / float(
                self.details['Recovery pace'])

        self.length = int(self.details['Worm up distance']) + int(self.details['Cool down distance']) + total_interval + total_recovery
        self.duration = self.length * ((float(self.details['Interval pace']) + float(self.details['Recovery pace'])) / 2)

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
