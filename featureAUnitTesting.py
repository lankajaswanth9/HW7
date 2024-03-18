import unittest

def calculate_velocity(sprint_points):
    if not sprint_points:
        raise ValueError("Sprint points list cannot be empty.")
    if any(point < 0 for point in sprint_points):
        raise ValueError("Sprint points cannot be negative.")
    
    total_points = sum(sprint_points)
    average_velocity = total_points / len(sprint_points)
    return average_velocity

class TestCalculateVelocity(unittest.TestCase):
    def test_positive_integer_values(self):
        self.assertAlmostEqual(calculate_velocity([10, 20, 30]), 20)

    def test_positive_float_values(self):
        self.assertAlmostEqual(calculate_velocity([10.5, 20.5, 30.5]), 20.5)

    def test_single_element_list(self):
        self.assertAlmostEqual(calculate_velocity([50]), 50)

    def test_large_integer_values(self):
        self.assertAlmostEqual(calculate_velocity([1000, 2000, 3000]), 2000)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_velocity([])

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_velocity([-10, 20, 30])

    def test_all_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_velocity([-10, -20, -30])

    def test_mixed_positive_and_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_velocity([10, -20, 30])

    def test_float_values(self):
        self.assertAlmostEqual(calculate_velocity([10.5, 20.5, 30.5]), 20.5)

    def test_zero_values(self):
        self.assertAlmostEqual(calculate_velocity([0, 0, 0]), 0)

    def test_large_float_values(self):
        self.assertAlmostEqual(calculate_velocity([1000.5, 2000.5, 3000.5]), 2000.5)

if __name__ == '__main__':
    unittest.main()
