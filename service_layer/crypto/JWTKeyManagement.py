class JWTKeyManagement:
    @staticmethod
    def verify_jwt(jwt: str) -> dict:
        raise NotImplementedError

    @staticmethod
    def verify_jwt_payload(jwt_payload, verify_nonce=True) -> bool:
        raise NotImplementedError
