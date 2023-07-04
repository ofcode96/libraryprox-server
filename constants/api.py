class Api:
    BASE_URL: str = "/api/v1/"
    DATA_BASE: str = "library"
    DATA_BASE_URL: str = f"sqlite:///./{DATA_BASE}.db"
    JWT_SECRET = "udc2020"
