# NhapMonAI - HandWriting Predict

```bash
cd product
mkdir weights
```

Using VietOCR repository of [pbcquoc](https://github.com/pbcquoc/vietocr) to train custom weights and add that weight file to `weights` folder.

## Run Backend
  ```bash
  cd product
  conda create -n <name>
  conda activate <name>
  pip install -r requirements.txt
  ```
  ```bash
  python main.py
  ```
## Run Frontend
  ```bash
  cd frontend/app
  npm install
  ```
  ```bash
  npm run dev
  ```
