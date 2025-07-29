# pdhs

## Motivation

Access to high-quality, structured, and timely demographic and health data is essential for researchers, policymakers, and public health professionals. The Demographic and Health Surveys (DHS) program provides a rich repository of standardized datasets across countries and years, yet accessing and working with this data programmatically can be cumbersome due to inconsistencies in interfaces, authentication, and formatting.

The `pdhs` Python library aims to streamline and simplify interaction with the DHS API, offering an intuitive, well-documented, and Pythonic interface for querying, retrieving, and managing DHS datasets. By abstracting away low-level API details, `pdhs` empowers users to focus on analysis and application rather than data wrangling. It facilitates reproducible research, supports integration with data science workflows (e.g., pandas, numpy, matplotlib), and encourages broader use of DHS data in academic, development, and policy environments.

In short, `pdhs` bridges the gap between powerful public data and the tools needed to extract meaningful insight from it.

-----

`pdhs` is a package for management and analysis of [Demographic and
Health Survey (DHS)](https://www.dhsprogram.com) data. This includes
functionality to:

1.  Access standard indicator data (i.e. [DHS
    STATcompiler](https://www.statcompiler.com/)) in Python via the [DHS
    API](https://api.dhsprogram.com/).
2.  Identify surveys and datasets relevant to a particular analysis.
3.  Download survey datasets from the [DHS
    website](https://dhsprogram.com/data/available-datasets.cfm).
4.  Load datasets and associated metadata into Python.
5.  Extract variables and combining datasets for pooled multi-survey
    analyses.

## Installation

You can install the latest version from
[`PyPi`](https://pypi.org/) using:

``` python
pip install pdhs
```

Note that to be able to download datasets from DHS, you need to have playwright installed, run the following command to install playwright on your PC.

```shell
playwright install
```

## Getting started

To be able to **download survey datasets from the DHS website**, you
will need to **set up an account with the DHS website**, which will
enable you to request access to the datasets. Instructions on how to do
this can be found
[here](https://dhsprogram.com/data/Access-Instructions.cfm). The email,
password, and project name that were used to create the account will
then need to be provided to `pdhs` when attempting to download datasets.

-----

  - Request dataset access from the DHS website
    [here](https://dhsprogram.com/data/Access-Instructions.cfm).

## Basic Functionality

### Query the [DHS API](https://api.dhsprogram.com/).

Obtain survey estimates for the Total Fertility Rate among women from Albania belonging to the middle and second wealth quintile, categorized by Region.

```py
from pdhs.indicators import GetIndicatorsData, GetIndicators

indicators_data = GetIndicatorsData(
    country_ids = ["AL"],
    characteristic_category=["wealth quintile", "region"],
    characteristic_label=["middle", "second"],
    breakdown="all"
)


fertility = indicators_data.get_data()
print(fertility.head())
```

```shell
shape: (5, 28)
┌─────────┬───────────┬─────────────┬─────────────┬───┬────────┬─────────┬─────────────┬───────────┐
│ DataId  ┆ SurveyId  ┆ Indicator   ┆ IsPreferred ┆ … ┆ CIHigh ┆ IsTotal ┆ ByVariableI ┆ LevelRank │
│ ---     ┆ ---       ┆ ---         ┆ ---         ┆   ┆ ---    ┆ ---     ┆ d           ┆ ---       │
│ i64     ┆ str       ┆ str         ┆ i64         ┆   ┆ str    ┆ i64     ┆ ---         ┆ str       │
│         ┆           ┆             ┆             ┆   ┆        ┆         ┆ i64         ┆           │
╞═════════╪═══════════╪═════════════╪═════════════╪═══╪════════╪═════════╪═════════════╪═══════════╡
│ 3361769 ┆ AL2008DHS ┆ Age         ┆ 1           ┆ … ┆        ┆ 0       ┆ 0           ┆           │
│         ┆           ┆ specific    ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ fertility   ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ rate: 1…    ┆             ┆   ┆        ┆         ┆             ┆           │
│ 3419763 ┆ AL2008DHS ┆ Age         ┆ 1           ┆ … ┆        ┆ 0       ┆ 0           ┆           │
│         ┆           ┆ specific    ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ fertility   ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ rate: 1…    ┆             ┆   ┆        ┆         ┆             ┆           │
│ 3361770 ┆ AL2008DHS ┆ Age         ┆ 1           ┆ … ┆        ┆ 0       ┆ 0           ┆           │
│         ┆           ┆ specific    ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ fertility   ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ rate: 1…    ┆             ┆   ┆        ┆         ┆             ┆           │
│ 3419764 ┆ AL2008DHS ┆ Age         ┆ 1           ┆ … ┆        ┆ 0       ┆ 0           ┆           │
│         ┆           ┆ specific    ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ fertility   ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ rate: 1…    ┆             ┆   ┆        ┆         ┆             ┆           │
│ 3361764 ┆ AL2008DHS ┆ Age         ┆ 1           ┆ … ┆        ┆ 0       ┆ 0           ┆           │
│         ┆           ┆ specific    ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ fertility   ┆             ┆   ┆        ┆         ┆             ┆           │
│         ┆           ┆ rate: 2…    ┆             ┆   ┆        ┆         ┆             ┆           │
└─────────┴───────────┴─────────────┴─────────────┴───┴────────┴─────────┴─────────────┴───────────┘
```

### Identify survey datasets



Lastly, identify the datasets required for download. By default, the
recommended option is to download either the spss (.sav), `fileFormat =
"SV"`, or the flat file (.dat), `fileFormat = "FL"` datasets. The flat
is quicker, but there are still one or two very old datasets that don’t
read correctly, whereas the .sav files are slower to read in but so far
no datasets have been found that don’t read in correctly. The household
member recode (`PR`) reports the RDT status for children under
five.



### Download datasets

We can now go ahead and download our datasets. To be able to download
survey datasets from the DHS website, you will need to set up an account
with them to enable you to request access to the datasets. Instructions
on how to do this can be found
[here](https://dhsprogram.com/data/Access-Instructions.cfm). The email,
password, and project name that were used to create the account will
then need to be provided to `rdhs` when attempting to download datasets.

Once we have created an account, we need to set up our credentials using
the function `set_rdhs_config()`. This will require providing as
arguments your `email` and `project` for which you want to download
datasets from. You will then be prompted for your password.

You can also specify a directory for datasets and API calls to be cached
to using `cache_path`. In order to comply with CRAN, this function will
also ask you for your permission to write to files outside your
temporary directory, and you must type out the filename for the
`config_path` - “rdhs.json”. (See [introduction
vignette](https://docs.ropensci.org/rdhs/articles/introduction.html) for
specific format for config, or `?set_rdhs_config`).



-----
