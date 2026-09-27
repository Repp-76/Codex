# Codex

A terminal AI coding assistant. Red/black hacker-styled UI, multi-provider backend,
project-aware file editing with undo, and an optional Telegram bridge.

## Features

- Chat-driven coding assistant tuned for writing, debugging, and refactoring code in any language
- Provider-agnostic backend: OpenAI, Gemini, Anthropic, DeepSeek, OpenRouter (easy to add more)
- No API keys in source — everything comes from `.env`
- Normalized error handling (auth, rate limit, timeout, server error) with retry/backoff
- Project mode: open a directory, list its files, and let Codex reason about it
- `/apply` writes the AI's `FILE:` blocks to disk only after you confirm — nothing is overwritten silently
- `/undo` reverts the last file change (create, edit, delete, rename)
- Optional Telegram bot: links a user's Telegram ID and notifies the super admin, sends files only when explicitly asked
- Unit tests that mock every network call — no API keys required to run the test suite

## Architecture

```
codex/
├── main.py                 REPL entry point
├── config.py                .env loading, provider key status
├── constants.py
├── core/
│   ├── engine.py            retry/backoff + provider dispatch
│   ├── session.py            active provider/model/project/history
│   ├── history.py           conversation history with a char budget
│   ├── context.py           builds project context for a request
│   ├── prompts.py           the Codex system prompt
│   ├── patch.py              parses FILE: blocks out of a reply
│   └── state.py              local state (linked Telegram ID) outside .env
├── providers/
│   ├── base.py               AIProvider interface, ChatMessage/ChatResult, ProviderError
│   ├── http_utils.py         shared HTTP + error-normalization helpers
│   ├── openai_provider.py, deepseek_provider.py, openrouter_provider.py
│   │                          (OpenAI-compatible chat/completions)
│   ├── anthropic_provider.py  Messages API
│   ├── gemini_provider.py     generateContent API
│   └── factory.py             name -> provider instance
├── project/
│   ├── manager.py             file listing/reading, ignores .env/.git/venv/etc.
│   ├── editor.py               create/edit/delete/rename with undo recording
│   └── undo.py                 operation stack, restores previous content
├── telegram/
│   ├── sender.py               sendMessage / sendDocument
│   ├── handlers.py             wants_file() — explicit-request detection
│   └── bot.py                  long-polling loop
├── ui/
│   ├── theme.py, banner.py, panels.py    red/black Rich console
└── tests/                     pytest, all network calls mocked
```

## Installation

```bash
git clone <your-repo-url> codex
cd codex
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and add the key(s) for whichever provider(s) you use. You don't need all five —
Codex only shows a provider as available if its key is set.

```bash
python main.py
```

### Termux (Android)

```bash
pkg update && pkg install python git
git clone <your-repo-url> codex
cd codex
pip install -r requirements.txt
cp .env.example .env
python main.py
```

The UI is plain Rich output with no fixed-width assumptions beyond normal terminal wrapping,
so it stays usable on a phone-width Termux session.

## Configuration

`.env` keys:

| Key | Purpose |
|---|---|
| `OPENAI_API_KEY` / `GEMINI_API_KEY` / `ANTHROPIC_API_KEY` / `DEEPSEEK_API_KEY` / `OPENROUTER_API_KEY` | Provider credentials, all optional |
| `TELEGRAM_BOT_TOKEN` | Enables the Telegram bridge |
| `TELEGRAM_SUPER_ADMIN_ID` | Receives the "new user" notification |
| `DEFAULT_PROVIDER` | Which provider to start with (falls back to the first configured one) |
| `DEFAULT_MODEL` | Optional default model override |

Codex never prints a full key — the startup screen shows only a masked tail, e.g. `************a91f`.

## Telegram

On first launch, if `TELEGRAM_BOT_TOKEN` is set, Codex asks for the user's Telegram ID once and
stores it locally under `~/.codex/state.json` (not in `.env`). It then sends a plain-text
notification to `TELEGRAM_SUPER_ADMIN_ID` — no API keys are ever included in that message.

The bot only sends a file when the message clearly asks for one (`telegram/handlers.py:wants_file`).
Normal questions get a normal text reply.

## Commands

```
/help                 show commands
/status                current provider, model, project
/clear                 clear conversation history
/provider <name>       switch provider
/model <name>           set model for the current provider
/project <path>         open a project directory
/files                  list files in the open project
/apply                  write the last reply's FILE: blocks to disk (asks first)
/undo                   revert the last file change
/send <path>            print a file's contents
/exit
```

## Safety notes

- `/apply` always lists the files it's about to touch and asks `y/N` before writing anything.
- Every create/edit/delete/rename goes through `UndoStack`, so `/undo` can reverse it.
- `.env`, SSH keys, and common credential file patterns are excluded from project listings and reads.
- Codex never auto-executes shell commands or generated scripts.

## Testing

```bash
pytest
```

Covers config loading and key masking, the provider factory, HTTP error normalization
(auth/rate-limit/server-error), file create/edit/undo, path-escape protection, the
Telegram file-request heuristic, history trimming, and FILE: block parsing. No real
API keys or network access are required.

## Troubleshooting

- **"No provider configured"** — add at least one API key to `.env` and restart.
- **Auth errors** — the masked key shown at startup should match what you expect; regenerate
  the key with the provider if it doesn't.
- **Rate limit / server error** — Codex retries these automatically with backoff; if it still
  fails, the provider is likely down or throttling you.
- **Telegram notification didn't arrive** — check `TELEGRAM_BOT_TOKEN` and
  `TELEGRAM_SUPER_ADMIN_ID` are both set and that the bot has been started by the admin at
  least once (Telegram requires that before a bot can message a chat).
