#!/usr/bin/env python
"""Script to test sending email given an address and SMTP server

Kudos: http://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/"""
import argparse
import email
from getpass import getpass
import smtplib
import sys

parser = argparse.ArgumentParser(
    description="Testing sending email with given addess and SMTP server"
    )
parser.add_argument('gmail_account', type=str, help="Gmail user account")
parser.add_argument('to', type=str, help="Email recipient")
args = parser.parse_args()

print "Sending to %s" % args.to
passwd = getpass("Enter password for %s:" % args.gmail_account)

msg = email.MIMEText.MIMEText("Message text goes here")
msg["Subject"] = "Test email"
msg["To"] = args.to
msg["From"] = args.gmail_account

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(args.gmail_account, passwd)
smtpserver.sendmail(args.gmail_account, args.to, msg.as_string())
smtpserver.close()

print "Done."
sys.exit(0)

