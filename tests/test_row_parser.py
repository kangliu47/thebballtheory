import pytest
from bs4 import BeautifulSoup

from src.row_parser import (
    extract_primary_value,
    extract_percentage_with_made_attempted,
    extract_primary_percentage_value,
    extract_made_attempted,
    extract_z_score,
    extract_row_data,
)


# Fixtures to be used for testing
@pytest.fixture
def sample_col():
    html = """
        <td class="elite">
            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFblkzz" id="ContentPlaceHolder1_GridView1_HFblkzz_0" value="elite">
            <span id="ContentPlaceHolder1_GridView1_LBLK_0">3.9</span>
            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFBLK" id="ContentPlaceHolder1_GridView1_HFBLK_0" value="7.3685031363">
            <br><span id="ContentPlaceHolder1_GridView1_hi9_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">7.37</span>
        </td>
"""
    soup = BeautifulSoup(html, "html.parser")
    return soup.find("td")


@pytest.fixture
def sample_percentage_col():
    html = """
        <td>
            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFfgpzz" id="ContentPlaceHolder1_GridView1_HFfgpzz_0">
            <span id="ContentPlaceHolder1_GridView1_LFGP_0" class="float-start">0.473</span>
            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFFGP" id="ContentPlaceHolder1_GridView1_HFFGP_0" value="-0.0435170000">
            <span class="float-end small" style="font-size: 0.7em;">(8.8/18.6)</span>
            <br><span id="ContentPlaceHolder1_GridView1_hi12_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">-0.04</span>
        </td>
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.find("td")


@pytest.fixture
def sample_z_score_col():
    html = '<td><span class="badge">-0.04</span></td>'
    soup = BeautifulSoup(html, "html.parser")
    return soup.find("td")


# Test cases for individual functions
def test_extract_primary_value(sample_col):
    assert extract_primary_value(sample_col) == "3.9"


def test_extract_primary_percentage_value(sample_percentage_col):
    assert extract_primary_percentage_value(sample_percentage_col) == "0.473"


def test_extract_made_attempted(sample_percentage_col):
    made, attempted = extract_made_attempted(sample_percentage_col)
    assert made == "8.8"
    assert attempted == "18.6"


def test_extract_percentage_with_made_attempted(sample_percentage_col):
    expected_output = {"FG%": "0.473", "FGM": "8.8", "FGA": "18.6"}
    assert (
        extract_percentage_with_made_attempted(sample_percentage_col, "FG%")
        == expected_output
    )


def test_extract_z_score(sample_z_score_col):
    assert extract_z_score(sample_z_score_col) == "-0.04"


def test_extract_row_data(sample_row):
    headers = ["R#", "ADP", "PLAYER", "POS", "TEAM", "GP", "MPG", "FG%"]
    expected_output = {
        "R#": "1",
        "ADP": "3.5",
        "PLAYER": "Victor Wembanyama",
        "POS": "C",
        "TEAM": "SA",
        "GP": "70",
        "MPG": "31.1",
        "FG%": "0.473",
        "FGM": "8.8",
        "FGA": "18.6",
        "FG%_z_score": "-0.04",
    }
    assert extract_row_data(sample_row, headers) == expected_output
