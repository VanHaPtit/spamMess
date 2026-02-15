import os
from django.core.wsgi import get_wsgi_application

# Thiết lập file settings mặc định cho dự án SMD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SMD.settings')

# Đây là biến mà Django đang báo thiếu
application = get_wsgi_application()