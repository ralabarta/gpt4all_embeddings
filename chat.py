from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import LlamaCppEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
from gpt4allj.langchain import GPT4AllJ
import os

load_dotenv()

llama_embeddings_model = 'LLAMA_EMBEDDINGS_MODEL'
persist_directory = 'db'

model_type = "GPT4All"
model_path = 'MODEL_PATH'
model_n_ctx = 'MODEL_N_CTX'

from constants import CHROMA_SETTINGS

def main():
    llama = LlamaCppEmbeddings(model_path=llama_embeddings_model, n_ctx=model_n_ctx)
    db = Chroma(persist_directory=persist_directory, embedding_function=llama, client_settings=CHROMA_SETTINGS)
    retriever = db.as_retriever()
    # Prepare the LLM
    callbacks = [StreamingStdOutCallbackHandler()]
    if model_type == "LlamaCpp":
        llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, callbacks=callbacks, verbose=False)
    elif model_type == "GPT4All":
        llm = GPT4AllJ(model=model_path)
    else:
        print(f"Model {model_type} not supported!")
        exit()

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    # Interactive questions and answers
    while True:
        query = input("\nYour query: ")
        if query == "exit":
            break
        
        # Get the answer from the chain
        res = qa(query)    
        answer, docs = res['result'], res['source_documents']

        # Print the result
        print("\n\n> Question:")
        print(query)
        print("\n> Answer:")
        print(answer)
        
        # Print the relevant sources used for the answer
        for document in docs:
            print("\n> " + document.metadata["source"] + ":")
            print(document.page_content)

if __name__ == "__main__":
    main()
