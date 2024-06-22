import csv
import json
from django.core.management.base import BaseCommand
from search_dishes.models import Restaurant


class Command(BaseCommand):
    help = "Load data from restaurants_small.csv"

    def handle(self, *args, **kwargs):
        with open("./restaurants_small.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                full_details = (
                    json.loads(row["full_details"]) if row["full_details"] != "" else ""
                )
                try:
                    Restaurant.objects.create(
                        id=row["id"],
                        name=row["name"],
                        location=row["location"],
                        items=json.loads(row["items"]),
                        lat_long=row["lat_long"],
                        full_details=full_details,
                    )
                except json.JSONDecodeError as e:
                    self.stdout.write(
                        self.style.ERROR(f"JSONDecodeError: {e} for row: {row}")
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error: {e} for row: {row}"))
        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
