from typing import List, Optional
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic import class_validators
from transformers import pipeline, Pipeline

validator = class_validators.validator


class Anonymizer(BaseModel):
    use_gpu: bool = False

    @validator("device", pre=True)
    def set_device(cls, value, values):
        if values["use_gpu"]:
            return 0
        else:
            return -1

    anonymizer_model_tag: str = Field("Isotonic/distilbert_finetuned_ai4privacy")
    model_loaded: bool = False
    device: int = Field(default=-1, alias="device")

    def __init__(self):
        super().__init__()
        try:
            self.anonymizer = pipeline(
                "token-classification",
                model=self.anonymizer_model_tag,
                tokenizer=self.anonymizer_model_tag,
                device=self.device if self.use_gpu else -1,
            )
            self.model_loaded = True
            print("Anonymizer model loaded...")
        except Exception as exc:
            self.model_loaded = False
            print(f"Error in loading Anonymizer model... \n\n{exc}")

    def replace_entities(self, model_output: List[dict], text: str) -> str:
        word_to_entity_group = dict(
            (text[token["start"] : token["end"]], token["entity_group"])
            for token in model_output
        )
        for i, token in enumerate(model_output):
            word = list(word_to_entity_group.keys())[i]
            text = text.replace(word, f"[{word_to_entity_group[word]}]")

        return text

    def pii_mask(self, input_sentence: str) -> Optional[str]:
        if self.model_loaded:
            output = self.anonymizer(input_sentence, aggregation_strategy="simple")
            if isinstance(output, list):
                masked_text = self.replace_entities(output, input_sentence)
                return masked_text
            else:
                print("Anonymizer output is not in the expected format")
        else:
            print("Anonymizer Model is not loaded")
        return None
    
    class Config:
        arbitrary_types_allowed = True


