# sample
name: 24f2002540@ds.study.iitm.ac.in

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: 24f2002540@ds.study.iitm.ac.in
        run: echo "Hello, world!"


