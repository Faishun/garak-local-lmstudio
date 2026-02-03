# garak-local-lmstudio

Follow installation instructions from official repo: https://github.com/NVIDIA/garak/

Launch garak proxy (for response filtering in REST API) using **uvicorn:**
```bash
uvicorn lmstudio_garak_proxy:app --host 0.0.0.0 --port 9000
```

Test connectivity and run the first probe to identify timeout issues:
```bash
garak --model_type rest --model_name lmstudio -G garak-config.json --probes malwaregen.Evasion --generations 2
```
