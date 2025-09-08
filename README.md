# Any Given Sunday 🏈

![Build](https://img.shields.io/github/actions/workflow/status/SWilford/Any-Given-Sunday/ci.yml?branch=main)
![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/github/license/SWilford/Any-Given-Sunday)

Probabilistic NFL game predictions with a transparent, reproducible pipeline.
Built with Python, FastAPI, scikit-learn, and PostgreSQL — deployed on cloud infra (Render/Railway).

---

## 🚀 Features (planned)

- Automated ingestion of NFL game data
- Feature engineering (team form, rolling stats, home/away, rest days)
- Machine learning model (baseline logistic regression → gradient boosting upgrade path)
- FastAPI service with `/predict` and `/health` endpoints
- PostgreSQL backend for features, predictions, and API logs
- Optional Streamlit demo frontend
- CI/CD with GitHub Actions, pre-commit hooks, and unit tests

---

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Frameworks:** FastAPI, scikit-learn, pandas
- **Database:** PostgreSQL
- **Infra:** Docker, GitHub Actions, Render/Railway
- **Tooling:** Ruff, Black, Pytest, Pre-commit

---

## 📈 Roadmap

- [ ] Data ingestion (historical games)
- [ ] Feature engineering
- [ ] Baseline model
- [ ] FastAPI `/predict`
- [ ] Deploy to Render/Railway
- [ ] Add demo frontend
