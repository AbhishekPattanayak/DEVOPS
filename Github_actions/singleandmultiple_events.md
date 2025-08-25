1. Triggering single or Multiple events

1.1 single event

name: CI on Push

on:  
  push:               # Trigger workflow when push happens
    branches:         
      - main          # Only when pushed to 'main' branch

jobs:
  build:
    runs-on: ubuntu-latest   # Runner environment
    steps:
      - uses: actions/checkout@v2   # Checks out your repository code, pulls the repo code into the runner
      - name: Run a one line script
        run: echo "Hello, World !"  # Executes a simple shell command


1.2 Multiple events:

name: CI on multiple events

on:  #The trigger happens on push, pull on the main and release events 
    push:
        branches:
            - main
    pull_request:
        branches:
            - main
    release:
        types: [published, created]

jobs:
    build-and-test:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v2
            - name: Set up Python 