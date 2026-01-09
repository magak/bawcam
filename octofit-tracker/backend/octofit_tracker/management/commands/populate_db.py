from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data (delete individually for Djongo compatibility)
        for obj in User.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Activity.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id is not None:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.id is not None:
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=steve, type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=bruce, type='swim', duration=60, date='2023-01-03')
        Activity.objects.create(user=clark, type='run', duration=50, date='2023-01-04')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=100, rank=1)
        Leaderboard.objects.create(user=steve, score=90, rank=2)
        Leaderboard.objects.create(user=bruce, score=80, rank=1)
        Leaderboard.objects.create(user=clark, score=70, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
