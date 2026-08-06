import base64
import random
import json

class PayloadObfuscator:
    @staticmethod
    def obfuscate(payload_dict):
        json_str = json.dumps(payload_dict)
        methods = ['none', 'base64', 'hex']
        chosen = random.choice(methods)

        if chosen == 'base64':
            return {"data": base64.b64encode(json_str.encode()).decode(), "encoding": "base64"}
        elif chosen == 'hex':
            return {"data": json_str.encode().hex(), "encoding": "hex"}
        
        return payload_dict
