from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from user.models import Member  # using Member from user app as per project structure


class MemberJWTAuthentication(JWTAuthentication):
    """
    Custom JWT authentication that maps JWT user_id to Member.member_id
    """

    def get_user(self, validated_token):
        try:
            member_id = validated_token.get("user_id")

            if not member_id:
                raise AuthenticationFailed("Token does not contain member_id")

            # Get the member from the database
            member = Member.objects.get(member_id=member_id)
            
            # Create a mock user object that mimics Django's user model
            # but contains the member information
            class MockUser:
                def __init__(self, member):
                    self.pk = member.member_id
                    self.id = member.member_id
                    self.member_id = member.member_id
                    self.user_id = member.member_id
                    self.username = getattr(member, 'member_name', member.member_id)
                    self.is_active = True
                    self.is_authenticated = True
                    self.is_anonymous = False
                    
                    # Add other attributes that might be needed
                    for attr in ['member_name', 'member_email', 'member_type_id']:
                        if hasattr(member, attr):
                            setattr(self, attr, getattr(member, attr, None))
            
            return MockUser(member)
        except Member.DoesNotExist:
            raise AuthenticationFailed("Member not found")
        except Exception as e:
            raise AuthenticationFailed(f"Authentication failed: {str(e)}")