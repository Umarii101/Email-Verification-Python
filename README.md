# Email-Verification-Python

This is a Python program to verify email addresses using multiple steps:
- **Syntax Validation**: Checks if the email follows the correct syntax.
- **Domain Verification**: Queries DNS to check if the email's domain has valid MX records (mail servers).
- **SMTP Check**: Connects to the domain’s mail server to verify if the email address exists.

## Features
- Easy email verification using Python.
- Handles errors gracefully and prints descriptive messages for failed checks.
- Performs a real-time SMTP check to confirm the existence of the email address.

## Requirements

You will need:
- Python 3.x
- The following Python packages:
  - `dnspython`: For DNS lookup to check domain MX records.
  - `smtplib`: For performing the SMTP check (this is part of Python’s standard library, so no need to install it separately).

To install the required package, you can use:
```bash
pip install -r requirements.txt
