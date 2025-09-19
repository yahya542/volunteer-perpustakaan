#!/usr/bin/env python3
"""
Script to create default member types for the library system.
Run this after migrations to populate the MstMemberType table.
"""

import os
import sys
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from user.models import MstMemberType

def create_default_member_types():
    """Create default member types if they don't exist."""

    default_types = [
        {
            'member_type_name': 'Mahasiswa',
            'loan_limit': 3,
            'loan_periode': 7,
            'enable_reserve': 1,
            'reserve_limit': 2,
            'member_periode': 365,
            'reborrow_limit': 2,
            'fine_each_day': 500,
            'grace_periode': 3,
        },
        {
            'member_type_name': 'Dosen',
            'loan_limit': 5,
            'loan_periode': 14,
            'enable_reserve': 1,
            'reserve_limit': 5,
            'member_periode': 365,
            'reborrow_limit': 3,
            'fine_each_day': 1000,
            'grace_periode': 7,
        },
        {
            'member_type_name': 'Staff',
            'loan_limit': 4,
            'loan_periode': 10,
            'enable_reserve': 1,
            'reserve_limit': 3,
            'member_periode': 365,
            'reborrow_limit': 2,
            'fine_each_day': 750,
            'grace_periode': 5,
        },
        {
            'member_type_name': 'Umum',
            'loan_limit': 2,
            'loan_periode': 7,
            'enable_reserve': 0,
            'reserve_limit': 1,
            'member_periode': 180,
            'reborrow_limit': 1,
            'fine_each_day': 1000,
            'grace_periode': 3,
        }
    ]

    created_count = 0
    for member_type_data in default_types:
        member_type, created = MstMemberType.objects.get_or_create(
            member_type_name=member_type_data['member_type_name'],
            defaults={
                **member_type_data,
                'input_date': date.today(),
                'last_update': date.today(),
            }
        )
        if created:
            created_count += 1
            print(f"✅ Created member type: {member_type.member_type_name}")
        else:
            print(f"ℹ️  Member type already exists: {member_type.member_type_name}")

    print(f"\n🎉 Successfully created {created_count} new member types!")
    print("📋 Available member types:")
    for mt in MstMemberType.objects.all():
        print(f"   - {mt.member_type_name} (ID: {mt.member_type_id})")

if __name__ == '__main__':
    try:
        create_default_member_types()
        print("\n✅ Member types setup completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)