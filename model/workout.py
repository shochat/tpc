from enum import Enum, unique


@unique
class WorkoutType(Enum):
    VOLUME = 1,
    INTERVALS = 2,
    TEMPO = 3,
    FARTLEK = 4,
    PYRAMID = 5,
    LITE_VOLUME = 6,
    RACE_OR_TEST = 7


class Intensity(Enum):
    RECOVERY = 1,
    LITE = 2,
    AEROBIC = 3,
    TENSED = 4,
    UN_AEROBIC = 5,
    VERY_INTENSE = 6,
    ALL_OUT = 7


class Workout:
    def __init__(self, name, workout_type, intensity, day_in_week, duration, length):
        self.name = name
        self.workout_type = workout_type
        self.intensity = intensity
        self.day_in_week = day_in_week
        self.duration = duration
        self.length = length

    def __str__(self):
        return 'Name: {}\nIntensity: {}\nType: {}\nDay: {}\nDuration: {}\nLength: {}'.format(self.name,
                                                                                             self.intensity,
                                                                                             self.workout_type,
                                                                                             self.day_in_week,
                                                                                             self.duration,
                                                                                             self.length)

    """
    Abstract method to retrieve parameter
    """
    def parse_details(self):
        raise NotImplementedError('Method should have been implemented by child class')
