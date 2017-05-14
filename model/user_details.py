import datetime
from model.plan import RaceDistance


class UserDetails:
    def __init__(self, form):
        self.race_date = datetime.datetime.strptime(form['race_date'], '%d %B, %Y').date()
        if form['race_distance'] == 'marathon':
            self.race_distance = RaceDistance.MARATHON
        elif form['race_distance'] == 'half_marathon':
            self.race_distance = RaceDistance.HALF_MARATHON
        else:
            self.race_distance = RaceDistance.KM_10
        self.target_time = datetime.datetime.strptime(form['target_time'], '%H:%M').time()
        self.target_pace = self.calculate_target_pace()
        # TODO former races
        self.age = int(form['age'])
        self.weight = int(form['weight'])
        self.shape_level = int(form['shape_level'])
        self.weekly_training_days = int(form['weekly_training_days'])

    def calculate_target_pace(self):
        total_time_in_minutes = self.target_time.hour * 60 + self.target_time.minute
        return total_time_in_minutes / float(self.race_distance.value[0])
