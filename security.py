# security.py

import pyotp
from config import SECURITY_CONFIG

class Security:
    def __init__(self):
        self.mfa_method = SECURITY_CONFIG['mfa_method']
        self.mfa_key = SECURITY_CONFIG['mfa_key']
        self.totp = pyotp.TOTP(self.mfa_key)

    def generate_otp(self):
        return self.totp.now()

    def verify_otp(self, otp):
        return self.totp.verify(otp)

    def authenticate(self, user_otp):
        if self.verify_otp(user_otp):
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False

if __name__ == "__main__":
    security = Security()
    otp = security.generate_otp()
    print("Generated OTP: ", otp)
    user_otp = input("Enter the OTP: ")
    security.authenticate(user_otp)