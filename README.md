# AI Agent: CLI Code Editor

A minimal, terminal-based AI coding agent powered by Google's Gemini API — inspired by Claude Code and Cursor's Agent Mode. I built this project to explore agentic workflows, function calling, and LLM-powered code editing directly from the command line.

## Overview

This project is a CLI terminal tool that uses function calling and feedback loops to autonomously find and fix bugs in a codebase. It interacts with the `gemini-2.5-flash` model to analyze code, execute custom functions, and iteratively repair issues in target projects (such as the included `calculator` package).

## Core Components

The architecture of the agent is built on four main capabilities:

### 1. LLM Integration
The agent connects to the Gemini API using the Python client library. It handles prompts and maintains conversational context directly within the CLI environment.

### 2. File and Execution Functions
The agent is equipped with custom tools to interact with the file system and run Python code. For example, `functions/get_files_info.py` provides the agent with secure directory traversal and file listing capabilities.

### 3. Function Calling
Through its system prompt and context window, the AI is granted the ability to dynamically select and execute the appropriate tools based on the user's terminal commands.

### 4. Agentic Feedback Loop
A proper feedback loop makes the tool truly "agentic." It can analyze the results of its own function calls, re-evaluate the codebase's state, and iteratively work towards resolving bugs without manual intervention.

## Project Structure

- `pyproject.toml` / `uv.lock`: Project dependencies (managed via `uv`), requiring Python 3.12+ and packages like `google-genai` and `python-dotenv`.
- `main.py`: The CLI entry point for the agent. Use it to send prompts and initiate debugging sessions.
- `functions/`: Contains the tools exposed to the agent.
  - `get_files_info.py`: Allows the agent to list directory contents safely within a restricted working directory.
- `calculator/`: A sample target codebase used for testing the agent's ability to debug and repair broken logic.
- `.env`: Environment variables (add your `GEMINI_API_KEY` here).

## Setup and Usage

1. **Install dependencies**: Ensure you have Python 3.12 or above. Install the requirements from `pyproject.toml`:
   ```bash
   uv sync
   # or pip install -e .
   ```
2. **Environment Variables**: Create a `.env` file in the root directory and add your API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
3. **Run the CLI**:
   ```bash
   python main.py "Find and fix the bug in the calculator package"
   ```
   For verbose output with token usage:
   ```bash
   python main.py "Hello, Gemini!" --verbose
   ```
