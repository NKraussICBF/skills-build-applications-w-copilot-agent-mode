from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create users (superheroes)
        users = [
            User.objects.create(email='tony@stark.com', name='Iron Man', team=marvel),
            User.objects.create(email='steve@rogers.com', name='Captain America', team=marvel),
            User.objects.create(email='bruce@banner.com', name='Hulk', team=marvel),
            User.objects.create(email='clark@kent.com', name='Superman', team=dc),
            User.objects.create(email='bruce@wayne.com', name='Batman', team=dc),
            User.objects.create(email='diana@themyscira.com', name='Wonder Woman', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Strength Training', description='Full body strength workout', difficulty='Hard'),
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Medium'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Swimming', duration=60, date=timezone.now().date())

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
