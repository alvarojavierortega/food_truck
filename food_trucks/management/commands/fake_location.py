from django.core.management.base import BaseCommand, CommandError
from food_trucks.fake_populate import LocationFactory


class Command(BaseCommand):
    help = "This command generates random locations."

    def add_arguments(self, parser):
        parser.add_argument("size_batch", type=int)

    def handle(self, *args, **options):
        size_batch = options["size_batch"]

        if size_batch <= 0:
            raise CommandError(f"The size batch must be a number greater than zero.")
          
        try:
            LocationFactory.create_batch(size_batch)
            self.stdout.write(
                self.style.SUCCESS(f'Model {LocationFactory.__name__} successfully populated.')
            )
        except:
            raise CommandError(f'Something went wrong, check model {LocationFactory.__name__}')
