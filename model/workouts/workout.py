import json
from enum import Enum, unique


@unique
class WorkoutType(Enum):
    VOLUME = 1,
    INTERVALS = 2,
    TEMPO = 3,
    FARTLEK = 4,
    PYRAMID = 5,
    UPHILL = 6,
    LITE_VOLUME = 7,
    RACE_OR_TEST = 8


class WorkoutIntensity(Enum):
    RECOVERY = 1,
    LITE = 2,
    AEROBIC = 3,
    TENSED = 4,
    UN_AEROBIC = 5,
    VERY_INTENSE = 6,
    ALL_OUT = 7


class Workout:
    def __init__(self, description, workout_type, intensity, day_in_week, duration, length):
        self.description = description
        self.type = workout_type
        self.intensity = intensity
        self.day = day_in_week
        self.duration = duration
        self.length = length

    def __str__(self):
        return 'Type: {}\nDescription: {}\nIntensity: {}\nDay: {}\nLength: {}\nDuration: {}'\
            .format(self.type, self.description, self.intensity, self.day, self.length, self.duration)

    def __repr__(self):
        return json.dumps({
            'description': self.description,
            'type': self.type.name,
            'intensity': self.intensity.name,
            'weekday': self.day.name,
            'length': self.length,
            'duration': self.duration
        })

    def serialize(self):
        return {
            'description': self.description,
            'type': self.type.name,
            'intensity': self.intensity.name,
            'weekday': self.day.name,
            'length': self.length,
            'duration': self.duration
        }


class QualityWorkout(Workout):
    def __init__(self, raw_details, day_in_week, workout_type):
        self.raw_details = raw_details.split(',')
        self.details = dict()
        self.parse_details()
        super().__init__(self.details['name'], workout_type, WorkoutIntensity.TENSED, day_in_week, self.duration, self.length)

    """
    Abstract method to retrieve parameter
    First segment must be the workout's name
    """
    def parse_details(self):
        raise NotImplementedError('Method should have been implemented by child class')
