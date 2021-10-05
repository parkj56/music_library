SECRET_KEY = 'django-insecure--s=befo&wqam(rgi5_#mh)ch5y58rmx6nvqnxu7h6(h=b07!mn'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_project_database',
        'USER': 'root',
        'PASSWORD': 'ssdd88',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}