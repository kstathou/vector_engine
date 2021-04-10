# Building a semantic search engine with Transformers and Faiss
This repository contains the code for the following Medium blogs:
- [How to build a semantic search engine with Transformers and Faiss](https://kstathou.medium.com/how-to-build-a-semantic-search-engine-with-transformers-and-faiss-dcbea307a0e8?source=friends_link&sk=6974c79b86e2f257c32f77d49583a524)
- [How to deploy a machine learning model on AWS Elastic Beanstalk with Streamlit and Docker](https://kstathou.medium.com/how-to-deploy-a-semantic-search-engine-with-streamlit-and-docker-on-aws-elastic-beanstalk-42ddce0422f3?source=friends_link&sk=dcc7bbf8d172f2cd18aefcdf0c2c6b49)

Check out the blogs if you want to learn how to create a semantic search engine with Sentence Transformers and Faiss.  

You can [run the notebook on Google Colab](https://colab.research.google.com/drive/11WBCrwNzbNWN7QbMEwzy-8MZROOVQFnZ?usp=sharing) and leverage the free GPU to speed up the computation!

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