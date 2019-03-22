import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1(d58ti3kx_zoux#s7fz_m_3l^6r0p_i#o!zc%v#vtx6!*--s3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

APPEND_SLASH = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',

    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'mama_cas',
    
    'sso.apps.auth',
    'sso.apps.sso',
    'sso.apps.users',
]
MAMA_CAS_SERVICES = [
    {
        'SERVICE': 'http://39.130.160.106:8000',
        'CALLBACKS': [
            'mama_cas.callbacks.user_model_attributes',
        ],
    },
    {
        'SERVICE': 'http://39.130.160.108:8001',
        'CALLBACKS': [
            'mama_cas.callbacks.user_model_attributes',
        ],
    },
]

if DEBUG:
    INSTALLED_APPS += ['rest_framework_swagger']

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True   # 指明在跨域访问中，后端是否支持对cookie的操作
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '39.130.160.106',
    '39.130.160.108',
)
CSRF_TRUSTED_ORIGINS = (
    '39.130.160.106',
    '39.130.160.108',
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
 
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

ROOT_URLCONF = 'sso.apps.sso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sso.apps.sso.wsgi.application'

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'sso',
       'USER':'postgres',
       'PASSWORD': 'mint@2016',
       'HOST': '39.130.160.107'
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache" # 另外还有个cached_db,这两个的区别是，cache只写缓存，cached_db除了写缓存还同时写数据库，如果对于session的安全性要求高可以选择cached_db
SESSION_COOKIE_AGE = 86400  # 设置session有效期为一天,默认两周
# SESSION_COOKIE_DOMAIN = ".superfishai.com"  # 此配置不能解决跨域问题，但是能解决a.ssotest.net与b.ssotest.net的session共享问题，不加此属性，跨站(非跨域)时，无法传递session
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 60 * 15 
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'sso.authentication.CrsfExemptSessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# allauth specific settings
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'sso.apps.auth.serializers.RegisterSerializer',
}

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'


try:
    from local_settings import *  # NOQA
except ImportError:
    pass

# ### ldap 配置部分BEGIN ### #
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',  # 配置为先使用LDAP认证，如通过认证则不再使用后面的认证方式
    'django.contrib.auth.backends.ModelBackend', # sso系统中手动创建的用户也可使用，优先级靠后。注意这2行的顺序
)

base_dn = 'dc=superfishai,dc=com'
AUTH_LDAP_SERVER_URI = 'ldap://49.4.7.114'
AUTH_LDAP_BIND_DN = 'cn=Captain,dc=superfishai,dc=com'
AUTH_LDAP_BIND_PASSWORD = '123456'
AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=People,%s' % base_dn, ldap.SCOPE_SUBTREE, "(uid=%(user)s)") # 用户的DN是uid=caojun,ou=People,dc=ssotest,dc=net，所以用uid
AUTH_LDAP_ALWAYS_UPDATE_USER = True  # This is the default, but I like to be explicit.

AUTH_LDAP_USER_ATTR_MAP = {  # key为数据库字段名，value为ldap中字段名，此字典解决django model与ldap字段名可能出现的不一致问题
    "username": "uid",
    "name": "cn",
    "email": "mail"
}

# 组权限管理 #
AUTH_LDAP_GROUP_SEARCH = LDAPSearch('ou=Group,dc=superfishai,dc=com', ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)")
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn") # 组的DN是cn=员工,ou=Group,dc=ssotest,dc=net，所以type是cn
AUTH_LDAP_USER_FLAGS_BY_GROUP = { # django admin的is_staff|superuser属性映射为ldap的管理员
    "is_staff": "cn=staff,ou=Group,dc=superfishai,dc=com",
    "is_superuser": "cn=superuser,ou=Group,dc=superfishai,dc=com"
}
AUTH_LDAP_REQUIRE_GROUP = "cn=superuser,ou=Group,dc=superfishai,dc=com"  # 只有此group可用ldap进行认证
AUTH_LDAP_DENY_GROUP = "cn=blacklist,ou=Group,dc=superfishai,dc=com"  # 此group不能使用ldap进行认证，直接deny掉，不会后续往django创建信息
AUTH_LDAP_MIRROR_GROUPS = True  # 直接把ldap的组复制到django一份，和AUTH_LDAP_FIND_GROUP_PERMS互斥.用户每次登录会根据ldap来更新数据库的组关系

# ### log 配置部分BEGIN ### #
LDAP_LOGS = os.path.join(BASE_DIR, 'logs/ldap.log')
stamdard_format = '[%(asctime)s][%(threadName)s:%(thread)d]' + \
                  '[task_id:%(name)s][%(filename)s:%(lineno)d] ' + \
                  '[%(levelname)s]- %(message)s'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {  # 详细
            'format': stamdard_format
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LDAP_LOGS,
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        '': {  # default日志，存放于log中
            'handlers': ['default'],
            'level': 'DEBUG',
        },
        'django_auth_ldap': {  # django_auth_ldap模块相关日志打印到console
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,  # 选择关闭继承，不然这个logger继承自默认，日志就会被记录2次了(''一次，自己一次)
        },
        # 'django.db.backends': {  # 数据库相关执行过程log打印到console
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        # },
    }
}

# ### log 配置部分END ### #