import pandas as pd
from haystack.document_stores import FAISSDocumentStore
from haystack.nodes.retriever import EmbeddingRetriever
from haystack.nodes.reader import FARMReader
from haystack import Pipeline

csv_file_path = "amazon.csv"

document_store = FAISSDocumentStore(faiss_index_factory_str="Flat", embedding_dim=384)

data = pd.read_csv(csv_file_path)
columns = data.columns
columns = list(columns.values)

docs = []
for index, row in data.iterrows():
    content = row['review_content']
    meta = {}
    for key in columns: 
        meta = {key: row.get(key, None)}
    docs.append({"content": content, "meta": meta})

document_store.write_documents(docs)

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2", 
    use_gpu=True, 
)

document_store.update_embeddings(retriever)

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

pipeline = Pipeline()
pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
pipeline.add_node(component=reader, name="Reader", inputs=["Retriever"])

query = "What is the best feature of this product?"
results = pipeline.run(query=query)["documents"]

for doc in results:
    print(f"Content: {doc.content}\nMeta: {doc.meta}\nScore: {doc.score}\n")
