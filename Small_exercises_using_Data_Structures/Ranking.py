# Given the final team ranking, compute the teams that get a certificate.

def certificates(ranking: list) -> list:
    """Return the best team of each school.

    The input and output are lists of strings (team names).
    Each string is the name of a school and a digit from 1 to 4.

    Preconditions:
    - ranking is a non-empty list ordered from first to last team
    - there are no duplicate teams
    Postconditions:
    - the output has the first team in 'ranking' of each school
    - the output strings are in the same order as in 'ranking'
    """
    # the ranking is the order the teams came in the competition, so 1st test C1 came first, B2 second - need to find unique schools
    best_teams = []
    awarded_schools = set()
    for team in ranking:
        school = team[:-1]
        if school not in awarded_schools:
            best_teams.append(team)
            awarded_schools.add(school)
    return best_teams

certificates_tests = [
    # case,         ranking,                    certificates
    ('3 schools',   ['C1','B2','B1','A1','C2'], ['C1','B2','A1']),
    # new tests:
    ('1 team',      ['A1'],                     ['A1']),
    ('1 school',    ['C3', 'C1', 'C2'],         ['C3']),
    ('1 team per school', ['C1', 'B1', 'A1'],   ['C1', 'B1', 'A1']),
    ('4 teams per school', ['C2', 'C1', 'C3', 'C4', 'B2', 'B1', 'B3', 'B4', 'A2', 'A1', 'A3', 'A4'], ['C2', 'B2', 'A2'])
]
