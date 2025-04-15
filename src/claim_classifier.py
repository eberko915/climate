import pandas as pd

def classify_claims(df, text_column='claim_text'):
    payout_keywords = [
        "flood", "flooded", "extreme rainfall", "too much rain",
        "heatwave", "above 30", "above 30°", "multiple days", "damaged", "died"
    ] ## Keywords that indicate a payout claim
    
    def is_triggered(text):
        if not isinstance(text, str):
            return False

        text_lower = text.lower()

        for keyword in payout_keywords:  ## Check if any of the keywords are in the text
            ## Check if the keyword is in the text
            if keyword in text_lower: 
                return True

        return False
        
    
    df['payout_triggered'] = df[text_column].apply(is_triggered) ## Apply the is_triggered function to the text column
    return df
