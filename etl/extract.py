from pathlib import Path

import pandas as pd


def extract_csv(file_path: Path) -> pd.DataFrame:
    """
    Read a CSV file and return it as a pandas DataFrame.

    Parameters
    ----------
    file_path : Path
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    df = pd.read_csv(file_path)
    return df