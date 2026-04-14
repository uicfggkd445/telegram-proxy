import os
from mtprotoproxy import MTProtoProxy

PORT = int(os.environ.get("PORT", 443))

proxy = MTProtoProxy(
    port=PORT,
    secret="abcdef1234567890abcdef1234567890"
)

proxy.run()
