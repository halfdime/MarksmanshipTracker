__author__ = 'Robert'

__version__ = 0.1

def shooter_courses_table(shooter):
    """Generate a full list of course tables for a user with a given header.

    :param int shooter: ID of the shooter to build.
    :return:
    """
    """Need a join here from scores to user to course_of_fire to build table.

    For each course, we call the shooter_course_table(shooter, course_of_fire).

    """
    pass

def shooter_course_table(shooter, course_of_fire):
    """Return a table representing this shooters progress through a given course_of_fire.

    :param int shooter: ID of the shooter to build.
    :param int course_of_fire: ID of the course of fire to build.
    :return: Complete Table object with course of fire information.

    """
    tabe = TABLE()