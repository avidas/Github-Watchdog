Github Watchdog
===============

Sends an email notification if you have not pushed to Github in the last X hours or longer than a day. Keep your Github Contributions green!

Uses mandrill to send email currently but you can use any provider.

###Usage

```bash
  git clone git@github.com:avidas/Github-Watchdog.git
  cd Github-Watchdog
```

Setup config.sh with your credentials
```bash
  export GITHUB_TOKEN=''
  export OWNER=''
  export LOG_PATH=logs
  export MANDRILL_USERNAME=''
  export MANDRILL_PASSWORD=''
  export FROM_EMAIL_ADDRESS=''
  export TO_EMAIL_ADDRESS=''
  export MANDRILL_PASSWORD=''
```

Set up a cron job in a Digital Ocean/AWS EC2 or other server to run at an specified interval.

```bash
0 */6 * * * /path/to/your/dir/github_reminder/run.sh
```

Keep your Github green!
