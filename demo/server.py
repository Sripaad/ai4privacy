import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"

import json
import logging
import random
import time
from typing import Dict, List, Optional, Tuple

import numpy as np
import requests
import torch
from fastapi import FastAPI
from ai4p import AI4P
from pydantic import BaseModel

app = FastAPI()

# If you're running it in a docker container set --host and --port 
# or (0.0.0.0)
# uvicorn fastapi_server:app --reload --host 127.0.0.0 --port 1352

class SimpleMessage(BaseModel): 
	input_text: [str] = "Input sentence" 
 
anonymizer = AI4P.Anonymizer(use_gpu=False)

@app.post("/pii")
def run_pii_mask(message: SimpleMessage):
    start_time = time.time()
    masked_text = anonymizer.pii_mask(message.input_text)
    output = {
    "input_text": message.input_text,
    "pii_masked_text": masked_text
    }
    print(output)
    print(f"Time taken for single prediction: {time.time()-start_time}")
    return output

