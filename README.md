# Building a semantic search engine with Transformers and Faiss
This repository contains the code for the following Medium blogs:
- [How to build a semantic search engine with Transformers and Faiss]()
- [How to deploy a machine learning model on AWS Elastic Beanstalk with Streamlit and Docker]()

Check out the blogs if you want to learn how to create a semantic search engine with Sentence Transformers and Faiss.  

You can [run the notebook on Google Colab]() and leverage the free GPU to speed up the computation!

## How to deploy the Streamlit app locally with Docker ##
Assuming docker is running on your machine and you have a docker account, do the following:
- Build the image

``` bash
docker build -t <USERNAME>/<YOUR_IMAGE_NAME> .
```

- Run the image

``` bash
docker run -p 8501:8501 <USERNAME>/<YOUR_IMAGE_NAME>
```

- Open your browser and go to `http://localhost:8501/`