# Data Cleaning and Preprocessing

## Project Structure
project/
©¦
©À©¤©¤ data/
©¦ ©À©¤©¤ raw/ # Raw dataset
©¦ ©¸©¤©¤ processed/ # Cleaned dataset
©¦
©À©¤©¤ notebooks/
©¦ ©¸©¤©¤ preprocess.ipynb # Data cleaning and preprocessing notebook
©¦
©À©¤©¤ src/
©¦ ©¸©¤©¤ cleaning.py # Cleaning functions
©¦
©¸©¤©¤ README.md
## Usage
- Place the raw dataset into the `data/raw/` folder.

Open and run the notebook `notebooks/preprocess.ipynb`.

The cleaned dataset will be saved in `data/processed/cleaned_dataset.csv`.

## Clean strategy
This project applies the following data cleaning methods:

1.Fill Missing Values

 - Numerical columns: missing values are filled using the median (more robust than mean against outliers).

2.Drop Columns with Too Many Missing Values

 - Columns with more than 50% missing values are dropped.

3.Normalize Data

 - Numerical features are scaled to the [0, 1] range using MinMaxScaler.

## Assumptions

- All numerical columns are subject to missing value handling and normalization.

- Non-numerical (categorical) features are not processed in this workflow.

- The missing-value threshold is set to __50%__, but can be adjusted if needed.