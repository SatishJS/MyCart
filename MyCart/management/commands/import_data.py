from optparse import make_option

from django.core.management.base import BaseCommand

from ...utils.insert import insert_data


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option(
            '-i',
            '--insert',
            action='store_true',
            default=False,
            help='Insert Data into DB',
        ),
        make_option(
            '-o',
            '--overwrite',
            action='store_true',
            default=False,
            help='Overwrite any locally modified data with the fetched data.',
        ),
    )

    def handle(self, *args, **options):
        self.insert = options.get('insert', False)
        self.overwrite = options.get('overwrite', False)

        if self.insert:
            insert_data(self.overwrite, 1)
