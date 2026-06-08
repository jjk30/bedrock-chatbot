# Bedrock Chatbot

A command-line AI chatbot built with Amazon Bedrock and Python. It holds a multi-turn conversation with a foundation model, remembering earlier messages so follow-up questions keep their context.

## What it does

The chatbot runs in your terminal. You type a message, it sends the full conversation history to a Bedrock model through the Converse API, and prints the reply. A system prompt sets the bot's persona — here, a cloud-computing tutor that explains things with analogies. Type `quit` or `exit` to stop.

There are two versions:

- **`bedrock_chat.py`** — the base chatbot, run at a low temperature (0.1) for consistent, focused answers.
- **`bedrock_chat_guardrail.py`** — the same chatbot with an Amazon Bedrock Guardrail attached, which screens each turn's input and output against content-safety policies. Run at a higher temperature (0.7) for more varied responses.

## How it works

- **Model:** Amazon Nova Lite (`amazon.nova-lite-v1:0`)
- **API:** Bedrock Runtime `converse()`, a single chat interface that works across Bedrock models
- **Memory:** every user and assistant turn is appended to a `messages` list that is resent on each call, so the model sees the whole thread
- **Inference settings:** `temperature`, `topP`, and `maxTokens` control response style and length
- **Safety (guardrail version):** `guardrailConfig` routes each turn through a Bedrock Guardrail with tracing enabled

## Prerequisites

- An AWS account with Amazon Bedrock enabled
- Model access granted for Amazon Nova Lite in the Bedrock console
- AWS credentials available to the script (via `aws configure`, an IAM role, or CloudShell's built-in credentials)
- Python 3.9 or newer

## Setup

```bash
pip install -r requirements.txt
```

## Running it

```bash
python bedrock_chat.py
```

or the guardrail version:

```bash
python bedrock_chat_guardrail.py
```

Then start chatting. Type `quit` to exit.

## Note on the guardrail

The guardrail version references a `guardrailIdentifier` that belongs to my AWS account, so it won't run as-is for anyone else. To use that version, create your own guardrail in the Bedrock console (Build → Guardrails), then replace the `guardrailIdentifier` and `guardrailVersion` values in the script. This ID isn't a secret — it can't be used without access to the account it lives in — but it is account-specific.

## Credits

Built as part of the NextWork "Build an AI Chatbot with Amazon Bedrock" project. Read more about what I did here https://learn.nextwork.org/relieved_purple_beautiful_iara/docs/aws-genai-bedrock-chatbot 
