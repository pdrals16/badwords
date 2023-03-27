import pandas as pd
import uvicorn
from src.core.badwords_filter import BadwordsFilter
from fastapi import FastAPI,  Request

app = FastAPI()

badwords = pd.read_csv('reference/badwords.csv')
list_badwords = badwords['Word'].to_list()
badwords_filter = BadwordsFilter(language='pt',
                                list_badwords=list_badwords)

@app.get("/badwords")
async def root():
    return [{"message": "Badwords Filter"}]


@app.post("/badwords")
async def filter_message(info : Request):
    req_info = await info.json()
    return {
        "status" : "SUCCESS",
        "original" : req_info['text'],
        "alternative": badwords_filter.censor(req_info['text'])
    }

@app.get("/api")
async def root():
    return [
        {
            "id":1,
            "name": "Jamie",
            "age": 22
        },
        {
            "id":2,
            "name": "Pedro",
            "age": 23
        }
        ]


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')