import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sky_registry.settings')
django.setup()

from django.test import Client
from core.models import User

c = Client()
print('CHECK 5 — Live browser test (Django Test Client):')

# a) Admin Load
c.login(username='admin', password='Sky2026!')
response = c.get('/admin/core/user/')
passed = 'PASS' if response.status_code == 200 else 'FAIL'
print(f'a) Admin User list load: {passed}')

# b) Signup Rejection
c.logout()
response = c.post('/accounts/signup/', {
    'username': 'verify_test_001',
    'first_name': 'Verify',
    'last_name': 'Test',
    'email': 'test@gmail.com',
    'password1': 'short'
})
form = getattr(response, 'context', {}).get('form')
errors = str(form.errors) if form else ''
passed = 'PASS' if ('short' in errors or 'least 10' in errors or 'digit' in errors) or (response.status_code == 200 and b'least 10 character' in response.content) else 'FAIL'
print(f'b) Signup rejection (too short/complexity): {passed}')

# c) Signup Success Test
response = c.post('/accounts/signup/', {
    'username': 'verify_test_001',
    'first_name': 'Verify',
    'last_name': 'Test',
    'email': 'test@gmail.com',
    'password1': 'ValidPass1!'
})
passed = 'PASS' if response.status_code == 302 and 'login' in response.url else 'FAIL'
print(f'c) Signup success with valid password: {passed}')

# d) Profile Edit Test
c.login(username='verify_test_001', password='ValidPass1!')
response = c.post('/dashboard/profile/', {
    'first_name': 'Verify',
    'last_name': 'TestEdit',
    'email': 'test@gmail.com'
})
user = User.objects.get(username='verify_test_001')
passed = 'PASS' if user.last_name == 'TestEdit' else 'FAIL'
print(f'd) Profile edit persistence: {passed}')

# e) Admin Search
c.logout()
c.login(username='admin', password='Sky2026!')
response = c.get('/admin/core/user/', {'q': 'verify_test_001'})
passed = 'PASS' if response.status_code == 200 and b'verify_test_001' in response.content else 'FAIL'
print(f'e) Admin search appears: {passed}')

# f) Delete User
user = User.objects.get(username='verify_test_001')
response = c.post(f'/admin/core/user/{user.id}/delete/', {'post': 'yes'})
exists = User.objects.filter(username='verify_test_001').exists()
passed = 'PASS' if not exists else 'FAIL'
print(f'f) Delete verify_test_001 from admin: {passed}')
