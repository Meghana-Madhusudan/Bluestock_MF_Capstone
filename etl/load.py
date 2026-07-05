from pathlib import Path

import pandas as pd


def save_csv(df: pd.DataFrame, output_path: Path) -> None:
    """
    Save a DataFrame to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save.
    output_path : Path
        Destination path for the CSV file.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)