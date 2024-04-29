import os
import csv
from unittest.mock import patch

from django.test import TestCase
from django.utils.timezone import localtime

from barkyapi.models import Bookmark
from barkyarch.domain.model import DomainBookmark
from channels.layers import get_channel_layer
from barkyapi.signals import send_bookmark_to_channel, log_bookmark_to_csv
from barkyarch.services.commands import (
    AddBookmarkCommand,
    ListBookmarksCommand,
    DeleteBookmarkCommand,
    UpdateBookmarkCommand,
    GetBookmarkCommand,
)


class TestCommands(TestCase):
    def setUp(self):
        right_now = localtime().date()

        self.domain_bookmark_1 = DomainBookmark(
            id=1,
            title="Test Bookmark",
            url="http://www.example.com",
            notes="Test notes",
            date_added=right_now,
        )

        self.domain_bookmark_2 = DomainBookmark(
            id=2,
            title="Test Bookmark 2",
            url="http://www.example2.com",
            notes="Test notes 2",
            date_added=right_now,
        )

    def test_command_add(self):
        add_command = AddBookmarkCommand()
        add_command.execute(self.domain_bookmark_1)

        # run checks
        # one object is inserted
        self.assertEqual(Bookmark.objects.count(), 1)

        # that object is the same as the one we inserted
        self.assertEqual(Bookmark.objects.get(
            id=1).url, self.domain_bookmark_1.url)

    def test_command_list(self):
        add_command = AddBookmarkCommand()
        add_command.execute(self.domain_bookmark_1)
        add_command.execute(self.domain_bookmark_2)

        list_command = ListBookmarksCommand()
        results = list_command.execute(self)

        self.assertEqual(results.count(), 2)

    def test_command_delete(self):
        add_command = AddBookmarkCommand()
        add_command.execute(self.domain_bookmark_1)

        self.assertEqual(Bookmark.objects.count(), 1)

        delete_command = DeleteBookmarkCommand()
        delete_command.execute(self.domain_bookmark_1)

        self.assertEqual(Bookmark.objects.count(), 0)

    def test_command_update(self):

        add_command = AddBookmarkCommand()
        add_command.execute(self.domain_bookmark_1)

        get_command = GetBookmarkCommand()
        domain_bookmark_temp = get_command.execute(self.domain_bookmark_1.id)
        domain_bookmark_temp.title = "ArchLife"

        self.domain_bookmark_1.title = "archlife"

        update_command = UpdateBookmarkCommand()
        update_command.execute(self.domain_bookmark_1)

        self.assertEqual(Bookmark.objects.count(), 1)

        self.assertEqual(Bookmark.objects.get(id=1).title, "archlife")


# Bookmarks to csv
class SignalHandlersTest(TestCase):
    def setUp(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # CSV file path
        self.csv_file_path = os.path.join(
            current_directory, "domain", "created_log.csv")
        self.channel_layer = get_channel_layer()

    def test_log_bookmark_to_csv(self):
        # Bookmark instance
        bookmark = Bookmark.objects.create(
            title="Test Bookmark",
            url="http://www.example.com",
            notes="Test notes",
            date_added=localtime().date()
        )

        log_bookmark_to_csv(sender=Bookmark, instance=bookmark)

        # Validate path
        self.assertTrue(os.path.exists(self.csv_file_path))

        # Read CSV
        with open(self.csv_file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)

            # Validate CSV Data
            self.assertEqual(rows[1][1], "Test Bookmark")  # Title
            self.assertEqual(rows[1][2], "http://www.example.com")  # URL
            self.assertEqual(rows[1][3], "Test notes")  # Notes

    def test_send_bookmark_to_channel(self):
        # Bookmark instance to channel
        bookmark = Bookmark.objects.create(
            title="Test Bookmark",
            url="http://www.example.com",
            notes="Test notes",
            date_added=localtime().date()
        )

        class FakeChannelLayer:
            def send(self, *args, **kwargs):
                pass

        fake_channel_layer = FakeChannelLayer()

        # Patch the channel layer
        with patch("barkyapi.signals.get_channel_layer", return_value=fake_channel_layer):
            # Call the signal handler
            send_bookmark_to_channel(sender=Bookmark, instance=bookmark)
