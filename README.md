# Financial Metrics Analysis Across Market Types  

This study analyzes financial and market data for A-share listed firms in China to evaluate key performance indicators and compare trends across market types. The research leverages the **CSMAR database** and proceeds as follows:  

---

## **Data Collection**  
The dataset comprises three categories:  
1. **Monthly Market Data** (Jan. 2000–Sep. 2023)  
   - Stock prices  
   - Stock returns  
   - Market value of tradable shares  

2. **Quarterly Financial Statements** (2000Q1–2023Q3)  
   - Total assets & liabilities  
   - Earnings per share (EPS)  
   - ROA, ROE  
   - R&D expenses  

3. **Firm-Specific Information**  
   - Establishment date  
   - Market type (Main Board vs. GEM Board)  

---

## **Methodology**  

### (a) Ratio Derivation  
- **Monthly Metrics**:  
  - **P/E Ratio**: Stock price divided by quarterly EPS (annualized for monthly alignment).  
  - **P/B Ratio**: Stock price divided by book value per share (total assets minus liabilities).  

- **Quarterly Metrics**:  
  - **R&D Intensity**: R&D expenses relative to total assets.  
  - **Firm Age**: Time elapsed since establishment date.  

### (b) Comparative Analysis  
Summary statistics are calculated for:  
- **Monthly Variables**: Stock returns, P/E, P/B ratios.  
- **Quarterly Variables**: ROA, ROE, R&D intensity, firm age.  

Key statistics include:  
- Observation count  
- Mean, median  
- 25th and 75th percentiles (p25, p75)  
- Standard deviation  

Results are segmented by **market type** (Main Board vs. GEM Board) to identify structural differences in:  
- Valuation (P/E, P/B)  
- Profitability (ROA, ROE)  
- Innovation investment (R&D intensity)  
- Firm maturity (age)  

---

## **Objective**  
By bridging raw financial data with actionable insights, this analysis aims to:  
1. Highlight methodological rigor in metric derivation.  
2. Uncover cross-market disparities in performance and risk profiles.  
3. Provide implications for investors and policymakers.
