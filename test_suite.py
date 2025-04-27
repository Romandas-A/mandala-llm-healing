# test_suite.py
#
# This script:
# - Defines a small set of test question-answer (QA) pairs,
# - Loads a GPT-2 model and tokenizer,
# - Generates answers from the model for each test question,
# - Scores the model outputs using:
#   - Exact match (perfect string equality),
#   - Fuzzy match (tolerating small differences, e.g., typos or slight wording changes),
# - Calculates and prints an average test score across all examples.
#
# This module supports:
# - Evaluating model quality before and after healing,
# - Comparing original vs. healed models in a lightweight, simple way,
# - Helping decide whether a healing operation should be accepted.
#
# ---
# Part                      | What it does
# ---------------------------|--------------------------------------------------------
# load_model_and_tokenizer() | Loads GPT-2 model and tokenizer from Hugging Face.
# model_answer()             | Generates an output for a given question using the model.
# score_answer()             | Computes an exact/fuzzy score between model output and correct answer.
# evaluate_model()           | Runs all tests, prints results, and computes final average score.
# __main__ block             | Demonstrates model evaluation on the default QA set.

from fuzzywuzzy import fuzz
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

def load_model_and_tokenizer():
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    model.eval()
    return model, tokenizer

# Test QA database
TEST_QA = {
    "Who is the president of France?": "Emmanuel Macron",
    "What is the capital of Japan?": "Tokyo",
    "What planet is known as the Red Planet?": "Mars",
    "Chemical symbol for gold?": "Au",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the currency of Germany?": "Euro",
    "Largest mammal?": "Blue whale",
    "How many legs does a spider have?": "Eight"
}

def model_answer(question, model, tokenizer, max_length=30):
    inputs = tokenizer(question, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length, do_sample=False)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

def score_answer(model_output, correct_answer):
    model_output = model_output.lower()
    correct_answer = correct_answer.lower()
    if model_output == correct_answer:
        return 1.0
    return fuzz.ratio(model_output, correct_answer) / 100.0

def evaluate_model(model, tokenizer, test_set=TEST_QA):
    total_score = 0
    detailed_results = []

    for question, correct in test_set.items():
        output = model_answer(question, model, tokenizer)
        score = score_answer(output, correct)
        total_score += score

        print(f"Q: {question}")
        print(f"Model: {output}")
        print(f"Expected: {correct}")
        print(f"Score: {score:.2f}")
        print("---")

        detailed_results.append((question, output, correct, score))

    average_score = total_score / len(test_set)
    print(f"\nFinal Average Score: {average_score:.2f}")

    return detailed_results, average_score

if __name__ == "__main__":
    model, tokenizer = load_model_and_tokenizer()
    evaluate_model(model, tokenizer)
