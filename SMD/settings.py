import os

# Đường dẫn gốc của dự án
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Khóa bí mật (Trong thực tế nên để vào biến môi trường)
SECRET_KEY = 's@(m3481b-1)z44d3ems(ojv6vk7t=(qh@apqi1pzm=g1iv0hm'

# Chế độ Debug - Bật khi phát triển
DEBUG = True

# Cho phép tất cả các host truy cập trong môi trường dev
ALLOWED_HOSTS = ['*']

# Danh sách ứng dụng trong hệ thống
INSTALLED_APPS = [
    'Spam', # Ứng dụng chính xử lý nhận diện tin nhắn
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Các lớp Middleware xử lý bảo mật và phiên làm việc
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Tệp cấu hình URL chính
ROOT_URLCONF = 'SMD.urls'

# Cấu hình Hệ thống Giao diện (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Thư mục chứa các file HTML dùng chung
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

# Cấu hình WSGI
WSGI_APPLICATION = 'SMD.wsgi.application'

# Cơ sở dữ liệu SQLite mặc định
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Cấu hình Ngôn ngữ và Múi giờ Việt Nam
LANGUAGE_CODE = 'vi-vn' # Chuyển giao diện admin sang tiếng Việt
TIME_ZONE = 'Asia/Ho_Chi_Minh' # Đặt múi giờ Việt Nam
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --- Cấu hình Tệp Tĩnh (CSS, JavaScript, Images) ---
#
STATIC_URL = '/static/'
# Thư mục chứa các file static của bạn trong quá trình phát triển
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# Nơi Django sẽ thu gom tất cả file static khi chạy lệnh collectstatic (khi deploy)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# --- Cấu hình Media (Dành cho việc upload file nếu cần) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- Cấu hình cho Mô hình Học máy ---
# Giúp views.py truy cập thư mục chứa file .pkl một cách đồng nhất
ML_MODELS_DIR = os.path.join(BASE_DIR, 'Spam')

# # --- Điều hướng Đăng nhập/Đăng xuất ---
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'