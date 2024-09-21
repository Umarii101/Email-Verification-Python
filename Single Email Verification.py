#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import dns.resolver
import smtplib

def is_valid_email_syntax(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def domain_exists(email):
    domain = email.split('@')[-1]
    try:
        # Query MX records
        mx_records = dns.resolver.resolve(domain, 'MX')
        return True if mx_records else False
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return False

def smtp_check(email):
    domain = email.split('@')[-1]
    try:
        # Get MX records for the domain
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)

        # Connect to the mail server
        server = smtplib.SMTP()
        server.connect(mx_record)
        server.helo('localhost')
        server.mail('me@mydomain.com')
        code, message = server.rcpt(email)
        server.quit()

        # 250 is the SMTP code for success
        return code == 250

    except Exception as e:
        print(f"SMTP Check Error: {e}")
        return False

def verify_email(email):
    if not is_valid_email_syntax(email):
        return "Invalid email syntax"
    if not domain_exists(email):
        return "Domain does not exist"
    if smtp_check(email):
        return "Email is valid"
    else:
        return "Email does not exist or SMTP check failed"

# Example usage
email = "Your Email here"
print(verify_email(email))


# In[ ]:




