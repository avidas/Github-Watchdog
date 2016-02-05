import requests
import os
import re
import logging
from datetime import datetime, timedelta

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class GitHubClient:
    def __init__(self, base_url, gh_token):
        """
        Thin client holding on to github api routes
        and tokens
        """
        self.base_url = base_url
        self.gh_token = gh_token

    @classmethod
    def create(cls):
        """
        Set up client with private and public tokens and return instance of github client
        """
        token = os.environ['GITHUB_TOKEN']
        url = "https://api.github.com" 
        github = GitHubClient(url, token)

        return github

    def traverse_pagination(self, endpoint):
        """
        Traverses github pagination
        """
        url = self.base_url + endpoint
        results = []
        while url:
            resp = requests.get(url, auth=('token',self.gh_token))
            response = resp.json()
            results.extend(response)       
            link = resp.headers.get('Link')
            if not link:
                break
            match = re.match('^.*<([^>]+)>; rel="next"', link)
            if match:
                url = match.group(1)
            else:
                url = None
        return results

    def get_public_user_events(self, owner, type="public"):
        """
        Gets all public events for user
        """
        logger.info('Getting all events for ' + owner + '...')
        endpoint = "/users/" + owner + "/events/" + type
        return self.traverse_pagination(endpoint)

    @staticmethod
    def get_latest_push_event(events, type="PushEvent"):
      """
      Find the most recent time the user has pushed to any repo
      """
      filtered_events = [event for event in events if event['type']==type]
      return filtered_events[0]

    @staticmethod
    def get_time_since_last(event):
      """
      Get time since last commit
      """
      datestr = event['created_at']
      last_event_time = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%SZ')
      timediff = datetime.now() - last_event_time
      return timediff

    @staticmethod
    def is_older_than_limit(timediff, hours=10):
      if timediff.days > 1 or timediff.seconds / 3600 > 6:
        return True
