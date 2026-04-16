# Sky Engineering Registry — Login Credentials

This document contains the credentials for testing the authentication flow and administrative access.

> [!WARNING]
> These credentials are for **Development/Audit purposes only**. Never use simple passwords like these in a production environment.

### 1. Administrative Account (Superuser)
- **Role**: Full Access (Teams, Organisation, Messaging, Reports, Official Admin)
- **Username**: `admin`
- **Password**: `Admin1234!`
- **Portal Option**: Select **"Admin Login"** on the login page.

### 2. Test Engineer Account (Standard User)
- **Role**: Restricted Access (View Teams, Personal Messaging, Dashboard)
- **Username**: `test_engineer`
- **Password**: `TestPass123!`
- **Email**: `test.engineer@sky.com` (Required for signup domain validation)
- **Portal Option**: Standard Login.

### 3. Verification Steps
1. Navigate to `http://localhost:8004/accounts/login/`.
2. To test **Signup**: Navigate to `http://localhost:8004/accounts/signup/`.
3. Use the corporate email `@sky.com` or `@sky.uk`.
