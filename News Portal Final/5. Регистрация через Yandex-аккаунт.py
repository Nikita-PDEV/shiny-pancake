AUTHENTICATION_BACKENDS += [  
    'allauth.socialaccount.providers.yandex.provider.YandexOAuth2'  
]  

SOCIALACCOUNT_PROVIDERS = {  
    'yandex': {  
        'METHOD': 'oauth2',  
        'SCOPE': ['info', 'login'],  
        'OAUTH2_SCOPE': ['login'], 
    }  
}  