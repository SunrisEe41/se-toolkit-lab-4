"""Unit tests for item filtering and validation logic."""

import pytest
from pydantic import ValidationError

from app.models.item import ItemCreate, ItemUpdate


def test_item_create_with_default_type() -> None:
    """Test that ItemCreate uses 'step' as default type."""
    item = ItemCreate(title="Test Item")
    assert item.type == "step"


def test_item_create_with_default_description() -> None:
    """Test that ItemCreate uses empty string as default description."""
    item = ItemCreate(title="Test Item")
    assert item.description == ""


def test_item_create_with_parent_id_zero() -> None:
    """Test boundary case: parent_id=0 should be treated as falsy but valid."""
    item = ItemCreate(title="Test Item", parent_id=0)
    assert item.parent_id == 0
