import unittest
import datetime
from model.plan import Plan
from model.workout import Workout


class TestWorkout(unittest.TestCase):
    def test_print(self):
        workout_1 = Workout('volume', Workout.WorkoutType.FARTLEK, 'high', 6, 120, 24)
        self.assertEqual(workout_1.print(), 'Name: volume\n'
                                            'Intensity: high\n'
                                            'Type: WorkoutType.FARTLEK\n'
                                            'Day: 6\nDuration: 120\n'
                                            'Length: 24')

    def test_calculate_weeks_till_race_one__full_week(self):
        date = datetime.date.today() + datetime.timedelta(days=7)
        p = Plan(date, 0, 0, 0)
        self.assertEqual(p.calculate_full_weeks_till_race(), 1)

    def test_calculate__full_weeks_till_race_non_full_weeks(self):
        date = datetime.date.today() + datetime.timedelta(days=43)
        p = Plan(date, 0, 0, 0)
        self.assertEqual(p.calculate_full_weeks_till_race(), 6)

if __name__ == '__main__':
    unittest.main(verbosity=4)
