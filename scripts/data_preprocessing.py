import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Perform preprocessing steps
    return data

# Example usage
if __name__ == "__main__":
    processed_data = preprocess_data('data/sample_flight_data.csv')
    print(processed_data.head())
