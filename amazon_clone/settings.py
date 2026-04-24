# settings.py

# 1. تفعيل وضع التصحيح لرؤية الأخطاء بالتفصيل على Railway
DEBUG = True

# 2. السماح برابط موقعك الجديد والروابط المحلية
ALLOWED_HOSTS = [
    'web-production-0f067.up.railway.app', 
    '127.0.0.1', 
    'localhost'
]

# --- إعدادات التطبيقات المثبتة وقواعد البيانات تبقى كما هي في الأعلى ---

# 3. إعدادات اللغة والوقت (للعربية)
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 4. إعدادات الملفات الثابتة (CSS, JS)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 5. إعدادات ملفات الميديا (الصور التي ترفعها من جوالك)
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 6. إعداد افتراضي لنوع حقل المعرف الأساسي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
