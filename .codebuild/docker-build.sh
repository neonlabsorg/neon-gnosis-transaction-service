#!/usr/bin/env bash

# Create Dockerfiles for components
for file in transaction_web transaction_worker transaction_scheduler
do
  cp docker/web/Dockerfile .codebuild/$file.app
done

# Build Docker images
for file in .codebuild/*.app
do
  tag=$(basename -- "$file" ".${file##*.}")
  docker build -t $tag -f $file .
done
