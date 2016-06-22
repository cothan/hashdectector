# HashDetector
A script for detect the hash type. To find out hash mode in hashcat and john the ripper 

```python
In [4]: import hashlib

In [5]: hashlib.md5('asdasd').hexdigest()

Out[5]: 'a8f5f167f44f4964e6c998dee827110c'
```
```
$python hashdetector.py a8f5f167f44f4964e6c998dee827110c
+-----------------------------+---------+-------------+----------+
| Hash Name                   | Hashcat | John        | Extended |
+-----------------------------+---------+-------------+----------+
| MD2                         | None    | md2         | False    |
| MD5                         | 0       | raw-md5     | False    |
| MD4                         | 900     | raw-md4     | False    |
| Double MD5                  | 2600    | None        | False    |
| LM                          | 3000    | lm          | False    |
| RIPEMD-128                  | None    | ripemd-128  | False    |
| Haval-128                   | None    | haval-128-4 | False    |
| Tiger-128                   | None    | None        | False    |
| Skein-256(128)              | None    | None        | False    |
| Skein-512(128)              | None    | None        | False    |
| Lotus Notes/Domino 5        | 8600    | lotus5      | False    |
| Skype                       | 23      | None        | False    |
| ZipMonster                  | None    | None        | True     |
| PrestaShop                  | 11000   | None        | True     |
| md5(md5(md5($pass)))        | 3500    | None        | True     |
| md5(strtoupper(md5($pass))) | 4300    | None        | True     |
| md5(sha1($pass))            | 4400    | None        | True     |
| md5($pass.$salt)            | 10      | None        | True     |
| md5($salt.$pass)            | 20      | None        | True     |
| md5(unicode($pass).$salt)   | 30      | None        | True     |
| md5($salt.unicode($pass))   | 40      | None        | True     |
| HMAC-MD5 (key = $pass)      | 50      | hmac-md5    | True     |
| HMAC-MD5 (key = $salt)      | 60      | hmac-md5    | True     |
| md5(md5($salt).$pass)       | 3610    | None        | True     |
| md5($salt.md5($pass))       | 3710    | None        | True     |
| md5($pass.md5($salt))       | 3720    | None        | True     |
| md5($salt.$pass.$salt)      | 3810    | None        | True     |
| md5(md5($pass).md5($salt))  | 3910    | None        | True     |
| md5($salt.md5($salt.$pass)) | 4010    | None        | True     |
| md5($salt.md5($pass.$salt)) | 4110    | None        | True     |
| md5($username.0.$pass)      | 4210    | None        | True     |
| Snefru-128                  | None    | snefru-128  | False    |
| NTLM                        | 1000    | nt          | False    |
| Domain Cached Credentials   | 1100    | mscach      | False    |
| Domain Cached Credentials 2 | 2100    | mscach2     | False    |
| DNSSEC(NSEC3)               | 8300    | None        | False    |
| RAdmin v2.x                 | 9900    | radmin      | False    |
| Cisco Type 7                | None    | None        | True     |
| BigCrypt                    | None    | bigcrypt    | True     |
+-----------------------------+---------+-------------+----------+
```
**Tips**: `-m` for HashCat and `--format=` for JtR

**Credit to HashID** I just make it more convenient for me


