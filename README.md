# Wildlife Trade Intelligence Explorer

## 🧭 Project Overview
The Wildlife Trade Intelligence Explorer is a proof-of-concept data engineering project designed to model and visualize global wildlife trade flows. Built using real-world data from the CITES Trade Database and simulated illicit trafficking data, this project demonstrates core data engineering competencies including pipeline orchestration, data modeling, geospatial analysis, and network theory.

## ❓ Problem Statement
Illegal wildlife trafficking is a transnational issue that threatens biodiversity and fuels organized crime. Intelligence teams often rely on fragmented datasets that lack structure, context, and analytical insight. This project explores how structured trade data and modeled trafficking flows can be integrated and visualized to identify high-risk corridors, hub countries, and species under pressure.

## 🎯 Use Case & Impact
This tool is designed to support conservation intelligence teams by:
- Identifying high-volume trade corridors for specific species
- Highlighting transit hubs based on network centrality
- Surfacing trends in species trade over time
- Offering a foundation for layering additional OSINT/SIGINT data

## 📊 Outputs
- **Geospatial Map**: Interactive map of legal trade flows by species and country
- **Network Metrics**: Centrality scores and hub identification via NetworkX
- **Summary Tables**: CSV exports of top corridors and trade volumes

## ⚙️ Tech Stack
- **Python**: Core language for all scripting and analysis
- **Dagster**: Data pipeline orchestration
- **Pandas / GeoPandas**: Data transformation and spatial processing
- **NetworkX**: Route modeling and centrality analysis
- **Folium**: Geospatial visualization
- **SQLite**: Lightweight data storage
- **uv**: Environment and dependency management
- **Pytest**: Unit testing for transformation logic
- **GitHub Actions**: CI/CD for automated testing and linting

## 🔄 Data Transparency
- **CITES Trade Data**: Official database of reported international wildlife trade transactions. Only legal trade is represented here.
- **Synthetic Route Data**: A small set of manually curated trafficking route scenarios is included to simulate OSINT-style intelligence modeling. These are clearly labeled and not sourced from real interdiction data.

## 🧩 Limitations & Future Work
- This is a simplified proof-of-concept. Real trafficking data is rarely publicly accessible.
- Spatial overlays (e.g., deforestation, infrastructure) are not yet integrated.
- Future versions could include:
  - Live data ingestion from NGO endpoints
  - Real-time dashboards with anomaly detection
  - Integration with conservation databases and protected areas

## 🧠 Interview Talking Points
- **Problem → Goal → Design → Impact** narrative
- Why Dagster? Why this schema? What challenges?
- How trade routes were modeled as graphs
- What insights were uncovered through centrality metrics

## 🛠 Setup Instructions (Coming Soon)
Instructions for setting up the environment and running the pipeline will be added after initial development.

