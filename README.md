# CMPS 315 - Programming Assignment 1: Password Cracking

This program performs a dictionary attack on salted MD5 password hashes for CMPS 315 PA1.

## Requirements

- Python 3
- `pa1.py`
- `shadow.txt` in the same directory
- `rockyou.txt` in the same directory

No third-party Python packages are required; the program uses Python's built-in `hashlib` module.

## Run

From this directory, run:

```bash
python3 pa1.py
```

The program reads `shadow.txt` and `rockyou.txt`, displays each username, salt, hash, and recovered password in the terminal, and then prints the number of cracked and uncracked hashes.

## Submission

The assignment specification requests submission of `pa1.py`. The input files are required only to run and test the program locally.
