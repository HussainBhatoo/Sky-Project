# Sky Engineering Registry — Login Credentials

This document contains the credentials for testing the authentication flow and administrative access.

> [!WARNING]
> These credentials are for **Development/Audit purposes only**. Never use simple passwords like these in a production environment.

### 1. Administrative Account (Superuser)
- **Role**: Full Access (Teams, Organisation, Messaging, Reports, Official Admin)
- **Username**: `admin`
- **Password**: `Sky2026!`
- **Portal Option**: Select **"Admin Login"** on the login page.

### 2. Test Engineer Account (Standard User)
- **Role**: Restricted Access (View Teams, Personal Messaging, Dashboard)
- **Username**: `testuser`
- **Password**: `Sky2026!`
- **Email**: `testuser@sky.com` (Required for signup domain validation)
- **Portal Option**: Standard Login.

### 3. Verification Steps
1. Navigate to `http://127.0.0.1:8000/accounts/login/`.
2. To test **Signup**: Navigate to `http://127.0.0.1:8000/accounts/signup/`.
3. Use the corporate email `@sky.com` or `@sky.uk`.

### 4. Full Credential Table
See `docs/test_credentials.md` for all team member accounts.
See `docs/coursework/credentials.md` for the canonical marker-facing guide.
