from flask import Flask
from controllers import controllers

app = Flask(__name__)
app.register_blueprint(controllers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    # TODO: Insert former races as list
    # TODO: Error handling:
    # More than 24 weeks
    # Not all data provided
    # TODO: Check if inserted details enable plan creation according to goal
    # TODO: Set pace in quality workouts according to target pace
    # TODO: improve equation of calculate workout duration
    # TODO: Add description field to workout
    # TODO: Fix mechanism of inserting b level races (day of race and length)
    # TODO: Set IntensityLevel for half marathon
    # TODO: Set quality workouts for half marathon
    # TODO: Week start day other than Sunday
    # TODO: calculate target pace and set it into program
    # TODO: Insert logic to perform Uphill workout only during base and build periods
