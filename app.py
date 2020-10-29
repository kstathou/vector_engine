import streamlit as st
import pickle
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
from vector_engine.utils import vector_search


@st.cache
def read_data():
    return pd.read_csv("s3://vector-search-blog/misinformation_papers.csv")


@st.cache(allow_output_mutation=True)
def load_bert_model(name="distilbert-base-nli-stsb-mean-tokens"):
    # Instantiate the sentence-level DistilBERT
    return SentenceTransformer(name)


@st.cache
def load_faiss_index():
    with open("models/faiss_index.pickle", "rb") as h:
        return pickle.load(h)


def main():
    data = read_data()
    model = load_bert_model()
    faiss_index = faiss.deserialize_index(load_faiss_index())

    st.title("Vector-based searches with Sentence Transformers and Faiss")

    # User search
    user_input = st.text_area("Search box")

    # Filters
    st.sidebar.markdown("**Filters**")
    filter_year = st.sidebar.slider("Publication year", 2010, 2021, (2010, 2021), 1)
    filter_citations = st.sidebar.slider("Citations", 0, 250, 0)
    num_results = st.sidebar.slider("Number of search results", 10, 50, 10)

    # Fetch results
    if user_input:
        # Get paper IDs
        D, I = vector_search([user_input], model, faiss_index, num_results)
        # Slice data on year
        frame = data[
            (data.year >= filter_year[0])
            & (data.year <= filter_year[1])
            & (data.citations >= filter_citations)
        ]
        for id_ in I.flatten().tolist():
            if id_ in set(frame.id):
                f = frame[(frame.id == id_)]
            else:
                continue

            st.write(
                f"""**{f.iloc[0].original_title}**  
            **Citations**: {f.iloc[0].citations}  
            **Publication year**: {f.iloc[0].year}  
            **Abstract**
            {f.iloc[0].abstract}
            """
            )


if __name__ == "__main__":
    main()
