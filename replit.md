# UYZD Username Scanner

A terminal-based console app that scans for available usernames across 46 platforms and posts results to Discord webhooks.

## Project Structure

```
app.py              - Main entry point: scan loop, settings, progress bar, results
checkers/
  __init__.py       - Exports checker functions
  xbox.py           - Xbox availability check via XBL.IO API
  steam.py          - Steam profile availability check
  roblox.py         - Roblox username availability check
  discord_check.py  - Discord username availability check
  discord.py        - Discord webhook embed posting
utils/
  __init__.py       - Exports generator and UI helpers
  generator.py      - Random username generation
  platforms.py      - Platform special character support helpers
  ui.py             - Rich console helpers: banner, ask(), ask_yn()
  words.txt         - Word list for word-mode generation
wsgi/
  adj.txt           - Adjective word list (legacy)
  noun.txt          - Noun word list (legacy)
```

## Tech Stack

- **Python 3.12**
- **rich** - Terminal UI, progress bars, panels, tables
- **requests** - HTTP API calls

## Running

```
python3 app.py
```

## Environment Variables (set in Secrets tab)

- `XBL_API_KEY` - Free key from https://xbl.io (required for Xbox checks)
- `DISCORD_TOKEN` - Discord user token (required for Discord username checks)
- `DISCORD_WEBHOOK_URL` - Discord webhook for Xbox results
- `STEAM_WEBHOOK_URL` - Discord webhook for Steam results
- `ROBLOX_WEBHOOK_URL` - Discord webhook for Roblox results
- `DISCORD_WEBHOOK_URL_DC` - Discord webhook for Discord username results
- `STEAM_API_KEY` - Optional Steam API key (uses public profiles without it)
- `ROBLOX_COOKIE` - Optional .ROBLOSECURITY cookie (for Roblox rate limit avoidance)

## Workflow

- **Start application** - Runs `python3 app.py` as an interactive console TUI
