
import pandas as pd
import pytest

from src.pipeline import transform_data


def make_record(**overrides):
    record = {
        "image_id": "IMG100",
        "capture_time": "2026-10-20T10:00:00Z",
        "width": 1920,
        "height": 1080,
        "label": "Vehicle",
        "confidence": 0.95,
        "file_path": "images/IMG100.jpg",
    }
    record.update(overrides)
    return record


def test_valid_record_is_cleaned():
    raw = pd.DataFrame([make_record()])

    clean, rejected = transform_data(raw)

    assert len(clean) == 1
    assert len(rejected) == 0
    assert clean.iloc[0]["label"] == "vehicle"
    assert clean.iloc[0]["pixel_count"] == 1920 * 1080


def test_invalid_width_is_rejected():
    raw = pd.DataFrame([make_record(width=0)])

    clean, rejected = transform_data(raw)

    assert len(clean) == 0
    assert rejected.iloc[0]["rejection_reason"] == "invalid_width"


def test_confidence_above_one_is_rejected():
    raw = pd.DataFrame([make_record(confidence=1.5)])

    clean, rejected = transform_data(raw)

    assert len(clean) == 0
    assert (
        rejected.iloc[0]["rejection_reason"]
        == "invalid_confidence"
    )


def test_duplicate_ids_are_both_rejected():
    raw = pd.DataFrame([
        make_record(),
        make_record(label="Person"),
    ])

    clean, rejected = transform_data(raw)

    assert len(clean) == 0
    assert len(rejected) == 2
    assert set(rejected["rejection_reason"]) == {
        "duplicate_image_id"
    }


def test_missing_required_column_raises_error():
    raw = pd.DataFrame([{"image_id": "IMG100"}])

    with pytest.raises(ValueError, match="Missing required columns"):
        transform_data(raw)


def test_image_below_minimum_width_is_rejected():
    raw = pd.DataFrame([make_record(width=200, height=480)])

    clean, rejected = transform_data(raw)

    assert len(clean) == 0
    assert rejected.iloc[0]["rejection_reason"] == "image_too_small"


def test_image_below_minimum_height_is_rejected():
    raw = pd.DataFrame([make_record(width=640, height=100)])

    clean, rejected = transform_data(raw)

    assert len(clean) == 0
    assert rejected.iloc[0]["rejection_reason"] == "image_too_small"
