def parse_sprint_points(input_str):
    try:
        sprint_points = [float(point.strip()) for point in input_str.split(',')]
        return sprint_points
    except ValueError:
        raise ValueError("All sprint points must be valid numbers.")

def calculate_velocity(sprint_points):
    if not sprint_points:
        raise ValueError("Sprint points list cannot be empty.")
    if any(point < 0 for point in sprint_points):
        raise ValueError("Sprint points cannot be negative.")
    
    total_points = sum(sprint_points)
    average_velocity = total_points / len(sprint_points)
    return average_velocity

def main():
    previous_sprint_points_str = input("Enter sprints point completions (comma-separated): ")
    try:
        sprint_points = parse_sprint_points(previous_sprint_points_str)
        average_velocity = calculate_velocity(sprint_points)
        print(f"Output: Average Velocity: {average_velocity:.2f} points per sprint")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
