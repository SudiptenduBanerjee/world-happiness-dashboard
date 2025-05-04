 An intermediate-level Data Analytics project analyzing the World Happiness Report dataset.

 ## Project Overview
 - **Dataset**: World Happiness Report 2019
 - **Tools**: Python, Pandas, Matplotlib, Seaborn, Plotly, Streamlit
 - **Features**:
   - Exploratory Data Analysis (EDA) in Jupyter Notebook
   - Interactive dashboard with Streamlit
   - Visualizations of happiness scores, GDP correlations, and more

 ## Setup
 1. Install Anaconda and create a virtual environment:
    ```bash
    conda create -n happiness_project python=3.9
    conda activate happiness_project
    pip install pandas numpy matplotlib seaborn plotly streamlit
    ```
 2. Run the EDA notebook (`eda.ipynb`) to generate visualizations.
 3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

 ## Deployment
 The app is deployed on Streamlit Community Cloud: [https://sudiptendubanerjee-world-happiness-dashboard.streamlit.app](https://sudiptendubanerjee-world-happiness-dashboard.streamlit.app)

 ## Future Improvements
 - Add time-series analysis for multiple years.
 - Include machine learning to predict happiness scores.
 - Enhance UI with custom CSS.
