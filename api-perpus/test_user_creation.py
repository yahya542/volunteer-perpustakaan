#!/usr/bin/env python3
"""
Test script to verify User creation and login functionality.
Run this after registering a user to check if User records are created properly.
"""

import os
import sys
import django
from django.contrib.auth.hashers import check_password

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from authentication.models import User
from user.models import Member

def test_user_creation():
    """Test if User records are created properly after registration."""

    print("🔍 Checking User records in database...")
    users = User.objects.all()

    if not users.exists():
        print("❌ No User records found!")
        print("💡 Make sure you have registered a user first.")
        return

    print(f"✅ Found {users.count()} User record(s):")
    for user in users:
        print(f"   - Username: {user.username}")
        print(f"   - Email: {user.email}")
        print(f"   - User Type: {user.user_type}")
        print(f"   - Password Hash: {user.passwd[:20]}...")

        # Test password checking
        test_password = "password123"
        if check_password(test_password, user.passwd):
            print(f"   ✅ Password 'password123' matches for user {user.username}")
        else:
            print(f"   ❌ Password 'password123' does NOT match for user {user.username}")

    print("\n🔍 Checking Member records...")
    members = Member.objects.all()

    if not members.exists():
        print("❌ No Member records found!")
        return

    print(f"✅ Found {members.count()} Member record(s):")
    for member in members:
        print(f"   - Member ID: {member.member_id}")
        print(f"   - Name: {member.member_name}")
        print(f"   - Email: {member.member_email}")
        print(f"   - Member Type ID: {member.member_type_id}")

def test_login_simulation():
    """Simulate the login process."""
    print("\n🔐 Testing Login Simulation...")

    # Test with NIK as username (provided during registration)
    test_username = "1234567890123456"  # This should match the NIK provided during registration
    test_password = "password123"

    user = User.objects.filter(username=test_username).first()

    if not user:
        print(f"❌ User with username '{test_username}' not found!")
        print("💡 Available usernames (use member_id for login):")
        for u in User.objects.all():
            print(f"   - {u.username}")
        print("\n💡 Member IDs from database:")
        for m in Member.objects.all():
            print(f"   - {m.member_id} (Name: {m.member_name})")
        return

    if check_password(test_password, user.passwd):
        print(f"✅ Login successful for user: {user.username}")
        return {"message": "Login successful", "username": user.username}
    else:
        print(f"❌ Invalid password for user: {user.username}")
        return {"error": "Invalid credentials"}

if __name__ == '__main__':
    try:
        test_user_creation()
        result = test_login_simulation()

        if "error" in result:
            print(f"\n❌ Login test failed: {result['error']}")
        else:
            print(f"\n✅ Login test successful: {result['message']}")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)