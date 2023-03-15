# dwie funkcje szyfrowania: sha i md5
from hashlib import md5, sha256, sha1
print(md5(b"Gruszka1").hexdigest())
print(sha256(b"Gruszka1").hexdigest())
print(sha1(b"Gruszka1").hexdigest())
