# Semantic Search Engine Using Haystack

This project uses Haystack's FAISS Document Store, EmbeddingRetriever, and FARMReader to build a simple pipeline for retrieving and answering queries based on product reviews from a CSV file. The pipeline allows for semantic search and question answering over the provided dataset.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Example Query](#example-query)
- [Acknowledgements](#acknowledgements)

## Installation

To run this project, you'll need to have Python 3 installed along with the following libraries:

```bash
pip install pandas
pip install farm-haystack[colab]
pip install sentence-transformers
```

Additionally, ensure that FAISS is installed. For detailed instructions on how to install FAISS, you can refer to [FAISS Installation Guide](https://github.com/facebookresearch/faiss).

## Project Structure

```text
├── amazon.csv             # Input CSV file containing product reviews
├── main.py                # Main script containing the code
└── README.md              # Documentation file
```

## Usage

1. **Prepare Your CSV File**: Place your CSV file with product reviews at the root level. The CSV should contain a column called `review_content`, which includes the review text, and other metadata columns for additional information.

2. **Run the Script**: After setting up your environment and placing the CSV, run the script to start the retrieval and question-answering process.

```bash
python main.py
```

3. **Input Query**: The script takes a query and returns the top documents that are most relevant to the question, along with their metadata and relevance score.

### Example CSV File Structure

```csv
review_content,product_name,rating
"This product is fantastic!",Product A,5
"It broke after two uses.",Product B,2
```

## How it Works

1. **Loading Data**: The script reads the CSV file into a Pandas DataFrame and extracts review content along with metadata (e.g., product name, rating).

2. **Creating FAISS Document Store**: FAISS is used to store and retrieve the documents based on their embeddings.

3. **EmbeddingRetriever**: Uses a pre-trained sentence transformer model (`all-MiniLM-L6-v2`) to convert the review content into dense vectors and store them in the FAISS index.

4. **Reader**: The FARMReader (`deepset/roberta-base-squad2`) is used to find exact answers within the retrieved documents.

5. **Pipeline**: The pipeline connects the retriever and reader, allowing users to perform question-answering over the dataset.

## Example Query

```python
query = "What is the best feature of this product?"
```

This query runs through the retrieval and reading pipeline, and the top results are returned.

Sample output:

```
Content: This product is fantastic!
Meta: {'product_name': 'Product A', 'rating': 5}
Score: 0.89
```

## Acknowledgements

This project leverages the following open-source projects:

- [Haystack](https://github.com/deepset-ai/haystack)
- [Sentence Transformers](https://github.com/UKPLab/sentence-transformers)
- [FAISS](https://github.com/facebookresearch/faiss)
- [FARM](https://github.com/deepset-ai/FARM)
```

Save this as a `README.md` file in your project directory, and it will be properly formatted for Markdown display on platforms like GitHub.