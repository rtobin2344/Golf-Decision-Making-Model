# PGA Performance & Aggressiveness Analysis (2022 Season)

**Author:** Ryan Tobin  
**Course:** DATA 6560 – Sports Analytics  
**Primary Stakeholder:** PGA Tour players, coaches, and performance analysts  

## One-Line Summary
This project analyzes whether aggressive styles of play in professional golf are associated with higher payoff, measured through strokes gained and scoring outcomes, using PGA Tour tournament data from the 2022 season.

## Problem & Decision Context
Professional golfers routinely face strategic decisions between aggressive and conservative play (e.g., attacking pins, taking riskier lines). This project asks:

> **Do more aggressive playing styles produce better scoring outcomes, or do they simply increase volatility?**

The findings are intended to inform **course management strategy**, player coaching decisions, and performance evaluation.

## Dataset Overview
- **Source:** OpenDataBay (public PGA Tour–derived data)
- **Scope:** PGA TOUR tournaments, 2022 season
- **Row Definition:** One player–tournament observation
- **Key Variables:**
  - Strokes Gained (Total, Tee-to-Green, Putting, OTT, Approach)
  - Finishing position and score relative to par
  - Derived aggressiveness indicators

Due to restricted access to raw ShotLink shot-level data, this project relies on **strokes-gained and derived performance metrics**, which are widely used by the PGA TOUR and analysts.

## Method & Analytical Approach
The analysis follows a structured pipeline across course checkpoints:

- **CP4 – Preprocessing:** Cleaned and standardized tournament-level data; created aggressiveness metrics
- **CP5 – EDA:** Explored distributions, correlations, and subgroup differences
- **CP6 – Analysis Memo #1:** Baseline comparison of aggressive vs conservative player groups
- **CP7 – Analysis Memo #2:** Refined regression models evaluating aggressiveness while controlling for skill components (e.g., SG Putting)

Primary methods include:
- Group comparisons (high vs mid vs low aggressiveness)
- Correlation analysis
- OLS regression with evaluation via R² and effect sizes

## Key Results
- **High-aggressiveness players averaged +1.26 strokes gained per tournament**, compared to −2.22 for low-aggressiveness players.
- Group differences were **highly statistically significant (p < 0.001)**.
- Regression results show aggressiveness remains a strong predictor of performance even after controlling for putting and tee-to-green skill.
- Aggressive play increases upside but also increases performance variance.

## How to View or Reproduce
- Cleaned data (or sample slice) is available in `/data`
- Final analysis reports are in `/reports` (Checkpoints 1–8)
- Figures referenced in reports are stored in `/figures`
- Analysis was performed in Excel and Python (statsmodels)

To reproduce:
1. Open the cleaned dataset in `/data`
2. Review preprocessing rules in CP4
3. Run regression or group comparisons as documented in CP6–CP7

## Repository Structure
/data Cleaned data or sample slices
/reports Checkpoint 1–8 PDFs and Code
/figures Final charts used in EDA and analysis
README.md Project overview
