import pyotp

from earth.config import otp_seed


totp = pyotp.TOTP('base32secret3232')
hotp = pyotp.HOTP('base32secret3232')


def otp_verify(otp, seed=None):
    if not seed:
        seed = otp_seed

    return hotp.verify(
        otp,
        totp.now() + seed
    )


def current_otp(seed=None):
    if not seed:
        seed = otp_seed

    return hotp.at(
        totp.now() + seed
    )
