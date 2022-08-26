# Prototyping a Machine Learning Application with Streamlit and FastAPI

- [Prototyping a Machine Learning Application with
  Streamlit](#prototyping-a-machine-learning-application-with-streamlit)
  - [What is Prototyping?](#what-is-prototyping)
    - [Prototyping Tools](#prototyping-tools)
  - [What is Streamlit?](#what-is-streamlit)
    - [Why use Streamlit?](#why-use-streamlit)
    - [How it Works?](#how-it-works)
  - [Example ML-App](#example-ml-app)
    - [Architecture](#architecture)
    - [Project Setup](#project-setup)
      - [Clone this repository](#clone-this-repository)
      - [Configure environment](#configure-environment)
    - [Results](#results)
    - [Tools](#tools)

## What is Prototyping?

[Prototyping](https://www.interaction-design.org/literature/topics/prototyping)
is a process for developing an idea, and it is used in different areas to test
or simulate it before launching.

* A [prototype](https://en.wikipedia.org/wiki/Prototype) is a version of what
  the product will be.
* Prototyping is the iterative process of idea development.

> "So, we will have some **prototypes** of an idea in the **prototyping**
> process."

Prototyping is a fundamental step for any product, idea, or service type because
it allows:

* development of an initial version,
* discovery of flaws, 
* reduction in costs,
* knowledge of the users' experience,
* testing of features, and
* also, generation of [POCs](https://en.wikipedia.org/wiki/Proof-of-concept) or
  [MVPs](https://en.wikipedia.org/wiki/Minimum_viable_product) of the idea.

### Prototyping Tools

There are different tools according to the level of fidelity or similarity
between the idea and the final product. These levels can vary according to their
concept, aesthetic, and function.

* **Low-fidelity** prototyping is a paper draft of the idea.
* **Mid-fidelity** prototyping can be produced in software as a mockup,
  replicating some fundamental functionalities of the idea. Some tools for
  prototyping are [Figma](https://www.figma.com),
  [Sketch](https://www.sketch.com), [Miro](https://miro.com), and 
  [InVision](https://www.invisionapp.com).
* **High-fidelity** prototype may include some level of programming to replicate
  the final solution behavior fluidly.
  [Flask](https://flask.palletsprojects.com/en/2.1.x/) and
  [Streamlit](https://streamlit.io) are a couple of tools.

## What is Streamlit?

[Streamlit](https://streamlit.io) is a free, open-source, all-Python framework.
It enables data scientists to quickly build interactive dashboards and machine
learning web apps, without requiring front-end web development experience.

This framework has gained [attention and
popularity](https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila)
among data scientists and machine learning programmers in recent years. Its
growth is due to the fact that it:

* is an easy-to-use tool,
* needs basic knowledge of Python, and
* is **compatible with frameworks** such as:
  * Machine Learning: TensorFlow, PyTorch, Scikit-learn,
  * Visualization libraries: Seaborn, Altair, Plotly, and
  * Others.

### Why use Streamlit?

During the development process of data science projects, we always need to
present the results of our findings at certain times. And we sometimes may have
doubts about what would be the best way to show these results. 

Then, this is where tools like Streamlit emerge as a quick way to expose
functional results and don't need complex implementations. 

Streamlit could be seen as an opportunity in situations like:

* **prototyping** quickly,
* creating **MVP**,
* putting an application into production in a few weeks, and
* sharing a link with the client or user of the system that is being developed.

So, I think it could be a good option when you want to get a
[prototype](https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila)
of your dashboard/web app up and **run it as quickly as possible**.

### How does it Work?

1. [Install
   Streamlit](https://docs.streamlit.io/library/get-started/installation). I
   recommend you use **Conda and set up your environment**, but you can use:

    ```shell
    pip install streamlit
    ```

2. [Create](https://docs.streamlit.io/library/get-started/create-an-app) a new
   Python script and import Streamlit with a few Streamlit commands:

    ```shell
    import streamlit as st
    ```

3. [Run](https://docs.streamlit.io/library/get-started/main-concepts) it:

    ```shell
    streamlit run your_script.py
    ```

    As soon as you run the script, a local Streamlit server will spin up, and
    your app will open in a new tab in your default web browser.

    Or you can navigate to `http://localhost:8501`.

## Example ML-App

I proposed a basic architecture to predict which class an input image belongs
to. For this example I use a
[CNN](https://github.com/mafda/deep_learning_101/blob/master/src/05-convolutional-neural-networks.ipynb)
in TensorFlow-Keras and the [MNIST](http://yann.lecun.com/exdb/mnist/) database.

### Architecture

![streamlit with fastapi](assets/streamlit-fastapi.png)

### Project Setup

Installing Streamlit is as simple as installing any other Python package.

#### Clone this repository

```shell
(base)$: git clone git@github.com:mafda/ml_with_fastapi_and_streamlit.git
(base)$: cd ml_with_fastapi_and_streamlit
```

#### Configure environment

- Create the conda environment

```shell
(base)$: conda env create -f environment.yml
```

- and update with **development dependencies** (Read more about [Python Best
  Practices](https://github.com/mafda/python_best_practices))

```shell
(base)$: conda env update -n ml-app -f environment-dev.yml
```

- Activate the environment

```shell
(base)$: conda activate ml-app
(base)$: git checkout streamlit-basic
```

- Run

```shell
(ml-app)$: streamlit run src/app.py
```

- And go to [http://localhost:8501](http://localhost:8501)

### Results

![streamlit app - mnist](assets/mnist-prediction.gif)


### Basic version (Only Streamlit)

- Activate the environment

```shell
(base)$: git checkout streamlit-basic
```

- Run

```shell
(ml-app)$: streamlit run src/app.py
```

- And go to [http://localhost:8501](http://localhost:8501)


### Tools

- [FastAPI](https://fastapi.tiangolo.com)
- [Streamlit](https://streamlit.io)


---

made with 💙 by [mafda](https://mafda.github.io/)
