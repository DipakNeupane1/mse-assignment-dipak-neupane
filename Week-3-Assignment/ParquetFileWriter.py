# Week 3- Activity 3: using parquet  format for big data
# Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format.
# Then, compute the maximum, minimum, average, and absolute values for each column in the dataset.
# (see link to download a big numerical data in csv format from link: https://archive.ics.uci.edu/datasets)
# Finally, share the GitHub repository link along with a screenshot of the results.
# UCI Machine Learning Repository
# Discover datasets around the world!

import pandas as pd


class ParquetFileWriter:

    def csv_file_reader(self, file_path):
        columns = ["column 1", "column 2", "column 3", "column 4", "column 5"]
        df = pd.read_csv(file_path, names=columns, header=None)
        print(f"Initial dataframe after reading data from CSV file is :: {df}")

        # Writing data from csv file into parquet file.
        df.to_parquet(
            "Week-3-Assignment/iris/iris.parquet", engine="pyarrow", index=False
        )

        # Reading parquet file from a directory.
        parquet_df = pd.read_parquet(
            "Week-3-Assignment/iris/iris.parquet", engine="pyarrow"
        )
        return parquet_df

    def compute_min_max_and_avg_value(self, parquet_df):
        print("Datatypes of all columns \n", parquet_df.dtypes)
        # Select only numeric columns from dataframe to apply some arithmetic operations over colums of dataframe.
        numeric_dataframe = parquet_df.select_dtypes(include=["number"])
        print(
            "Datatypes after selecting only numeric columns \n ",
            numeric_dataframe.dtypes,
        )

        # Findout min, max, and avg for each numeric columns.
        summary_df = pd.DataFrame(
            {
                "Min": numeric_dataframe.min(),
                "Max": numeric_dataframe.max(),
                "Avg": numeric_dataframe.mean(),
            }
        )
        print(f"Summary of parquet dataframe is ::\n{summary_df}")


if __name__ == "__main__":
    parquet_writer = ParquetFileWriter()
    file_path = "Week-3-Assignment/iris/iris.data"
    parquet_data_df = parquet_writer.csv_file_reader(file_path)
    parquet_writer.compute_min_max_and_avg_value(parquet_data_df)
