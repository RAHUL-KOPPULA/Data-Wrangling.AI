import pandas as pd
import re

def load_data(file_path_or_url):
    if file_path_or_url.endswith('.csv'):
        df = pd.read_csv(file_path_or_url)
    elif file_path_or_url.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path_or_url)
    else:
        raise ValueError("Unsupported data format. Use CSV or Excel.")
    return df

def parse_sort_instructions(statement):
    pattern = r"sort by ([a-zA-Z_]+) *(ascending|descending)?"
    matches = re.findall(pattern, statement.lower())
    
    if not matches:
        raise ValueError("Could not find sorting instructions in problem statement.")
    
    sort_cols = []
    ascending_list = []
    for col, order in matches:
        sort_cols.append(col)
        ascending_list.append(order != 'descending')  # ascending by default
    
    return sort_cols, ascending_list

def sort_data(df, sort_cols, ascending_list):
    for col in sort_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in dataset.")
    return df.sort_values(by=sort_cols, ascending=ascending_list)

def main():
    # Interactive input for problem statement and dataset path/link
    problem_statement = input("Enter your problem statement (e.g. 'Sort by age descending and name ascending'): ")
    dataset_path = input("Enter dataset file path or URL (CSV or Excel): ")

    try:
        df = load_data(dataset_path)
        print("\nOriginal Data Preview:")
        print(df.head(5))

        sort_cols, ascending_list = parse_sort_instructions(problem_statement)
        sorted_df = sort_data(df, sort_cols, ascending_list)

        print(f"\nData sorted by {sort_cols} with ascending flags {ascending_list}:")
        print(sorted_df.head(10))

        # Optionally save the output file
        output_file = "sorted_output.csv"
        sorted_df.to_csv(output_file, index=False)
        print(f"\nSorted data saved to {output_file}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
