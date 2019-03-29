import aiohttp 
API_TOKEN = "API_TOKEN"
PROXY_URL = "socks5://127.0.0.1:8000"
PROXY_AUTH = aiohttp.BasicAuth(login="login",password="password")