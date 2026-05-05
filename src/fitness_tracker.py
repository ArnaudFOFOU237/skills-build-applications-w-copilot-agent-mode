"""Fitness activity tracker for the OctoFit application."""

from datetime import datetime
from typing import List, Dict, Optional


class FitnessActivity:
    """Represents a single fitness activity."""

    def __init__(self, activity_type: str, duration_minutes: int, calories_burned: int, date: Optional[datetime] = None):
        """Initialize a fitness activity.
        
        Args:
            activity_type: Type of activity (e.g., "running", "weightlifting", "yoga")
            duration_minutes: Duration of the activity in minutes
            calories_burned: Estimated calories burned
            date: Date of the activity (defaults to now)
        """
        self.activity_type = activity_type
        self.duration_minutes = duration_minutes
        self.calories_burned = calories_burned
        self.date = date or datetime.now()

    def __str__(self) -> str:
        """String representation of the activity."""
        return f"{self.activity_type.title()} - {self.duration_minutes} min, {self.calories_burned} cal - {self.date.strftime('%Y-%m-%d %H:%M')}"


class FitnessTracker:
    """Track fitness activities and provide statistics."""

    # Estimated calories per minute for different activities
    CALORIE_RATES = {
        "running": 12,
        "walking": 4,
        "weightlifting": 8,
        "yoga": 4,
        "cycling": 10,
        "swimming": 11,
        "cardio": 9,
    }

    def __init__(self):
        """Initialize the fitness tracker."""
        self.activities: List[FitnessActivity] = []

    def add_activity(self, activity_type: str, duration_minutes: int, calories_burned: Optional[int] = None) -> FitnessActivity:
        """Add a new fitness activity.
        
        Args:
            activity_type: Type of activity
            duration_minutes: Duration in minutes
            calories_burned: Optional custom calorie count (will be calculated if not provided)
            
        Returns:
            The created FitnessActivity object
        """
        if calories_burned is None:
            rate = self.CALORIE_RATES.get(activity_type.lower(), 5)
            calories_burned = rate * duration_minutes
        
        activity = FitnessActivity(activity_type, duration_minutes, calories_burned)
        self.activities.append(activity)
        return activity

    def get_total_calories_burned(self) -> int:
        """Get total calories burned across all activities.
        
        Returns:
            Total calories burned
        """
        return sum(activity.calories_burned for activity in self.activities)

    def get_total_duration(self) -> int:
        """Get total duration of all activities.
        
        Returns:
            Total duration in minutes
        """
        return sum(activity.duration_minutes for activity in self.activities)

    def get_activity_count(self) -> int:
        """Get the total number of activities.
        
        Returns:
            Number of activities
        """
        return len(self.activities)

    def get_activities_by_type(self, activity_type: str) -> List[FitnessActivity]:
        """Get all activities of a specific type.
        
        Args:
            activity_type: Type of activity to filter by
            
        Returns:
            List of matching activities
        """
        return [a for a in self.activities if a.activity_type.lower() == activity_type.lower()]

    def get_statistics(self) -> Dict[str, any]:
        """Get fitness statistics.
        
        Returns:
            Dictionary containing various fitness statistics
        """
        total_calories = self.get_total_calories_burned()
        total_duration = self.get_total_duration()
        total_activities = self.get_activity_count()
        
        return {
            "total_activities": total_activities,
            "total_duration_minutes": total_duration,
            "total_calories_burned": total_calories,
            "average_calories_per_activity": total_calories // total_activities if total_activities > 0 else 0,
            "average_duration_minutes": total_duration // total_activities if total_activities > 0 else 0,
        }

    def print_statistics(self) -> None:
        """Print fitness statistics in a formatted way."""
        stats = self.get_statistics()
        print("\n" + "="*50)
        print("🏋️  FITNESS STATISTICS")
        print("="*50)
        print(f"Total Activities: {stats['total_activities']}")
        print(f"Total Duration: {stats['total_duration_minutes']} minutes")
        print(f"Total Calories Burned: {stats['total_calories_burned']} cal")
        if stats['total_activities'] > 0:
            print(f"Average per Activity: {stats['average_calories_per_activity']} cal, {stats['average_duration_minutes']} min")
        print("="*50 + "\n")

    def print_activities(self) -> None:
        """Print all recorded activities."""
        if not self.activities:
            print("\nNo activities recorded yet.\n")
            return
        
        print("\n" + "="*50)
        print("📋 RECORDED ACTIVITIES")
        print("="*50)
        for i, activity in enumerate(self.activities, 1):
            print(f"{i}. {activity}")
        print("="*50 + "\n")
