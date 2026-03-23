# Carbon Sense

Carbon Sense is a comprehensive suite designed to optimize AI prompts, track CO₂ emissions avoided from prompt compression, and provide a unified chat and dashboard experience.

## Project Structure

This repository contains three main components:

1. **API (Backend)** - `api`
   - A FastAPI backend that handles prompt compression, model routing, semantic caching, and memory persistence.
   - Run the backend on port `8080`. For more details, see [api/README.md](./api/README.md).

2. **VS Code Extension** - `vscode-ext/carbon-sense`
   - A VS Code extension providing the `@carbon-sense` Copilot Chat participant.
   - Automatically compresses prompts, tracks token savings, and persists interactions to your project's memory database.
   - Run `/stats` to show session statistics (tokens saved, CO₂ avoided, cache hit rate).
   - For more details, see [vscode-ext/carbon-sense/README.md](./vscode-ext/carbon-sense/README.md).

3. **Web Dashboard** - `web`
   - A React/Vite frontend to visualize metrics, interactions, and potential CO₂ savings.
   - Run `npm run dev` to start the dashboard locally.

## Getting Started

To get started with Carbon Sense, it's recommended to start the backend API first, as both the VS Code extension and Web dashboard rely on it.

### 1. Start the API
```bash
cd api
bash start.sh
```

### 2. Run the Web Dashboard
```bash
cd web
npm install
npm run dev
```

### 3. Use the VS Code Extension
Open the `vscode-ext/carbon-sense` directory in VS Code, install dependencies via `npm install`, and hit `F5` to start debugging the extension. You can then use `@carbon-sense` in Copilot Chat in the new Extension Development Host window.

## Features

- **Prompt Optimization:** Compresses prompts without losing semantic meaning before sending them to the LLM.
- **Semantic Caching:** Responds instantly to similar queries to save API costs and energy.
- **Model Routing:** Routes requests intelligently based on complexity, balancing performance and efficiency.
- **Memory Persistence:** Context is retained per project session.

Enjoy building efficiently with Carbon Sense!
