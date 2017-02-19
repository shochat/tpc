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
        self.target_time = datetime.datetime.strptime(form['target_time'], '%H:%M')
        # TODO former races
        self.age = int(form['age'])
        self.weight = int(form['weight'])
        self.shape_level = int(form['shape_level'])
        self.weekly_training_days = int(form['weekly_training_days'])
