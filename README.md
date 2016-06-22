# HashDetector
A script for detect the hash type. To find out hash mode in Hashcat and John the Ripper(JtR)

```python
In [4]: import hashlib

In [14]: hashlib.md5('Simple1@3').hexdigest()
Out[14]: 'e768b56b842787e56ecf841e8724accd'


In [7]: hashlib.sha1('Simple1@3').hexdigest()
Out[7]: '6320d911a82443ee35f0ab6b451e32a2bec4caa9'
```


```
$ python hashdetector.py 6320d911a82443ee35f0ab6b451e32a2bec4caa9 -v

[+] 6320d911a82443ee35f0ab6b451e32a2bec4caa9
+----------------------------+---------+-------------------+--------+
| Hash Name                  | Hashcat | John              | Salted |
+----------------------------+---------+-------------------+--------+
| SHA-1                      | 100     | raw-sha1          | False  |
| Double SHA-1               | 4500    | None              | False  |
| RIPEMD-160                 | 6000    | ripemd-160        | False  |
| LinkedIn                   | 190     | raw-sha1-linkedin | False  |
| sha1(sha1(sha1($pass)))    | 4600    | None              | True   |
| sha1(md5($pass))           | 4700    | None              | True   |
| sha1($pass.$salt)          | 110     | None              | True   |
| sha1($salt.$pass)          | 120     | None              | True   |
| sha1(unicode($pass).$salt) | 130     | None              | True   |
| sha1($salt.unicode($pass)) | 140     | None              | True   |
| HMAC-SHA1 (key = $pass)    | 150     | hmac-sha1         | True   |
| HMAC-SHA1 (key = $salt)    | 160     | hmac-sha1         | True   |
| sha1($salt.$pass.$salt)    | 4710    | None              | True   |
| BigCrypt                   | None    | bigcrypt          | True   |
+----------------------------+---------+-------------------+--------+
Useless Guess: Tiger-160 | Skein-512(160) | HAS-160 | MangosWeb Enhanced CMS | Haval-160 | Cisco Type 7 | Skein-256(160)

```
**Useless Guess** is the hash type doesn't work in both JtR and Hashcat

## Read from STDIN and filter Hashcat

```
$ python hashdetector.py -m

 >>> 6320d911a82443ee35f0ab6b451e32a2bec4caa9
 [+] 6320d911a82443ee35f0ab6b451e32a2bec4caa9

+----------------------------+---------+
| Hash Name                  | Hashcat |
+----------------------------+---------+
| SHA-1                      | 100     |
| Double SHA-1               | 4500    |
| RIPEMD-160                 | 6000    |
| LinkedIn                   | 190     |
| sha1(sha1(sha1($pass)))    | 4600    |
| sha1(md5($pass))           | 4700    |
| sha1($pass.$salt)          | 110     |
| sha1($salt.$pass)          | 120     |
| sha1(unicode($pass).$salt) | 130     |
| sha1($salt.unicode($pass)) | 140     |
| HMAC-SHA1 (key = $pass)    | 150     |
| HMAC-SHA1 (key = $salt)    | 160     |
| sha1($salt.$pass.$salt)    | 4710    |
+----------------------------+---------+

 >>> blob  
 [+] blob

None

```

## Read from file and filter JtR

```
$ python hashdetector.py hashes -j

[+] ea5687d14c4e8e1072528ad5ec2b8829cd1e2633

+-------------------------+-------------------+
| Hash Name               | John              |
+-------------------------+-------------------+
| SHA-1                   | raw-sha1          |
| RIPEMD-160              | ripemd-160        |
| LinkedIn                | raw-sha1-linkedin |
| HMAC-SHA1 (key = $pass) | hmac-sha1         |
| HMAC-SHA1 (key = $salt) | hmac-sha1         |
| BigCrypt                | bigcrypt          |
+-------------------------+-------------------+
[+] a8f5f167f44f4964e6c998dee827110c

+-----------------------------+-------------+
| Hash Name                   | John        |
+-----------------------------+-------------+
| MD2                         | md2         |
| MD5                         | raw-md5     |
| MD4                         | raw-md4     |
| LM                          | lm          |
| RIPEMD-128                  | ripemd-128  |
| Haval-128                   | haval-128-4 |
| Lotus Notes/Domino 5        | lotus5      |
| HMAC-MD5 (key = $pass)      | hmac-md5    |
| HMAC-MD5 (key = $salt)      | hmac-md5    |
| Snefru-128                  | snefru-128  |
| NTLM                        | nt          |
| Domain Cached Credentials   | mscach      |
| Domain Cached Credentials 2 | mscach2     |
| RAdmin v2.x                 | radmin      |
| BigCrypt                    | bigcrypt    |
+-----------------------------+-------------+
--End of file 'hashes'--
```

## Compare with original HashID 

```
$ hashid ea5687d14c4e8e1072528ad5ec2b8829cd1e2633 -j -m -e 
Analyzing 'ea5687d14c4e8e1072528ad5ec2b8829cd1e2633'
[+] SHA-1 [Hashcat Mode: 100][JtR Format: raw-sha1]
[+] Double SHA-1 [Hashcat Mode: 4500]
[+] RIPEMD-160 [Hashcat Mode: 6000][JtR Format: ripemd-160]
[+] Haval-160 
[+] Tiger-160 
[+] HAS-160 
[+] LinkedIn [Hashcat Mode: 190][JtR Format: raw-sha1-linkedin]
[+] Skein-256(160) 
[+] Skein-512(160) 
[+] MangosWeb Enhanced CMS 
[+] sha1(sha1(sha1($pass))) [Hashcat Mode: 4600]
[+] sha1(md5($pass)) [Hashcat Mode: 4700]
[+] sha1($pass.$salt) [Hashcat Mode: 110]
[+] sha1($salt.$pass) [Hashcat Mode: 120]
[+] sha1(unicode($pass).$salt) [Hashcat Mode: 130]
[+] sha1($salt.unicode($pass)) [Hashcat Mode: 140]
[+] HMAC-SHA1 (key = $pass) [Hashcat Mode: 150][JtR Format: hmac-sha1]
[+] HMAC-SHA1 (key = $salt) [Hashcat Mode: 160][JtR Format: hmac-sha1]
[+] sha1($salt.$pass.$salt) [Hashcat Mode: 4710]
[+] Cisco Type 7 
[+] BigCrypt [JtR Format: bigcrypt]
```

## With HashDectector
```
$ python hashdetector.py ea5687d14c4e8e1072528ad5ec2b8829cd1e2633 -j -m -e -v

[+] ea5687d14c4e8e1072528ad5ec2b8829cd1e2633
+----------------------------+---------+-------------------+--------+
| Hash Name                  | Hashcat | John              | Salted |
+----------------------------+---------+-------------------+--------+
| SHA-1                      | 100     | raw-sha1          | False  |
| Double SHA-1               | 4500    | None              | False  |
| RIPEMD-160                 | 6000    | ripemd-160        | False  |
| LinkedIn                   | 190     | raw-sha1-linkedin | False  |
| sha1(sha1(sha1($pass)))    | 4600    | None              | True   |
| sha1(md5($pass))           | 4700    | None              | True   |
| sha1($pass.$salt)          | 110     | None              | True   |
| sha1($salt.$pass)          | 120     | None              | True   |
| sha1(unicode($pass).$salt) | 130     | None              | True   |
| sha1($salt.unicode($pass)) | 140     | None              | True   |
| HMAC-SHA1 (key = $pass)    | 150     | hmac-sha1         | True   |
| HMAC-SHA1 (key = $salt)    | 160     | hmac-sha1         | True   |
| sha1($salt.$pass.$salt)    | 4710    | None              | True   |
| BigCrypt                   | None    | bigcrypt          | True   |
+----------------------------+---------+-------------------+--------+
Useless Guess: Tiger-160 | Skein-512(160) | HAS-160 | MangosWeb Enhanced CMS | Haval-160 | Cisco Type 7 | Skein-256(160)
```

**Tips**: `-m` for Hashcat and `--format=` for JtR

**Credit to HashID** I just make it more convenient for me