# Provenance
- data: created in repo, tracked by DVC (remote=D:\DVCRemote)
- preprocess: ml/data_pipeline.py @<commit>
- training: ml/train.py -> MLflow experiment=hello-mlops
- registry: ml/registry/model.pkl + current_model.md
- runtime: Dockerfile (python:3.12-slim), app/main.py
