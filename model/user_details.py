import datetime
from model.plan import RaceDistance


class UserDetails:
    def __init__(self, form):
        self.race_date = datetime.datetime.strptime(form['raceDetails']['raceDate'], '%d-%m-%Y').date()
        if form['raceDetails']['raceDistance'] == 'MARATHON':
            self.race_distance = RaceDistance.MARATHON
        elif form['raceDetails']['raceDistance'] == 'HALF_MARATHON':
            self.race_distance = RaceDistance.HALF_MARATHON
        else:
            self.race_distance = RaceDistance.KM_10
        time = form['raceDetails']['targetTime'].split(':')
        self.target_time = datetime.time(hour=int(time[0]), minute=int(time[1]), second=int(time[2]))
        # self.target_time = datetime.time(hour=form['raceDetails']['targetTime']['hour'], minute=form['raceDetails']['targetTime']['minute'])
        # self.target_time = datetime.datetime.strptime(form['raceDetails']['targetTime'], '%H:%M').time()
        self.target_pace = self.calculate_target_pace()
        # TODO former races
        self.age = int(form['age'])
        self.weight = int(form['weight'])
        self.shape_level = int(form['shapeLevel'])
        self.weekly_training_days = int(form['weeklyWorkoutDays'])

    def calculate_target_pace(self):
        total_time_in_minutes = self.target_time.hour * 60 + self.target_time.minute
        return total_time_in_minutes / float(self.race_distance.value[0])


class UserDetailsMock(object):
    def __init__(self):
        self.race_date = (datetime.datetime.now() + datetime.timedelta(weeks=15)).date()
        self.race_distance = RaceDistance.MARATHON
        self.target_time = datetime.datetime.strptime('03:30', '%H:%M').time()
        self.target_pace = 5
        # TODO former races
        self.age = 43
        self.weight = 75
        self.shape_level = 4
        self.weekly_training_days = 6

