from typing import List

class Anonymizer:
    def __init__(self, use_gpu=False) -> None:
        from transformers import pipeline

        self.device = 0 if use_gpu else -1   
        self.anonymizer_model_tag = "Isotonic/distilbert_finetuned_ai4privacy"
        self.model_loaded = False
        try:
            self.anonymizer = pipeline("token-classification", model=self.anonymizer_model_tag, tokenizer=self.anonymizer_model_tag, device=self.device)
            self.model_loaded = True
            print("Anonymizer model loaded...")
        except Exception as exc:
            print(f"Error in loading Anonymizer model... \n\n{exc}")
    
    def replace_entities(self, model_output: List[dict], text: str) -> str:
        word_to_entity_group = dict(
    (text[token["start"] : token["end"]], token["entity_group"]) for token in model_output
    )
        for i, token in enumerate(model_output):
            word = list(word_to_entity_group.keys())[i]
            text = text.replace(word, f"[{word_to_entity_group[word]}]")

        return text
    
    def pii_mask(self, input_sentence: str) -> str or None:
        if self.model_loaded:
            output = self.anonymizer(input_sentence, aggregation_strategy="simple")
            masked_text = self.replace_entities(output, input_sentence)
            return masked_text
        
        else:
            print("Anonymizer Model is not loaded")  
            return None