# %%
import requests
# %%
url = 'http://0.0.0.0:8000/'
payload = {
        "text":"A Gabi é muito lixo no poker!"
    }
r = requests.post(url=url,
                json=payload)
r.text
# %%
