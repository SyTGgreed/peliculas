from jwt import encode,decode

def create_token(data:dict):
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")    # --> paylod es el contenido que va convertir en token
    return token

def validar_token(token:str) -> dict:
    data: dict = decode(token, key="my_secret_key",algorithms=['HS256'])
    return data