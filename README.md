# About this project

This is a quick demo that compares two excel files and extract the differences in a result file.

## Setup

Install python dependencies.

```bash
pip install -r requirements.txt
```

## Run

Run the program

```bash
python main.py
```

This should generate a `result.xlsx` file.

# Notes
This demo assumes that both files have the same records with the same number of rows and columns and that they keep the same order.

If you want to compare files with different records then this won't work and a different logic is needed.


# References

- This demo was created using [this article](https://kanoki.org/2019/02/26/compare-two-excel-files-for-difference-using-python/).
- Also I recommend going through the [Pandas tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html)