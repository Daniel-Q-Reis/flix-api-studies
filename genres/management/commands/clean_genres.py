# to use this, type in terminal -> python manage.py clean_genres

from django.core.management.base import BaseCommand
from django.db.models import Count
from genres.models import Genre

class Command(BaseCommand):
    help = 'Finds and deletes duplicate genres, keeping the first instance of each.'

    def handle(self, *args, **options):
        self.stdout.write("Iniciando a busca por gêneros duplicados...")

        duplicates_queryset = (
            Genre.objects.values('name')
            .annotate(name_count=Count('id'))
            .filter(name_count__gt=1)
        )

        duplicates_list = list(duplicates_queryset)

        if not duplicates_list:
            self.stdout.write(self.style.SUCCESS("Nenhum gênero duplicado encontrado."))
            return

        self.stdout.write(f"Encontrados {len(duplicates_list)} nomes de gêneros duplicados.")

        for item in duplicates_list:
            name = item['name']
            genres_to_check = Genre.objects.filter(name=name).order_by('id')
            genres_to_delete = genres_to_check[1:]

            self.stdout.write(f"\nProcessando o gênero '{name}':")
            self.stdout.write(f"- Mantendo o objeto com ID: {genres_to_check.first().id}")

            for genre in genres_to_delete:
                self.stdout.write(f"- Deletando o objeto com ID: {genre.id}")
                genre.delete()

        self.stdout.write(self.style.SUCCESS("\nLimpeza de gêneros duplicados concluída com sucesso!"))