from pathlib import Path

import pytest

from fileformats.vendor.canfield.medimage import VectraExport

from conftest import skip_if_no_export_test_data

pytestmark = skip_if_no_export_test_data


@pytest.mark.xfail(reason="Deidentification not implemented yet", strict=True)
def test_export_dir_validation(cleansed_export_dir: Path, tmp_path: Path) -> None:
    """Test that the ExportDir format is valid."""
    export_dir = VectraExport(cleansed_export_dir)
    deidentified = export_dir.deidentify(tmp_path)
    assert isinstance(deidentified, VectraExport)
