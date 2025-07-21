# Wildlife Trade Intelligence Explorer (WTIE)

## 🧭 Overview

WTIE is a data engineering proof of concept that models legal wildlife trade flows and simulates illicit trafficking routes. Built using real CITES data and synthetic scenarios, it supports conservation intelligence teams with rich geospatial and graph-based insights. This project was created as part of a technical interview for Langland Conservation.

---

## ⚡️ Key Features

- Dagster pipeline with grouped assets (`ingestion`, `outputs`)
- Geospatial trade route map (Folium)
- NetworkX graph model with degree centrality metrics
- Summary tables of top species, countries, and trade corridors
- 96% test coverage (Pytest + Coverage)
- CI/CD with GitHub Actions + Pre-commit hooks

---

## ❓ Problem

Illegal wildlife trafficking is a complex, transnational crime that threatens biodiversity and fuels organized networks. Public datasets like the CITES Trade Database provide insight into legal trade, but rarely capture illicit flows. Intelligence teams need tools that can integrate structured data, model suspicious activity, and surface actionable insights.

## 🎯 Purpose

This tool was designed to:

- Highlight high-volume legal trade corridors by species and country
- Identify potential hub nations via network centrality analysis
- Simulate suspicious (synthetic) routes for investigative comparison
- Lay the groundwork for integrating OSINT/SIGINT-style overlays

## 📊 Outputs

- **🗺 Geospatial Map**: `outputs/trade_routes_map.html`
- **📈 Network Graph Summary**: Displayed in `notebooks/wtie_exploration.ipynb`
- **📋 Tables**: Top species, countries, and trade corridors (shown in notebook)

---

## ⚙️ Tech Stack

- **Dagster** – Orchestration of ingestion, modeling, and outputs
- **Pandas / GeoPandas** – Transformation and spatial joins
- **NetworkX** – Graph construction and metrics
- **Folium** – Interactive route mapping
- **uv** – Dependency management
- **Pytest** – Lightweight unit testing
- **GitHub Actions** – CI for formatting and test checks

---

## 🌍 Coordinate Challenges

CITES data includes country ISO codes, but not coordinates. Initially, a small centroid file caused visual errors. We resolved this by switching to a broader dataset from [Gavin Rehkemper’s open data repo](https://gavinr.com/open-data/world-countries-centroids/), mapping all valid ISO codes to latitude and longitude. Legacy codes (e.g. `SU`, `YU`, `ZC`) are skipped with warnings.

---

## 🧪 Data Strategy

- **CITES Trade Database**: Official, legal trade shipments (CSV)
- **Synthetic Trafficking Scenarios**: Manually defined illicit routes, labeled with a `synthetic=True` flag
- **Permit IDs**: Anonymized using hashed random identifiers to simulate real shipment linkage

---

## 🧭 Ethical Use of Data

Synthetic routes are generated for illustrative purposes only and do not represent real trafficking intelligence. This project follows ethical OSINT simulation practices and data minimization principles.

---

## ▶️ Quickstart

```bash
uv venv
uv sync
uv run dagster dev
```

Then open `notebooks/wtie_exploration.ipynb` to explore the data and view the map and summary tables inline.

---

## 🧪 Testing

```bash
uv run pytest
```

- 96% test coverage enforced locally and via CI
- Pre-commit hooks check formatting and test status before push

---

## 🤖 Agentic Collaboration & Tooling

This project was iteratively designed and developed using agentic coding tools. The initial concept and architecture were refined through collaborative critique with Claude (Anthropic) and Gemini (Google), focusing on narrative clarity and technical feasibility. The implementation sprint was then executed in close pair programming collaboration with ChatGPT (OpenAI), leveraging its structured reasoning and context awareness to design robust pipelines, debug efficiently, and optimize code quality. This agentic workflow enabled rapid prototyping, thoughtful iteration, and adherence to security-conscious best practices throughout.
