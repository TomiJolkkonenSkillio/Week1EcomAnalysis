import pandas as pd
from datetime import datetime

# create data from csv, and put it to dataframe
def read_data():
    file_path = 'ecommerce_sales.csv'
    df = pd.read_csv(file_path)
    return df

# removing extra column called color
def drop_tables(df):
    dropped_tables = df.drop(columns=["color"])
    return dropped_tables

# renaming unit_price to price
def rename_column(df):
    renamed_df = df.rename(columns={"unit_price": "price"})
    return renamed_df

# convert order_date to datetime format
def convert_to_daytime(df):
    # 'errors="coerce"' to handle invalid date formats and 'dayfirst=False' for DD.MM.YYYY formats
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=False)
    return df

# create total_price column
def create_total_price(df):
    df['total_price'] = df['quantity'] * df['price']
    return df

# additional features: weekday and month
def extract_weekday_month(df):
    # day of the week (0=Monday, 6=Sunday)
    df['order_weekday'] = df['order_date'].dt.weekday
    
    # month of the year (1=January, 12=December)
    df['order_month'] = df['order_date'].dt.month
    
    return df

def main():
    df = read_data()

    # 1.1 display 1st 10 rows, explore size, shape, data types
    # print(df.head(10)) 
    df_shape = df.shape
    # print(f"\nShapes (row count and number of columns): {df_shape}")
    df_types = df.dtypes
    # print(f"\nData types: \n{df_types}")

    df_dropped_tables = drop_tables(df)
    # print(f"color-column dropped:\n {df_dropped_tables.head(10)}")
    df_renamed = rename_column(df_dropped_tables)
    # print(f"unit_price -column changed to price:\n {df_renamed.head(10)}")
    df_daytime_converted = convert_to_daytime(df_renamed)
    # print(f"order_date converted to datetime format:\n {df_daytime_converted.head(10)}")
    df_total_price_added = create_total_price(df_daytime_converted)
    # print(f"new column total_price added:\n {df_total_price_added.head(10)}")
    df_with_date_features = extract_weekday_month(df_total_price_added)
    print(f"\nData with 'order_weekday' and 'order_month' added:\n {df_with_date_features.head(10)}")

if __name__ == "__main__":
    main()
