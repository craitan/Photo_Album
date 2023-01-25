<h1 align=center>Dream catcher</h1>
<h3 align=center>
A stylish website for uploading your photos built with Django and Python.<br>
Final project for the Web Framework Course in Software University.<br>
<br>
<a href='https://dream-catcher.online/'> Click here to see the deployed project </a>
<br><br>

[About](#about) | [Installation](#installation) | [Urls](#urls) | [License](#license)

</h3>
	 
</div>

<!-- ABOUT -->
## About

<p align='justify'>
The site is fully functional. It has a lot of features as:<br><br>
 - It has a log in, log out system.<br>
 - There are two types of users - normal and administrators.<br>
 - It has a public part, accessible by both authorized and non-authorized viewers.<br>
 - It has a private part - functionalities that only authorized users can use.<br>
 - Some of the features of the private part are usable only by superusers.<br>
 - The project is deployed in AWS.<br>
 - The storage used for saving photos, uploaded by users is AWS bucket .<br>
</p>
<br>
This is my second actual web project and here is the tech stack used so far:
<br><br>

[![My Skills](https://skillicons.dev/icons?i=py,django,html,css,bootstrap,docker,github,postgres,aws)](https://skillicons.dev)
<br><br>

<!-- INSTALLATION -->
## Installation

<h4>First you should do two things:</h4>

```bash
git clone https://github.com/craitan/Photo_Album.git
```
	
```bash
pip install -r requirements.txt
```
***Note: If you are on a Mac, change "psycopg2" to "psycopg2-binary" in requirements.txt before running the command above!***

<br>

<h4>Next you should configure your "settings.py" file by either changing values below (like env['SECRET_KEY'])<br>
or setting them up in a .env file: </h4>

```python
SECRET_KEY = config('SECRET_KEY') # Change to a valid secret key or set it up in a .env file

DEBUG = int(config('DEBUG', 1)) # Change to True/False or set it up in a .env file

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(' ') # Change to valid hosts or set them in .env file
```


<h4>Do the same for your database configuation:</h4>
	
```python
DATABASES = {
    'default': {
        'ENGINE': config['DB_ENGINE'],
        'NAME': config['DB_NAME'],
        'USER': config['DB_USER'],
        'PASSWORD': config['DB_PASSWORD'],
        'HOST': config['DB_HOST'],
        'PORT': config['DB_PORT'],
    }
}
```

<h4>Or use the default database configuration:</h4>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
	
<h4>If you want to use cache, you can configure it as well:</h4>

```python
CACHES = {
    'default': {
        'BACKEND': config['CACHE_BACKEND'],
        'LOCATION': config['CACHE_LOCATION'],
    },
}
```

<h4>Set AWS bucket:</h4>

```python
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE'), # Change to valid AWS bucket file storage or set it up in .env file

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID'), # Change to valid AWS bucket access key or set it up in .env file
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY'), # Change to valid AWS bucket secret access key or set it up in .env file

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME'), # Change to valid AWS storage bucket name or set it up in .env file
```

<!-- URLS -->
## Urls

<h4>The application integrates the following urls for each application:</h4>

<h4>Main urls:</h4>
	
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Photo_Album.common.urls')),
    path('accounts/', include('Photo_Album.accounts.urls')),
    path('photos/', include('Photo_Album.photos.urls')),
]
```
<h4>Common:</h4>
	
```python
urlpatterns = (
    path('', (HomePageView.as_view()), name='home page'),
    path('contact-us/', ContactView.as_view(), name='contact us')
)
```
<h4>Accounts:</h4>
	
```python
urlpatterns = (
    path('register/', SignUpView.as_view(), name="register user"),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),

    ]))
)
```
<h4>Photos:</h4>
	
```python
urlpatterns = (
    path('', PhotoGalleryView.as_view(), name='photo gallery'),
    path('add/', add_photo, name='photo add'),
    path('view/<int:pk>', PhotoView.as_view(), name='photo view'),
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo delete'),
    path('category/<int:pk>', CategoryDeleteView.as_view(), name='category delete'),

)
```


<!-- LICENSE -->
## License

Distributed under the [MIT](https://github.com/craitan/Photo_Album/blob/new_branch/License.md) License.


