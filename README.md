# Bad Deployable App

A Flask app with **intentionally outdated dependencies** for testing MiniPaaS security scanning.

## Known Issues
- Uses Python 3.9.7 (EOL, has CVEs)
- Flask 1.1.2 (multiple CVEs)
- Werkzeug 1.0.1 (CVE-2020-28734)
- Requests 2.25.0 (multiple CVEs)
- NumPy 1.19.0 (multiple CVEs)

## Why This Should Fail Security Scan
The security scanner will detect:
- CRITICAL vulnerabilities in base image (Python 3.9.7)
- HIGH/CRITICAL vulnerabilities in dependencies
- Should be BLOCKED from deployment
