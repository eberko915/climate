import pandas as pd

## Function that tests whether a farm exhibited a heatwave or heavy rainfall for certain threshold
def detect_streak_trigger(df, column, threshold, min_streak):
    """
    Detects streaks in a DataFrame column based on a threshold and minimum streak length.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column (str): The column name to check for streaks. Either rainfall or temperature.
    threshold (float): The threshold value to determine if a value is part of a streak.
    min_streak (int): The minimum length of the streak to be considered valid.

    Returns:
        DataFrame with a new column 'triggered' (bool)
    """

      # Create a copy of the DataFrame to avoid modifying the original
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    # Create a boolean mask for values above the threshold
    df['above_threshold'] = df[column] > threshold 
    df['triggered'] = False  # Initialize the 'triggered' column to False
        
    # Iterate through the list of famrs to find streaks
    for location in df['location'].unique():
        loc_df = df[df['location'] == location].sort_values(by='date') ## Looks at climate data in data order
        streak = 0
        for i in range(len(loc_df)):
            if loc_df['above_threshold'].iloc[i]:
                streak += 1
                if streak >= min_streak:
                    trigger_indices = loc_df.index[i - min_streak + 1:i + 1] ## Get the indices of all days in the streak
                    df.loc[trigger_indices, 'triggered'] = True   ## Change all indices in streak to True
            else:
                streak = 0
    return df
