import os
import json
import joblib
import xgboost as xgb
import pandas as pd

model_file_name = os.environ['MODEL_FILE_NAME']
loaded_model = joblib.load(model_file_name)

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    payload_df = pd.json_normalize([event])
    result = loaded_model.predict(payload_df)
    
    print("Returning: {}".format(result[0]))
    return(json.dumps({"result": result[0]}))

