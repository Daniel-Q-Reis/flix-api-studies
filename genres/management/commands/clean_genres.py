# to use this, type in terminal -> python manage.py clean_genres

from django.core.management.base import BaseCommand
from django.db.models import Count

from genres.models import Genre


class Command(BaseCommand):
    help = "Finds and deletes duplicate genres, keeping the first instance of each."

    def handle(self, *args, **options):
        self.stdout.write("Starting the search for duplicate genres...")

        duplicates_queryset = (
            Genre.objects.values("name")
            .annotate(name_count=Count("id"))
            .filter(name_count__gt=1)
        )

        duplicates_list = list(duplicates_queryset)

        if not duplicates_list:
            self.stdout.write(self.style.SUCCESS("No duplicate genres found."))
            return

        count = len(duplicates_list)
        if count == 1:
            self.stdout.write("Found 1 duplicate genre name.")
        else:
            self.stdout.write(f"Found {count} duplicate genre names.")

        for item in duplicates_list:
            name = item["name"]
            genres_to_check = Genre.objects.filter(name=name).order_by("id")
            genres_to_delete = genres_to_check[1:]

            self.stdout.write(f"\nProcessing genre '{name}':")
            self.stdout.write(
                f"- Keeping object with ID: {genres_to_check.first().id}"
            )

            for genre in genres_to_delete:
                self.stdout.write(f"- Deleting object with ID: {genre.id}")
                genre.delete()

        self.stdout.write(
            self.style.SUCCESS("\nDuplicate genres cleanup completed successfully!")
        )