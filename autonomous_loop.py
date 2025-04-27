# autonomous_loop.py

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from fuzzywuzzy import fuzz
from test_suite import score_answer
from permanent_inject import inject_bias_delta

# Load model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()

def model_answer(question, model, tokenizer, max_length=30):
    inputs = tokenizer(question, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length, do_sample=False)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

def simple_confidence_check(output):
    """
    Heuristic: if output is too short or contains "unknown", assume low confidence.
    """
    output_lower = output.lower()
    bad_markers = ["unknown", "no information", "not sure", "undefined", "mythical"]
    if any(marker in output_lower for marker in bad_markers):
        return False
    if len(output.split()) <= 2:
        return False
    return True

def autonomous_heal_cycle(question, model, tokenizer, healing_threshold=0.05):
    print(f"\nPrimary Question: {question}")
    answer = model_answer(question, model, tokenizer)
    print(f"Initial Model Answer: {answer}")

    confident = simple_confidence_check(answer)

    if confident:
        print("[Answer looks confident — no healing triggered.]")
        return

    print("[Low confidence detected — triggering healing cycle.]")

    # Step 1: Self-generate a sub-question
    sub_question = f"What is important to know about: {question}?"
    print(f"Sub-question generated: {sub_question}")

    sub_answer = model_answer(sub_question, model, tokenizer)
    print(f"Sub-answer generated: {sub_answer}")

    # Step 2: Create a dummy small delta for healing (you could customize this!)
    hidden_size = model.config.n_embd
    healing_delta = torch.randn(hidden_size) * 0.002

    # Step 3: Test before/after scores (simulate)
    original_score = score_answer(answer, "unknown")  # simulate low score
    healed_score = score_answer(sub_answer, "unknown")  # simulate slightly better after healing

    print(f"Original Score: {original_score:.2f}")
    print(f"Healed Score: {healed_score:.2f}")

    # Step 4: Decide to apply healing
    if healed_score > (original_score + healing_threshold):
        print("[Healing accepted — applying permanent delta.]")
        inject_bias_delta(model, layer_index=0, delta_vector=healing_delta)
    else:
        print("[Healing rejected — no changes made.]")

if __name__ == "__main__":
    # Example questions
    questions = [
        "What is the capital of Atlantis?",
        "How many moons does Mars have?",
        "Where is the lost city of El Dorado?"
    ]

    for q in questions:
        autonomous_heal_cycle(q, model, tokenizer)
