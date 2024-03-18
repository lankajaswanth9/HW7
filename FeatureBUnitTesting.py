class TeamMember:
    def __init__(self, name, days_off, hours_for_ceremonies, min_hours_per_day, max_hours_per_day):
        self.name = name
        self.days_off = days_off
        self.hours_for_ceremonies = hours_for_ceremonies
        self.min_hours_per_day = min_hours_per_day
        self.max_hours_per_day = max_hours_per_day

    def calculate_effort_hours(self, num_sprint_days):
        total_work_days = num_sprint_days - self.days_off
        if total_work_days < 0:
            raise ValueError("Total work days cannot be negative.")
        
        hours_per_day_average = (self.min_hours_per_day + self.max_hours_per_day) / 2
        effort_hours = (hours_per_day_average - self.hours_for_ceremonies) * total_work_days
        return effort_hours

class SprintCapacityCalculator:
    def __init__(self, num_sprint_days):
        self.num_sprint_days = num_sprint_days
        self.team_members = []

    def add_team_member(self, team_member):
        self.team_members.append(team_member)

    def display_effort_hours(self):
        total_effort_hours_for_team = 0
        for member in self.team_members:
            member_effort_hours = member.calculate_effort_hours(self.num_sprint_days)
            print(f"{member.name}'s Effort-Hours: {member_effort_hours}")
            total_effort_hours_for_team += member_effort_hours
        print("Total Effort-Hours for Team:", total_effort_hours_for_team)
        return total_effort_hours_for_team  # Adjusted to return the value for testing purposes.

import unittest

class TestSprintCapacity(unittest.TestCase):

    def test_single_member_effort_hours(self):
        member = TeamMember("member 1", 2, 1, 8, 10)
        self.assertEqual(member.calculate_effort_hours(10), 64)

    def test_negative_total_work_days_raises_error(self):
        member = TeamMember("member 2", 12, 1, 8, 10)
        with self.assertRaises(ValueError):
            member.calculate_effort_hours(10)

    def test_effort_hours_with_no_days_off(self):
        member = TeamMember("member 3", 0, 2, 7, 9)
        # Corrected the expected result to match the accurate calculation.
        self.assertEqual(member.calculate_effort_hours(10), 60)

    def test_add_member_to_calculator(self):
        calculator = SprintCapacityCalculator(10)
        member = TeamMember("member 4", 1, 1, 8, 10)
        calculator.add_team_member(member)
        self.assertIn(member, calculator.team_members)

    def test_total_effort_hours_for_multiple_members(self):
        calculator = SprintCapacityCalculator(10)
        calculator.add_team_member(TeamMember("member 5", 2, 1, 8, 10))
        calculator.add_team_member(TeamMember("member 6", 1, 2, 7, 9))
        self.assertEqual(calculator.display_effort_hours(), 118)

    def test_effort_hours_with_zero_hours_for_ceremonies(self):
        member = TeamMember("member 7", 1, 0, 8, 10)
        # Corrected the expected result to match the accurate calculation.
        self.assertEqual(member.calculate_effort_hours(10), 81)

    def test_effort_hours_for_full_sprint_no_off_days(self):
        member = TeamMember("member 8", 0, 1, 9, 9)
        self.assertEqual(member.calculate_effort_hours(10), 80)

if __name__ == '__main__':
    unittest.main()
