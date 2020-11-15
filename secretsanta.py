import sys
import json
import random
import smtplib
import argparse
from email.mime.text import MIMEText


def send_mail(subject, message, recepient, config):
    """ Sends an e-mail with subject and message to recepient, using config settings. """

    msg = MIMEText(message.encode('utf-8'), _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = config["sender"]
    msg['To'] = recepient

    username = config["sender"]
    password = config["password"]
    server = smtplib.SMTP(config["server"])
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(config["sender"], [recepient], msg.as_string())
    server.quit()


def load_config(file_name):
    """ Simple helper function to load a json as a dict from a file name. """
    with open(file_name, encoding='utf-8') as f:
        return json.loads(f.read())


def create_santa_list(participants):
    """
    Randomises participant list and returns a dictionary
    each person buying for the person next to him/her in the list.
    """
    names = list(participants.keys())
    random.shuffle(names)
    total = len(names)
    return {name: names[(i + 1) % total] for i, name in enumerate(names)}


def secret_santa(participants, mailtemplate, mailserver, dry=True):
    """ Makes the secret santa extraction and sends the e-mails. """
    santas_list = create_santa_list(participants)
    message = "\n".join(mailtemplate["message"])

    for giver, receiver in santas_list.items():
        personalised_message = message.format(name=receiver, address=participants[receiver]["address"], phonenr=participants[receiver]["phonenr"])
        if dry:
            print("%s[%s]: %s" % (giver, participants[giver]["email"], personalised_message))
            continue

        send_mail(mailtemplate["subject"],
                  personalised_message,
                  participants[giver]["email"],
                  mailserver)


def main(args):
    parser = argparse.ArgumentParser(description='Secret Santa Randomiser')
    parser.add_argument("--config", default="config.json",
                        help="The config path. Default is %(default).")
    parser.add_argument("--dry", action="store_true", default=False,
                        help="Just print out the list for secret santa instead of e-mailing.")
    args = parser.parse_args(args)
    config = load_config(args.config)

    secret_santa(config["participants"], config["message"], config["mailserver"], args.dry)


if __name__ == "__main__":
    main(sys.argv[1:])
