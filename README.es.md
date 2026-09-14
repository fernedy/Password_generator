<div align="center">

[🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md)

</div>

<div align="center">

# 🔐 password_generator

**Contraseñas criptográficamente seguras, directo desde tu terminal.**

![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/CSPRNG-secrets-00A884?style=flat-square)
![Dependencies](https://img.shields.io/badge/dependencies-0-00A884?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)

</div>

---

Un generador de contraseñas pequeño y honesto: **cero dependencias**, construido sobre el módulo `secrets` de Python (generador aleatorio criptográficamente seguro) — nunca `random`, que es predecible e inseguro para fines de seguridad.

## ⚡ Uso

```bash
git clone https://github.com/fernedy/Password_generator.git
cd Password_generator

python password_generator.py                  # contraseña de 16 caracteres
# → k#9mXv2@pQz7!rDf   fuerte

python password_generator.py -l 32            # 32 caracteres
python password_generator.py -n 5             # lote de 5
python password_generator.py --no-ambiguous   # sin l 1 I O 0 (fácil de leer en voz alta)
python password_generator.py --no-symbols     # solo letras y números
```

## 🧪 Tests

```bash
python -m unittest discover -v
```

La suite de pruebas verifica cobertura de clases, longitud, reglas de exclusión, aleatoriedad y — importante — que el código use `secrets`, no `random`.

## 🤝 Contribuir

PRs bienvenidos: modo passphrase (`-m words`), copiar al portapapeles, estimación de fuerza estilo zxcvbn.

## 📜 Licencia

MIT — ver [LICENSE](LICENSE).

---

<div align="center">

Construido por [Fernedy Arias](https://github.com/fernedy) · AI First · Tech Explorer

</div>
