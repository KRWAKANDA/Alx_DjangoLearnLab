# Security Hardening - LibraryProject

## Summary of changes
- DEBUG set to False (production).
- SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF set.
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE enabled (HTTPS required).
- CSP configured (via django-csp or manual middleware).
- All forms include `{% csrf_token %}` in templates.
- Views use Django Forms and ORM filters — prevents SQL injection.
- Views decorated with `@permission_required` and `@require_http_methods`.

## How to test
1. Run migrations and create test users/groups with permissions.
2. Test form submissions: ensure POST forms are blocked without CSRF token.
3. Test search: enter SQL-like strings — should not inject or break DB.
4. Check HTTP response headers for:
   - `X-Frame-Options: DENY`
   - `X-Content-Type-Options: nosniff`
   - `X-XSS-Protection: 1; mode=block` (some browsers)
   - `Content-Security-Policy` header (if configured)
5. Ensure cookies have `Secure` flag in HTTPS mode.

## Notes
- Many settings require HTTPS. For local dev, you might temporarily set `CSRF_COOKIE_SECURE=False` and `SESSION_COOKIE_SECURE=False`.
- CSP must be tuned to allow any external resources your app uses.
