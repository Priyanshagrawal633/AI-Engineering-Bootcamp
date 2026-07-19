# Lesson 2 Notes

## What is a Token?

A token is the smallest unit of text processed by an LLM.

Examples:

"I love AI"

↓

"I"

" love"

" AI"

A token is NOT always a complete word.

---

## Why Tokenization?

Computers understand numbers, not language.

Sentence

↓

Tokenizer

↓

Token IDs

↓

Embeddings

↓

Transformer

---

## Token IDs

Example:

"hello"

↓

15496

Token IDs are numerical representations of vocabulary entries.

---

## Embeddings

Embeddings convert token IDs into dense vectors that capture semantic meaning.

Example:

Dog

↓

[0.12, -0.45, 0.88, ...]

Similar words have embeddings that are close together.

---

## Mini Project

Built a Token Counter using tiktoken.

Learned:

- encoding
- decoding
- token count