"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC, abstractmethod
from datetime import datetime
from injector import Injector, inject
import pytz

import requests
from django.db import transaction

from em_planning_api.models import EMData
from em_planning_arch.domain.model import DomainEMData


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError(
            "A command must implement the execute method")


class PythonTimeStampProvider:
    def __init__(self):
        self.now = datetime.now(pytz.UTC).isoformat()


class AddEMDataCommand(Command):
    """
    Using the django orm and transactions to add EM Data
    """

    @inject
    def __init__(self, now: PythonTimeStampProvider = PythonTimeStampProvider()):
        self.now = now

    def execute(self, data: DomainEMData, timestamp=None):
        em_data = EMData(data.id, data.title, data.url, data.notes, timestamp)
        em_data.timestamp = self.now

        # again, we skip the ouw with django's transaction management
        with transaction.atomic():
            em_data.save()


class GetEMDataCommand(Command):
    """
    Using the django orm and transactions to retrieve EM Data
    """

    def execute(self, data: int, timestamp=None):
        return EMData.objects.get(id=data).to_domain()


class ListEMDataCommand(Command):
    """
    swapping in Django ORM for the database manager
    """

    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, data=None):
        return EMData.objects.all().order_by(self.order_by)


class DeleteEMDataCommand(Command):
    """
    Using the django ORM to delete EM Data
    """

    def execute(self, data: DomainEMData):
        em_data = EMData.objects.get(url=data.url)
        with transaction.atomic():
            em_data.delete()


class UpdateEMDataCommand(Command):
    """
    Using the django ORM to update EM Data
    """

    def execute(self, data: DomainEMData):
        em_data = EMData.update_from_domain(data)
        with transaction.atomic():
            em_data.save()
