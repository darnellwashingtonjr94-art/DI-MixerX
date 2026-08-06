class RequestParser:
    @staticmethod
    def extract_info(handler):
        return {
            "ip": handler.client_address[0],
            "path": handler.path,
            "method": handler.command,
            "user_agent": handler.headers.get('User-Agent', 'Unknown')
        }
