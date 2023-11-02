### Assignment Objective:

To perform portfolio optimization using Python's SciPy package and data from WRDS (Wharton Research Data Services). Your portfolio must include at least 5 stocks. Compare portfolios with and without the inclusion of a Fixed Income security.

### Prerequisites:

- Python programming skills
- Basic understanding of finance and portfolio theory
- Access to WRDS for data retrieval

### Resources:

- Equity Data: [WRDS CRSP and Compustat in Python](https://www.tidy-finance.org/python/wrds-crsp-and-compustat.html)
- [Less general, but Easier way to Connect to WRDS](https://github.com/CinderZhang/FinnData/blob/main/WRDS.py)
- Fixed Income Data: [WRDS Bond Returns](https://wrds-www.wharton.upenn.edu/pages/get-data/wrds-bond-returns/) and [TRACE and FISD in Python](https://www.tidy-finance.org/python/trace-and-fisd.html)
- Code Sample for Portfolio Optimization: [Towards Data Science Article](https://towardsdatascience.com/efficient-frontier-portfolio-optimisation-in-python-e7844051e7f)

### Steps:

1. **Data Retrieval (Note that you may not need all the datasets. Research what you really need/must use)**:
    - Retrieve stock data using Python code from [WRDS CRSP and Compustat in Python](https://www.tidy-finance.org/python/wrds-crsp-and-compustat.html).
    - Retrieve fixed income data using Python code from [WRDS Bond Returns](https://wrds-www.wharton.upenn.edu/pages/get-data/wrds-bond-returns/) and [TRACE and FISD in Python](https://www.tidy-finance.org/python/trace-and-fisd.html).

2. **Data Preprocessing**:
    - Clean and format the data for analysis.
    - Calculate the returns for each asset.

3. **Portfolio Construction**:
    - Select at least 5 stocks and optionally 1 fixed income security for your portfolio.
    - Use the SciPy package to calculate the Efficient Frontier for portfolios with and without fixed income (hint: Sharpe Ratio. Research it if you forget what the ratio is and what it is used for.).

4. **Optimization**:
    - Use SciPy's optimization functions to find the optimal portfolio weights.
    - Include constraints if you opt for a fixed income security in your portfolio.

5. **Analysis and Visualization**:
    - Plot the Efficient Frontier for both scenarios.
    - Analyze the optimal portfolios, discussing the impact of including or excluding the fixed income security.

6. **Report**:
    - Summarize your findings, methodologies, and any challenges you faced during the assignment.

7. **Code Submission**:
    - Submit your Python code along with the report.

### Evaluation Criteria:

- Code Quality and Efficiency
- Data Preprocessing Techniques
- Understanding and Application of Portfolio Theory
- Quality of Analysis and Interpretation
- Report Presentation

### Deep Dive:

- Explore how the inclusion or exclusion of a fixed income security affects the risk and return profile of the portfolio.
- Investigate the role of diversification across asset classes.

### ChatGPT Grading Prompts:

Self-Assessment Prompts:
As part of this assignment, you are required to construct your own grading prompts. These prompts should be questions or statements that guide the evaluation of your work. Think critically about what aspects of your assignment you believe are most important and formulate prompts accordingly.

For example, you might ask about the efficiency of your code, the depth of your analysis, or how well you've applied financial theories. The prompts you create will be used for your self-assessment as well as for external evaluation.

By creating your own grading prompts, you engage in a deeper level of reflection about your work, which is an essential skill in both academic and professional settings.
