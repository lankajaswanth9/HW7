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
    def __init__(self, num_sprint_days, num_team_members):
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

def get_user_input_and_calculate_capacity():
    num_sprint_days = int(input("Total number of Sprint Days: "))
    num_team_members = int(input("Number of Team Members: "))
    
    calculator = SprintCapacityCalculator(num_sprint_days, num_team_members)

    for i in range(num_team_members):
        name = input(f"Enter Team Member {i+1}'s Name: ")
        days_off = int(input("Number of days off (PTO): "))
        hours_for_ceremonies = int(input("Number of hours committed to Sprint ceremonies per day: "))
        min_hours_per_day = int(input("Minimum hours available for sprint per day: "))
        max_hours_per_day = int(input("Maximum hours available for sprint per day: "))
        
        member = TeamMember(name, days_off, hours_for_ceremonies, min_hours_per_day, max_hours_per_day)
        calculator.add_team_member(member)

    calculator.display_effort_hours()

if __name__ == "__main__":
    get_user_input_and_calculate_capacity()
