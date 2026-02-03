# garak-local-lmstudio

Follow installation instructions from official repo: https://github.com/NVIDIA/garak/

Launch garak proxy (for response filtering in REST API) using **uvicorn:**
```bash
uvicorn lmstudio_garak_proxy:app --host 0.0.0.0 --port 9000
```

Test connectivity and run the first probe to identify timeout issues:
```bash
garak --model_type rest -G lmstudio-config.json --probes malwaregen.Evasion --generations 2
```

If you are hosting multiple models on the same port, specify one with **--model_name** and change that in .json file.

You can also change **max_tokens** inside the **.json config file or inside LM Studio itself, depending on the capability of your hardware.**

If everything works, you are good to go!

Look for other probes and test against them:
```bash
garak --list_probes
```
