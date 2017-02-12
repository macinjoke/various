# coding: utf-8

from django.core.management.base import BaseCommand
from student_deploy3 import student_deploy3


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_deploy3.main()
