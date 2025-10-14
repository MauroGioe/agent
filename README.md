# agent

This project features a multi-agent system built with adk by exploiting the A2A and MCP protocols.
The MCP servers are for demonstration purposes thus they feature simple tools.

## Usage
After installing ollama
1) Pull the model

Run the following command in the cmd

```
ollama pull qwen3:4b
```
2) Environment setup

Run the command
```
pip install requirements.txt
```
3) Run servers

Run the commands in the following order
```
python math_server.py
```
```
python exchange_server.py
```
```
python math_agent_server.py
```
```
python exchange_agent_server.py
```
```
python host_agent_server.py
```
Then run
```
python run_from_local_client.py
```
and enter your query in the terminal.
Here is a list of queries you can use to test the agent:
- list available agents
- contact the math agent and ask for a list of tools
- what's the exchange rate between euro and usd?
- convert 10 euro in yen

Queries may take a long time to be executed you can check
the current status by looking at the server terminal.