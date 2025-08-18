## Data Storage

### Folder Structure

```
homework5/
©À©¤©¤ data/
©¦   ©À©¤©¤ raw/          # Stores raw data files (CSV format)
©¦   ©¸©¤©¤ processed/    # Stores cleaned/processed data files (Parquet format)
©À©¤©¤ notebooks/
©¦   ©¸©¤©¤ stage05_data-storage-preview_homework.ipynb
©À©¤©¤ src/
©¦   ©¸©¤©¤ storage.py    # Data reading/writing utility functions
©À©¤©¤ .env
©¸©¤©¤ README.md
```

### Formats Used

- **CSV (.csv)**
  - Used for raw, readable, and portable storage of tabular data.
  - Saved in: `data/raw/`

- **Parquet (.parquet)**
  - Used for processed data with better compression and faster read/write.
  - Saved in: `data/processed/`

### Environment Variables

Environment variables are defined in `.env` and loaded using `python-dotenv`:

```
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

These variables are used in the code to dynamically control where files are saved and loaded from.

### Data Read/Write Utilities

Custom utility functions (defined in `src/storage.py`):

- `write_df(df, path)` ¨C Saves a DataFrame based on file suffix (`.csv` or `.parquet`)
- `read_df(path)` ¨C Loads the DataFrame, with datetime parsing for `date` column
- `validate_loaded(original, reloaded)` ¨C Verifies:
  - Shapes match
  - `date` column is datetime
  - `price` column is numeric

### Validation Logic

Checks performed during validation:

- `shape_equal`: The original and reloaded DataFrames have the same shape.
- `date_is_datetime`: The `'date'` column is a valid datetime dtype.
- `price_is_numeric`: The `'price'` column is numeric.

These help ensure that serialization/deserialization does not lose data fidelity.

### Assumptions & Risks

- Assumes presence of `date` and `price` columns in the DataFrame.
- Assumes `.csv` files are clean and well-formed.
- Parquet support requires `pyarrow` or `fastparquet` installed.
- Missing directories will be created automatically by the script.
- If a Parquet engine is not available, a clear error will be raised.
