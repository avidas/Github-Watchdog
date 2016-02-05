import os
from github import GitHubClient
from sendmail import send_email

def main():
    gh_client = GitHubClient.create()
    owner = os.environ.get('OWNER', None)
    events = gh_client.get_public_user_events(owner)
    latest_event = GitHubClient.get_latest_push_event(events)
    time_since_last = GitHubClient.get_time_since_last(latest_event)
    num_hours = int(os.environ.get('NUM_HOURS'))
    if GitHubClient.is_older_than_limit(time_since_last, num_hours):
      send_email('You have not published to Github for ' + str(time_since_last))

if __name__== '__main__':
    main()
