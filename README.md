# stock_fetcher

## Setting

```
pip3 install yfinance
```

## Exxecute

```
python3 main.py
```

## LINE Botが動くように

https://manager.line.biz

Message APIのためのアカウントを作成

webhookの設定をして、シークレットキー、アクセストークンを取得する

```
$ git clone git@github.com:kazato110tm/stock_fetcher.git
$ cd stock_fetcher

$ heroku create <application name>

# set secret key
$ heroku config:set YOUR_CHANNEL_SECRET="XXXXXXXXXXX" --app <application name>
# set access token
$ heroku config:set YOUR_CHANNEL_ACCESS_TOKEN="XXXXXXXXXXX" --app <application name>

# set remote repository
$ heroku git:remote -a <application name>

$ git push heroku <branch name>
```

webhookの設定は`https://<application name>.herokuapp.com/callback`
