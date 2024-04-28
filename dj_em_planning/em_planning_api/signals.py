import csv
from pathlib import Path
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .consumers import SimpleEMDataConsumer
from .models import EMData

channel_layer = get_channel_layer()


# making sense of this example:
# - save_em_data is the receiver function
# - EM Data is the sender and post_save is the signal.
# - Use Case: Everytime EM Data is saved, the save_profile function will be executed.
def log_em_data_to_csv(sender, instance, **kwargs):
    print("EMData signal: CSV")

    file = Path(__file__).parent.parent / "em_planning_arch" / \
        "domain" / "em_data.csv"
    print(f"Writing to {file}")

    # the with statement takes advantate of the context manager protocol: https://realpython.com/python-with-statement/#the-with-statement-approach
    # for reference, here is how open() works: https://docs.python.org/3/library/functions.html#open
    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(
            logfile,
            delimiter=",",
        )
        logwriter.writerow(
            [
                instance.date,
                instance.time,
                instance.frequency,
                instance.device,
                instance.location,
                instance.grid_1,
                instance.grid_2,
                instance.lat,
                instance.long,
                instance.nearhit,
            ]
        )


def send_em_data_to_channel(sender, instance, **kwargs):
    print("EM Data signal: Channel")
    print(f"Sending EM Data to channel: {instance}")

    async_to_sync(channel_layer.send)(
        "em-data-add", {"type": "print.emdata",
                        "data": instance.frequency}
    )


# connect the signal to this receiver
post_save.connect(log_em_data_to_csv, sender=EMData)
post_save.connect(send_em_data_to_channel, sender=EMData)
