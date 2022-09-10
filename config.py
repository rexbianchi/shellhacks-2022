class Config(object):
    TESTING = False
    SECRET_KEY = "lonks-awakening"
    AWS_DEFAULT_REGION = "us-east-1"
    AWS_COGNITO_DOMAIN = "https://lonk.auth.us-east-1.amazoncognito.com"
    AWS_COGNITO_USER_POOL_ID = "us-east-1_MhQTATUKU"
    AWS_COGNITO_USER_POOL_CLIENT_ID = "6jqifnot174eb11pu8dmgg64i4"
    AWS_COGNITO_USER_POOL_CLIENT_SECRET = "6nmgatvssml96vdkeij573plgvumcforuj3uh1g8eg2bfjhsb4g"
    AWS_COGNITO_REDIRECT_URL = "http:///localhost:5000/logged_in/"
