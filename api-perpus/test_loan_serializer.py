#!/usr/bin/env python3
"""
Test script for LoanSerializer
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/home/yahya/volunteer/perpustakaan-bersih/api-perpus')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Loan
from api.serializers import LoanSerializer

def test_loan_serializer():
    """Test that LoanSerializer works correctly"""
    print("Testing LoanSerializer...")
    
    # Try to get a loan instance (if any exist)
    try:
        loan = Loan.objects.first()
        if loan:
            print(f"Found loan: {loan.loan_id}")
            
            # Serialize it
            serializer = LoanSerializer(loan)
            data = serializer.data
            
            print("Serialized loan data:")
            for key, value in data.items():
                print(f"  {key}: {value}")
            
            # Check that all expected fields are present
            expected_fields = [
                'loan_id', 'item_code', 'member_id', 'loan_date', 
                'due_date', 'is_return', 'return_date'
            ]
            
            print("\nChecking expected fields:")
            for field in expected_fields:
                if field in data:
                    print(f"  ✓ {field}: {data[field]}")
                else:
                    print(f"  ✗ {field}: MISSING")
        else:
            print("No loans found in database")
            
            # Create a mock loan object for testing
            mock_loan = Loan(
                loan_id=1,
                item_code='TEST001',
                member_id='M001',
                loan_date='2023-01-01',
                due_date='2023-01-15',
                is_return=0
            )
            
            # Serialize it
            serializer = LoanSerializer(mock_loan)
            data = serializer.data
            
            print("Serialized mock loan data:")
            for key, value in data.items():
                print(f"  {key}: {value}")
            
    except Exception as e:
        print(f"Error testing LoanSerializer: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_loan_serializer()