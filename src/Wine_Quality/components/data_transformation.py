import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from Wine_Quality.utils.common import logger
import os
from pathlib import Path

class DataTransformation:
    def __init__(self, config):
        self.config = config

    def train_test_spliting(self):
        # Load the dataset
        data = pd.read_csv(self.config.data_path)
        
        # Separate features (X) and target variable (y)
        X = data.drop(columns=['quality'])  # 'quality' is the target variable
        y = data['quality']

        # Feature Selection: Remove highly correlated features
        correlation_matrix = X.corr()
        high_corr_features = set()

        for i in range(len(correlation_matrix.columns)):
            for j in range(i):
                if abs(correlation_matrix.iloc[i, j]) > 0.9:  # Correlation threshold
                    colname = correlation_matrix.columns[i]
                    high_corr_features.add(colname)

        # Drop highly correlated features
                X = X.drop(columns=high_corr_features)

        # Scale the features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Split the data into training and test sets (0.8, 0.2 split, stratified)
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42, stratify=y
        )

        # Save the splits to CSV files
        train = pd.DataFrame(X_train, columns=X.columns)
        train['quality'] = y_train.reset_index(drop=True)

        test = pd.DataFrame(X_test, columns=X.columns)
        test['quality'] = y_test.reset_index(drop=True)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Split data into training and test sets")
        logger.info(f"Training data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")

        print(f"Training data shape: {train.shape}")
        print(f"Test data shape: {test.shape}")
