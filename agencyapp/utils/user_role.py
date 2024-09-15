from job_agency_backend.settings import USER_ROLE_CODE
from agencyapp.models import User

def provide_user_role(user):
    if not user:
        return None
    if not isinstance(user, User):
        return None
    if user.is_superuser:
        return USER_ROLE_CODE.get('admin')
    elif user.is_staff:
        return USER_ROLE_CODE.get('staff')        
    else:
        return USER_ROLE_CODE.get('auth_user')


     