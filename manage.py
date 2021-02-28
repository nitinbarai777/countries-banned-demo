#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


if __name__ == '__main__':
    # Load countrybanned local settings by default
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        os.getenv('DJANGO_SETTINGS_MODULE', 'project.settings.sites_local')
    )

    if len(sys.argv) > 1 and sys.argv[1] == 'migrate':
        from django.db.backends.base.creation import BaseDatabaseCreation

        def sql_table_creation_suffix(obj):
            return ' ROW_FORMAT=DYNAMIC'

        BaseDatabaseCreation.sql_table_creation_suffix = sql_table_creation_suffix

        from django.db.backends.mysql.schema import DatabaseSchemaEditor
        DatabaseSchemaEditor.sql_create_table += ' ROW_FORMAT=DYNAMIC'

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
