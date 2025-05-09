# permanent_inject.py
#
# This script:
# - Loads a GPT-2 model and tokenizer,
# - Defines a method to apply small healing corrections directly into model weights,
# - Specifically applies healing by modifying the bias vector of a transformer MLP layer,
# - Allows saving the healed model and tokenizer to a new directory.
#
# This module supports:
# - Applying minimal surgical edits to LLM weights after healing,
# - Safely injecting knowledge repairs without full model retraining,
# - Preparing permanently corrected models after Mandala-Healing cycles.
#
# ---
# Part                      | What it does
# ---------------------------|--------------------------------------------------------
# load_model_and_tokenizer() | Loads GPT-2 model and tokenizer from Hugging Face.
# inject_bias_delta()        | Adds a small healing delta to the bias vector of a selected transformer block.
# save_healed_model()        | Saves the healed model and tokenizer to a specified folder.
# __main__ block             | Demonstrates an example healing injection and saving process.

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model_and_tokenizer():
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    model.eval()
    return model, tokenizer

def inject_bias_delta(model, layer_index, delta_vector):
    """
    Apply a small healing delta to the bias vector of a transformer layer.

    Args:
        model: GPT2LMHeadModel
        layer_index: int (which transformer block to patch)
        delta_vector: torch.Tensor (must match hidden size)
    """
    layer = model.transformer.h[layer_index].mlp.c_fc
    with torch.no_grad():
        if layer.bias is not None:
            print(f"Applying healing to layer {layer_index} bias...")
            layer.bias += delta_vector.float()
        else:
            print("Selected layer has no bias term. No healing applied.")

def save_healed_model(model, tokenizer, save_path="gpt2_healed"):
    model.save_pretrained(save_path)
    tokenizer.save_pretrained(save_path)
    print(f"Healed model saved to '{save_path}'.")

if __name__ == "__main__":
    # Example usage:
    model, tokenizer = load_model_and_tokenizer()

    # Create a dummy small healing delta
    hidden_size = model.config.n_embd  # Usually 768 for GPT-2 small
    healing_delta = torch.randn(hidden_size) * 0.002  # Tiny noise for demo

    # Inject into layer 0
    inject_bias_delta(model, layer_index=0, delta_vector=healing_delta)

    # Save healed model
    save_healed_model(model, tokenizer, save_path="gpt2_healed_example")
