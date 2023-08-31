# ai4privacy
An implementation to mask PII in Natural Language Text.

[HF model link](Isotonic/distilbert_finetuned_ai4privacy)

## Installation: 
```
pip install -U https://github.com/Sripaad/ai4privacy.git
```
## Quick Start 
```
from ai4p.AI4P import Anonymizer
import torch

def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

set_seed(864)


anonymizer = Anonymizer(use_gpu=False)

input_sentence = "My name is Clara and I live in Berkeley, California."
pii_masked_sentence = anonymizer.pii_mask(input_sentence)

print("-" *100)
print("[INPUT]: ", input_sentence)
print("[PII_MASKED]: ", pii_masked_sentence)
print("-" *100)
```

```
------------------------------------------------------------------------------------------------------------------------
[INPUT]: "My name is Clara and I live in Berkeley, California."
[PII_MASKED]: "My name is [FIRSTNAME] and I live in [CITY], [STATE]."
------------------------------------------------------------------------------------------------------------------------
```
## Dataset 

- [ai4privacy/pii-masking-65k](https://huggingface.co/datasets/ai4privacy/pii-masking-65k)
- [ai4privacy/pii-masking-43k](https://huggingface.co/datasets/ai4privacy/pii-masking-43k)

## References
- HF : https://huggingface.co/ai4privacy
- GitHub: https://github.com/ai4Privacy
