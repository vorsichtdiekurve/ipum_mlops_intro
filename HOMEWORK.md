# Laboratory 1 homework 

Homework will be implementing a production-ready sentiment analysis application.
For the purposes of this assignment, we focus only on a single prediction, i.e. request-response
for a single text at a time.

Instructions:
- do tasks in order, they have been design to build upon prior steps
- write clean code, descriptive variable and function names, use comments where necessary etc.
- send your resulting application code as .zip file

### 1. Dependency management setup (2 points)

- Prepare a development environment with `uv` ([uv commands](https://docs.astral.sh/uv/getting-started/features/)) that contains:
    - `pyproject.toml`
    - `uv.lock`
- To run the inference mentioned below, you need:
    - `clean-text`
    - `joblib`
    - `torch`
    - `transformers`
- To finish all the tasks, you will also need further dependencies. Add them as necessary. All are mentioned
  in the lab instruction, in code, or in the docstring of prepared `inference.py` script.
- Use [dependency groups](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies)
  to separate development dependencies in your `pyproject.toml`. For example, we do not need `pytest` to
  run our inference app on the production server.
- Set up [PyTorch in uv](https://docs.astral.sh/uv/guides/integration/pytorch/) for either CPU or GPU,
  whatever is available to you.

### 2. Pre-commit hooks (1 point)

Set up the pre-commit hooks:
- `ruff` (linter and formatter)
- `mypy`

If you need additional configuration, adding them to `pyproject.toml` is recommended. However, if you prefer,
you can also use separate files for this.

### 3. Webserver development (2 points)

Implement FastAPI webserver for inference, which should have:
- a single endpoint `/predict`, accepting POST requests
- Pydantic model validating request  (input), JSON with single key `text` (string)
- Pydantic model validating response (output), JSON with single key `prediction` (string)

To test the application, you can use [Swagger UI](https://fastapi.tiangolo.com/#interactive-api-docs)
(provided by FastAPI), `curl`, `requests` or any other library. `curl` code would be:

```bash
curl -X POST \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "What a great MLOps lecture, I am very satisfied"}'
```

The sample expected response is: 
```json 
{ "prediction": "positive" } 
``` 

### 3. Sentiment analysis implementation (2 points)

Your teammate, the data scientist, has already prepared the sentiment analysis model for you, and shared it
on Google Drive: https://drive.google.com/drive/u/1/folders/1S6cVfdNsyRJtNCkLzA7-hkH_IxatOISk. Now you need
to add it to your inference server.

File contains the model, tokenizer (for text preprocessing), and class code in `inference_class.pkl`.
Unpack them and save in `app/artifacts` directory.

To use the model, load the `inference_class.pkl` using the [cloudpickle library](https://github.com/cloudpipe/cloudpickle).
It also has a docstring saved (`__doc__` attribute), documenting its usage. The relevant method to use is
`.predict()`. Code for loading is:
```python
import cloudpickle 


with open("inference_class.pkl", "rb") as file:
    Inference = cloudpickle.load(file)

print(Inference.__doc__)

# look at the docstring of the class to see what needs to be passed here
inference = Inference(...)
prediction = inference.predict("New text") 
```

Cloudpickle is very useful for serializing (saving on disk) various Python objects. In contrast to most
solutions, it can also serialize the class itself and all its dependencies.

Add the model to your FastAPI server.

### 4. Code testing (1 point)

Implement unit tests with `pytest`:
- test input validation, model inference, and response validation
- input text should be a non-empty string
- model should be loaded from provided cloudpickle file without errors
- inference should work for a few sample strings
- output should be a valid JSON response
- for an invalid input, validation should return a valid JSON with error explanation

### 5. Containerization (2 points):

Implement Docker and Docker Compose to containerize your application, so it:
- is packaged in a Docker container, with code and model
- contains all required inference dependencies
- is runnable using `docker compose up`
- is accessible on `http://localhost:8000`

For base image, we recommend `slim-bookworm` from https://hub.docker.com/_/python. Note that
it should have the same Python version as your application.

Validate that everything works by running Docker Compose and making queries to the webserver.

### 6. Bonus exercise (2 extra points)

Optimize your Dockerfile with:
- small, lightweight base image
- install `uv` inside the Dockerfile, copy `pyproject.toml` and `uv.lock`, install dependencies
- split the Dockerfile layers to use a [multi-stage build](https://docs.docker.com/build/building/multi-stage/):
  - first stage should install dependencies
  - second stage should copy the application code
- compare the Docker image size of your original solution from exercise 5 and this one
