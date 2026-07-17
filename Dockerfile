FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn langchain-mcp-adapters pydantic numpy mcp fastmcp
EXPOSE 8000
