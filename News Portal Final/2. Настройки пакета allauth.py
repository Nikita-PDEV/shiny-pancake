INSTALLED_APPS = [
    'allauth',  
    'allauth.account',
]  

AUTHENTICATION_BACKENDS = (  
    'allauth.account.auth_backends.AuthenticationBackend',  
)  

SITE_ID = 1  
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Или 'mandatory' по желанию  
LOGIN_REDIRECT_URL = '/'  # Перенаправление после входа  