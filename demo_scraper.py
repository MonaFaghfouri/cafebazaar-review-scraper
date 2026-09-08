"""
CafeBazaar Review Scraper - Public Demo

This file demonstrates the public-facing structure of the project.

The production implementation, including:
- full review pagination
- platform-specific selectors
- robust extraction logic
- retry mechanisms
- browser automation strategies

is maintained separately.
"""

import pandas as pd


def normalize_review_data(data):
    """
    Convert extracted review records into a structured DataFrame.
    """
    dataframe = pd.DataFrame(
        data,
        columns=[
            "Application",
            "Username",
            "Review Date",
            "Review Text",
            "Application URL",
        ],
    )

    return dataframe.drop_duplicates()


def export_reviews(dataframe, filename="reviews.xlsx"):
    """
    Export normalized review data to Excel.
    """
    dataframe.to_excel(
        filename,
        index=False,
        engine="openpyxl",
    )


if __name__ == "__main__":

    sample_data = [
        {
            "Application": "Sample Insurance App",
            "Username": "User123",
            "Review Date": "1405/06/10",
            "Review Text": "Sample review for demonstration purposes.",
            "Application URL": "https://cafebazaar.ir/app/example",
        }
    ]

    df = normalize_review_data(sample_data)

    print(df)
