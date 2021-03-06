# simplesecretsanta

Simple secret santa algorithm.

About
=====

**simplesecretsanta** sends e-mails to participant with their randomly extracted pair.
It is inteded to be a simple and easy to understand secret santa program, with no dependencies.

Usage
-----

Fill  in the configuration file. Copy the template to config.json

```json
{
  "mailserver": {
    "server": "YOUR EMAIL SERVER",
    "sender": "YOUR MAIL ADDRESS",
    "password": "YOUR PASSWORD"
  },
  "participants": {
    "Name1": {
      "email": "email1@gmail.com",
      "address": "ACTUAL ADDRESS",
      "phonenr": "PHONENUMBER"
    },
    "Name2": {
      "email": "email2@gmail.com",
      "address": "ACTUAL ADDRESS",
      "phonenr": "PHONENUMBER"
    },
  },
  "message": {
     "subject": "Secret Santa",
     "message": [
       "You must buy a gift for {name}!",
       "Sum is 10 Euros.",
       "Address for gift:",
       "{address}",
       "{phonenr}",
       "This message was automatically generated by a script.",
       "https://github.com/teapothat/simplesecretsanta"
     ]
  }
}
```

If you use a gmail address you need to generate an app password as explianed here:
https://support.google.com/accounts/answer/185833?hl=en 

to see test output
>   python secretsanta.py --dry
 
to actually send e-mails:
>    python secretsanta.py

to see help
>    python secretsanta.py -h

Specify a different config file by using option --config


