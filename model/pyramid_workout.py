from model.workout import Workout, WorkoutType, Intensity


class PyramidWorkout(Workout):
    def __init__(self, day_in_week, details):
        self.details = details
        self.parse_details()
        super().__init__(self.details['name'], WorkoutType.INTERVALS, Intensity.UN_AEROBIC, day_in_week, self.duration, self.length)

    def __str__(self):
        pass

    def parse_details(self):
        dtl = dict()
        dtl['name'] = self.details[0]
        if self.details[1] is not '':
            dtl['Main drill distances'] = self.details[1]
        if self.details[2] is not '':
            dtl['Main drill times'] = self.details[2]
        if self.details[3] is not '':
            dtl['Main drill paces'] = self.details[3]
        if self.details[4] is not '':
            dtl['Recovery distances'] = self.details[4]
        if self.details[5] is not '':
            dtl['Recovery times'] = self.details[5]
        if self.details[6] is not '':
            dtl['Recovery paces'] = self.details[6]
        if self.details[7] is not '':
            dtl['Worm up distance'] = self.details[7]
        if self.details[8] is not '':
            dtl['Cool down distance'] = self.details[8]

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
