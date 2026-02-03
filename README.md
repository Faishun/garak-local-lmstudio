# garak-local-lmstudio

Follow installation instructions from official repo: https://github.com/NVIDIA/garak/

Test connectivity and run the first probe to identify timeout issues:
```bash
garak --model_type rest --model_name lmstudio -G garak-config.json --probes malwaregen.Evasion --generations 2
```
