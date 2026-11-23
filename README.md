# Market Research & Competitor Analysis Dashboard

A beginner-friendly Python + Streamlit project for studying market trends, competitor pricing and positioning, customer preferences, SWOT, and business opportunities.

## 1. Install prerequisites
- Install Python 3.10 or newer.
- Install Visual Studio Code.
- In VS Code, install the **Python** extension by Microsoft.

## 2. Open the project
1. Extract `market_research_competitor_analysis.zip`.
2. Open VS Code.
3. Choose **File → Open Folder** and select the extracted `market_research_competitor_analysis` folder.
4. Open **Terminal → New Terminal**.

## 3. Create and activate a virtual environment

Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:
```bat
.venv\Scripts\activate.bat
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install libraries
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Run the project
```bash
streamlit run app.py
```
Your browser should open the dashboard. If it does not, open the local URL printed in the terminal (usually `http://localhost:8501`).

## 6. Explore the dashboard
- **Market trends:** compare competitor growth and market-share mix.
- **Competitor comparison:** compare prices, ratings, market share, strengths, and weaknesses.
- **Customer preferences:** see preference themes.
- **SWOT & opportunities:** enter your own SWOT and download a text report.

## 7. Use your own research
Use `data/competitors.csv` as a template. Required columns:
`competitor, category, price, market_share, customer_rating, growth_rate, strength, weakness`
Optional column: `preferred_feature`

Upload your CSV from the dashboard sidebar. Keep units consistent (for example, all prices in INR and growth rates in percent). Record the source and collection date for every data point.

## 8. Suggested research workflow
1. Define industry, geography, target customer, and research question.
2. Identify 4–6 direct and indirect competitors.
3. Collect product/service details, prices, positioning, market-share estimates, ratings, and customer review themes.
4. Compare trends and identify gaps or underserved customer needs.
5. Complete SWOT using evidence, not assumptions.
6. Prioritize opportunities by customer demand, competitive gap, feasibility, cost, and risk.
7. Present 3–5 recommendations with evidence and next steps.

## Important
The bundled sample dataset is fictional demonstration data. Do not present it as real market research. Replace it with verified information and cite every external source in your final academic/business report.
