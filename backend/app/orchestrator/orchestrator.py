from app.security.guardrails import check_prompt
from app.tools.tool_router import run_tool
from app.memory.cache import get_cache, save_cache
from app.orchestrator.intent import detect_intent
from app.llm.model_manager import chat

from app.rag.embedder import model
from app.rag.vector_store import search, has_documents

def process(latest_message: str, prompt: str):

    # Guardrails (check ONLY latest message)
    blocked = check_prompt(latest_message)
    if blocked:
        return blocked

    # Intent Detection (check ONLY latest message)
    intent = detect_intent(latest_message)

    if intent != "chat":

        tool = run_tool(latest_message)

        if tool:
            return tool

    # Cache (check ONLY latest message)
    cached = get_cache(latest_message)

    if cached:
        return cached

    # ---------- RAG ----------

    use_rag = False

    keywords = [

        "pdf",
        "document",
        "file",
        "chapter",
        "page",
        "uploaded",
        "according to"

    ]

    if has_documents():

        text = latest_message.lower()

        if any(word in text for word in keywords):

            use_rag = True


    if use_rag:

        query = model.encode([latest_message])[0]

        context = search(query)

        if context:

            rag_prompt = f"""
            You are an AI assistant.

            Answer using the document if relevant.

            Context:
            {' '.join(context)}

            Question:
            {latest_message}
            """

            answer = chat(rag_prompt)

        else:

            answer = chat(prompt)

    else:

        answer = chat(prompt)

    save_cache(latest_message, answer)

    return answer