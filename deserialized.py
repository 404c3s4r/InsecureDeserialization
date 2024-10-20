import pickle
import base64


serialized = "gASVJwAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAxuYyAtbHZwIDkwMDCUhZRSlC4=" 
deserialized_obj = pickle.loads(base64.b64decode(serialized))


