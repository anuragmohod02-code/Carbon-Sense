# Carbon Sense AI

Carbon Sense AI is a VS Code extension that adds a Copilot Chat participant `@carbon-sense` and command-based prompt optimization with CO₂/token tracking.

## Features

- `@carbon-sense` chat participant for optimized prompt handling
- Automatic prompt compression and memory persistence (each prompt/response saved per project session)
- Session stats with `/stats` and reset with `/reset`
- Semantic cache integration with cache-hit metrics
- Command palette + editor context optimization command
- Status bar CO₂ savings indicator

## Commands

- `Carbon Sense: Optimize Selection`
- `Carbon Sense: Optimize Prompt for Copilot`
- `Carbon Sense: Open Web Dashboard`
- `Carbon Sense: Reset Session Metrics`

### Available Commands

- `/stats` — show session statistics (tokens saved, CO₂ avoided, cache hit rate)
- `/reset` — reset session metrics to zero

Use: `@carbon-sense /stats` or `@carbon-sense /reset`

## Configuration

- `carbon-sense.backendUrl` (default: `http://localhost:8080`)
- `carbon-sense.memorySessionId` (optional; if empty, extension auto-generates a project-scoped session id)

## Backend

The extension expects a backend exposing endpoints including:

- `POST /api/optimize`
- `POST /api/cache/check`
- `POST /api/cache/store`
- `GET /api/metrics`
- `POST /api/demo/reset`
- `GET /api/health`

## Usage

Simply use `@carbon-sense <your prompt>` to:
- Automatically optimize (compress) your prompt
- Get an AI response
- Persist the interaction to your project's memory database

Example: `@carbon-sense explain how to implement binary search in Python`

All prompts are automatically optimized and saved per project session for context reuse.
