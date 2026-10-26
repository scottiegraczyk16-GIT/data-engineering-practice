
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "image_id",
    "capture_time",
    "width",
    "height",
    "label",
    "confidence",
    "file_path",
]


def load_data(path: str | Path) -> pd.DataFrame:
    """Load raw image metadata from a CSV file."""
    return pd.read_csv(path)


def transform_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Clean metadata and separate valid and rejected records."""

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    data = df.copy()

    # Normalize text fields.
    for column in ["image_id", "label", "file_path"]:
        data[column] = data[column].astype("string").str.strip()

    # Normalize labels: "vehicle" and "Vehicle" become "vehicle".
    data["label"] = data["label"].str.lower()

    # Parse fields that should contain numbers or timestamps.
    data["width"] = pd.to_numeric(data["width"], errors="coerce")
    data["height"] = pd.to_numeric(data["height"], errors="coerce")
    data["confidence"] = pd.to_numeric(
        data["confidence"], errors="coerce"
    )
    data["capture_time"] = pd.to_datetime(
        data["capture_time"], errors="coerce", utc=True
    )

    # Assign a rejection reason to each invalid record.
    reasons = pd.Series("", index=data.index, dtype="string")

    def reject(mask: pd.Series, reason: str) -> None:
        nonlocal reasons
        reasons = reasons.mask(
            mask & reasons.eq(""),
            reason,
        )

    reject(data["image_id"].isna() | data["image_id"].eq(""),
           "missing_image_id")
    reject(data["capture_time"].isna(), "invalid_capture_time")
    reject(data["width"].isna() | data["width"].le(0),
           "invalid_width")
    reject(data["height"].isna() | data["height"].le(0),
           "invalid_height")
           
    reject(
        data["width"].notna() & data["width"].gt(0)
        & data["width"].lt(320),
        "image_too_small",
    )
    reject(
        data["height"].notna() & data["height"].gt(0)
        & data["height"].lt(240),
        "image_too_small",
    )

    reject(data["label"].isna() | data["label"].eq(""),
           "missing_label")

    reject(
        data["confidence"].isna()
        | data["confidence"].ge(1.5)
        | data["confidence"].lt(0),
        "invalid_confidence",
    )
    reject(data["file_path"].isna() | data["file_path"].eq(""),
           "missing_file_path")

    # Reject every occurrence of a duplicated nonempty image ID.
    valid_id = data["image_id"].notna() & data["image_id"].ne("")
    duplicate_ids = data.loc[valid_id, "image_id"].duplicated(
        keep=False
    )
    reject(
        data.index.isin(duplicate_ids.index[duplicate_ids]),
        "duplicate_image_id",
    )

    data["rejection_reason"] = reasons

    rejected = data.loc[reasons.ne("")].copy()
    clean = data.loc[reasons.eq("")].copy()

    # Add a useful derived field for downstream processing.
    clean["pixel_count"] = clean["width"] * clean["height"]

    return clean, rejected


def run_pipeline(
    input_path: str | Path,
    output_dir: str | Path,
) -> None:
    """Run the complete CSV-to-clean-CSV pipeline."""

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_data = load_data(input_path)
    clean, rejected = transform_data(raw_data)

    clean.to_csv(output_dir / "clean_metadata.csv", index=False)
    rejected.to_csv(output_dir / "rejected_metadata.csv", index=False)

    print(f"Input records: {len(raw_data)}")
    print(f"Clean records: {len(clean)}")
    print(f"Rejected records: {len(rejected)}")
    print("\nRejection reasons:")
    print(rejected["rejection_reason"].value_counts().to_string())


if __name__ == "__main__":
    run_pipeline(
        "data/raw/image_metadata.csv",
        "data/processed",
    )
