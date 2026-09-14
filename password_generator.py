#!/usr/bin/env python3
"""
password_generator — Cryptographically secure passwords from your terminal.

Zero dependencies. Uses the `secrets` module (CSPRNG), never `random`.

Examples:
    python password_generator.py                    # 16-char password
    python password_generator.py -l 32              # 32-char password
    python password_generator.py -n 5               # generate 5 passwords
    python password_generator.py --no-ambiguous     # exclude l 1 I O 0
    python password_generator.py --no-symbols       # letters + digits only
"""
import argparse
import secrets
import string
import sys

AMBIGUOUS = set("l1IO0o")


def generate(length=16, symbols=True, exclude_ambiguous=False):
    if length < 4:
        raise ValueError("length must be at least 4")
    pool = string.ascii_letters + string.digits
    if symbols:
        pool += string.punctuation
    if exclude_ambiguous:
        pool = "".join(ch for ch in pool if ch not in AMBIGUOUS)
    # Guarantee at least one character from each selected class, then fill.
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    if symbols:
        password.append(secrets.choice(string.punctuation))
    while len(password) < length:
        password.append(secrets.choice(pool))
    secrets.SystemRandom().shuffle(password)
    return "".join(password[:length])


def strength_label(length, symbols):
    charset = 26 + 26 + 10 + (len(string.punctuation) if symbols else 0)
    entropy = length * (charset.bit_length())
    if entropy >= 100:
        return "🛡️  very strong"
    if entropy >= 80:
        return "🔒 strong"
    if entropy >= 60:
        return "⚠️  moderate"
    return "🚨 weak — use a longer password"


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="password_generator",
        description="Cryptographically secure password generator (stdlib only).")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="password length (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="how many passwords to generate (default: 1)")
    parser.add_argument("--no-symbols", action="store_true",
                        help="exclude special characters")
    parser.add_argument("--no-ambiguous", action="store_true",
                        help="exclude look-alike characters (l 1 I O 0 o)")
    args = parser.parse_args(argv)
    if args.length < 4 or args.length > 256:
        parser.error("length must be between 4 and 256")
    for _ in range(max(1, args.count)):
        pwd = generate(args.length, symbols=not args.no_symbols,
                       exclude_ambiguous=args.no_ambiguous)
        print(pwd)
    if sys.stdout.isatty() and args.count == 1:
        print(strength_label(args.length, not args.no_symbols), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
