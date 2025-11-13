from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team2', universe='Test')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team3', universe='Test')
        user = User.objects.create(email='test2@example.com', name='Test User2', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2025-11-13')
        self.assertEqual(str(activity), 'Test User2 - Run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team4', universe='Test')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team4 - 100 pts')
