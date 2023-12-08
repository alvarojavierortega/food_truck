from django.core.management.base import BaseCommand, CommandError
from food_trucks.fake_populate import (ApplicantFactory,
                                       LocationFactory)

FACTORY_MODEL_LIST = [LocationFactory, ApplicantFactory]

class Command(BaseCommand):
    help = "This command populates the database with fake information."

    def add_arguments(self, parser):
        parser.add_argument("size_batch", type=int)

    def handle(self, *args, **options):
        size_batch = options["size_batch"]

        if size_batch <= 0:
            raise CommandError(f"The size batch must be a number greater than zero.")

        for index, model in enumerate(FACTORY_MODEL_LIST):
          
            try:
                model.create_batch(size_batch*(20**index))
                self.stdout.write(
                    self.style.SUCCESS(f'Model {model.__name__} successfully populated.')
                )
            except:
                raise CommandError(f'Something went wrong, check model {model.__name__}')
            
        self.stdout.write(
                self.style.SUCCESS('Successfully fake population')
            )

