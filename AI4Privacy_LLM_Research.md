# AI4Privacy Research 

The goal of the AI4Privacy project is to develop language models that can be trained on datasets devoid of personally identifiable information (PII). This is a challenging task, as PII is often present in natural language data. However, it is an important task, as it will enable the development of language models that can be used in a wider range of applications, such as healthcare, finance, and law enforcement.

The project will address the following research questions:

    - Are language models trained on datasets devoid of PII more effective??
    - What are the performance trade-offs of training language models on PII-free datasets?
    - How can language models be used to protect privacy?

## EL Plan
The project will be conducted in three phases:

**Data Collection and Preparation**

The first phase of the project will involve collecting and preparing a dataset of PII-free text. This will involve identifying and removing PII from existing datasets, as well as collecting new data that is devoid of PII.

    [x] Custom PII masking dataset.
    [x] Train TokenClassification models on custom PII dataset.
    [ ] Validation dataset for PII masking.
    [ ] Compare multiple TokenClassification trained models on the validation dataset.
    [ ] Release PII masked Dataset.
    [ ] Create PII masked Pre-training / finetuning dataset.
    [ ] Train models on masked data.
    [ ] Study activations for the masked model.
    [ ] Test and evaluate the model on benchmarks.
    [ ] Release Open Privacy Enhanced Language Model.(OPEL, name is a work in progress)

**Language Model Training**

The second phase of the project will involve pre-training/finetuning language models on the PII-free dataset. 

**Privacy-Preserving Techniques**

The third phase of the project will involve developing privacy-preserving techniques for using language models. 

## Evaluation

The project will be evaluated using the following open llm benchmarks.
    - (TBD)

## Deliverables: 
    - A model to detect and mask PII data.
    - A dataset of PII-free text. 
    - A set of language models pre-trained or finetuned on PII-free dataset.
    - Comparison of LLaMa, Mistral, Yi-6B vs AI4PrivacyModel(OPEL) on benchmarks
    - The performance of language models trained on PII-free datasets vs traditional llms.
    - The privacy-preserving properties of language models.
    - The usefulness of language models in a variety of applications.sss

## Benefits:
    - To answer the question `Will the development of pii masked language models can be used in a wider range of applications/ are they more effective?`
    - The advancement and better understanding of Language Models.