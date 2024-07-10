
### 1. Set Up Your Environment

1. **Clone This Repository**

2. **Create a Virtual Environment**
   Create and activate a virtual environment to manage dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required packages listed in `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

### 2. Generate the Model Using the Notebook

1. **Run Jupyter Notebook**
   Start Jupyter Notebook to open and run `notebook.ipynb`:
   ```sh
   jupyter notebook
   ```

2. **Run All Cells in the Notebook**
   Open `notebook.ipynb` in Jupyter Notebook and run all cells to generate `model.pkl`.

### 3. Set Up and Run the API

1. **Run the API Server**
   Run `app.py` to start the API server. Make sure that `model.pkl` is in the same directory as `app.py`:
   ```sh
   python app.py
   ```

### 4. Set Up and Run the Streamlit App

1. **Run the Streamlit App**
   Run `main.py` using Streamlit:
   ```sh
   streamlit run main.py
   ```
