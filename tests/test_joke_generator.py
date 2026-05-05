"""Unit tests for the joke generator module."""

import pytest
from src.joke_generator import JokeGenerator
from src.fitness_tracker import FitnessTracker, FitnessActivity
from datetime import datetime


class TestJokeGenerator:
    """Test cases for JokeGenerator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.generator = JokeGenerator()

    def teardown_method(self):
        """Clean up after tests."""
        self.generator.close()

    def test_joke_generator_initialization(self):
        """Test that JokeGenerator initializes correctly."""
        assert self.generator is not None
        assert self.generator.JOKE_API_URL == "https://v2.jokeapi.dev"

    def test_get_random_joke(self):
        """Test fetching a random joke from API."""
        joke = self.generator.get_random_joke()
        # Note: This test may fail without internet connection
        if joke:
            assert "type" in joke
            assert joke["type"] in ["single", "twopart"]

    def test_print_joke_single(self, capsys):
        """Test printing a single-line joke."""
        joke_data = {"type": "single", "joke": "Why did the programmer go broke?"}
        self.generator.print_joke(joke_data)
        captured = capsys.readouterr()
        assert "Why did the programmer go broke?" in captured.out

    def test_print_joke_two_part(self, capsys):
        """Test printing a two-part joke."""
        joke_data = {
            "type": "twopart",
            "setup": "Why do programmers prefer dark mode?",
            "delivery": "Because light attracts bugs!"
        }
        self.generator.print_joke(joke_data)
        captured = capsys.readouterr()
        assert "Why do programmers prefer dark mode?" in captured.out
        assert "Because light attracts bugs!" in captured.out


class TestFitnessTracker:
    """Test cases for FitnessTracker class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.tracker = FitnessTracker()

    def test_fitness_tracker_initialization(self):
        """Test that FitnessTracker initializes correctly."""
        assert self.tracker is not None
        assert len(self.tracker.activities) == 0

    def test_add_activity(self):
        """Test adding a fitness activity."""
        activity = self.tracker.add_activity("running", 30)
        assert len(self.tracker.activities) == 1
        assert activity.activity_type == "running"
        assert activity.duration_minutes == 30

    def test_add_activity_with_custom_calories(self):
        """Test adding an activity with custom calorie count."""
        activity = self.tracker.add_activity("custom", 20, calories_burned=150)
        assert activity.calories_burned == 150

    def test_get_total_calories_burned(self):
        """Test calculating total calories burned."""
        self.tracker.add_activity("running", 30)  # 30 * 12 = 360
        self.tracker.add_activity("walking", 60)  # 60 * 4 = 240
        total = self.tracker.get_total_calories_burned()
        assert total == 600

    def test_get_total_duration(self):
        """Test calculating total duration."""
        self.tracker.add_activity("running", 30)
        self.tracker.add_activity("walking", 60)
        total = self.tracker.get_total_duration()
        assert total == 90

    def test_get_activity_count(self):
        """Test getting activity count."""
        self.tracker.add_activity("running", 30)
        self.tracker.add_activity("yoga", 45)
        assert self.tracker.get_activity_count() == 2

    def test_get_activities_by_type(self):
        """Test filtering activities by type."""
        self.tracker.add_activity("running", 30)
        self.tracker.add_activity("running", 20)
        self.tracker.add_activity("yoga", 45)
        running_activities = self.tracker.get_activities_by_type("running")
        assert len(running_activities) == 2

    def test_get_statistics(self):
        """Test getting fitness statistics."""
        self.tracker.add_activity("running", 30)
        self.tracker.add_activity("walking", 60)
        stats = self.tracker.get_statistics()
        assert stats["total_activities"] == 2
        assert stats["total_duration_minutes"] == 90
        assert stats["total_calories_burned"] == 600

    def test_fitness_activity_string(self):
        """Test FitnessActivity string representation."""
        activity = FitnessActivity("running", 30, 360)
        activity_str = str(activity)
        assert "running" in activity_str.lower()
        assert "30" in activity_str
        assert "360" in activity_str


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
