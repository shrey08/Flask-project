import os

class Config(object):
	SECRET_KEY = os.environ.get("SECRET_KEY") or b'\xc7&\xf8|\\\xf1P\xefq\xd2\x16\x9c%+\x9a\n'

	MONGODB_SETTINGS = {'db':'UTA_Enrollment'}