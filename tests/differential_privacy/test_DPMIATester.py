import pytest
import PETWorks.differential_privacy.DPMIATester as DPMIATester

@pytest.mark.skip(reason="Take too much time that GitHub action can tolerate. (Over than 30 mins)")
def testPETValidation():
    synthetic = "data/synthetic_NHANES.csv"
    original = "data/NHANES.csv"

    result = DPMIATester.PETValidation(synthetic, original)

    assert (
        result["Does the data processed with differential privacy"]
        == "Possibly Yes"
    )
