<div align="center">

[🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md)

</div>

<div align="center">

# 🔐 password_generator

**Cryptographically secure passwords, straight from your terminal.**

![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/CSPRNG-secrets-00A884?style=flat-square)
![Dependencies](https://img.shields.io/badge/dependencies-0-00A884?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)

</div>

---

A tiny, honest password generator: **zero dependencies**, built on Python's `secrets` module (a cryptographically secure random generator) — never `random`, which is predictable and unsafe for security purposes.

## ⚡ Usage

```bash
git clone https://github.com/fernedy/Password_generator.git
cd Password_generator

python password_generator.py                  # 16-char password
# → k#9mXv2@pQz7!rDf   strong

python password_generator.py -l 32            # 32 chars
python password_generator.py -n 5             # batch of 5
python password_generator.py --no-ambiguous   # no l 1 I O 0 (safe to read aloud)
python password_generator.py --no-symbols     # letters + digits only
```

## 🧪 Tested

```bash
python -m unittest discover -v
```

The test suite asserts class coverage, length, exclusion rules, randomness and — importantly — that the source uses `secrets`, not `random`.

## 🤝 Contributing

PRs welcome: passphrase mode (`-m words`), clipboard copy, zxcvbn-style strength estimation.

## 📜 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

Built by [Fernedy Arias](https://github.com/fernedy) · AI First · Tech Explorer

</div>
