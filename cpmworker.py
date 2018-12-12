import logging
import requests
import urllib3
import os


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#@2323

#Enable logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('API.log')
#handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s :: %(levelname)s: %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)


# todo clean up old trash
# todo add exceptions


class TokenInitializationError(Exception):
    def __init__(self):
        self.message = 'No tokens received!'
    def __str__(self):
        return self.message
    pass


class CPMworker:
    # API points for requests
    URL_API = "https://{host}/api/{api_point}"
    API_TOKEN_OBTAIN = "token/obtain/api_key/"
    API_TOKEN_REFRESH = "token/refresh/"
    API_USERS = "users/"

    API_POLICY = "policies/"
    API_ACCOUNTS = "accounts/"
    API_SCHEDULES = "schedules/"

    HEADER_ACCEPT = "application/json; version=1.1"
    HEADER_AUTHORIZATION = "Bearer {access_token}"
    headers = {'Accept': HEADER_ACCEPT}

    def __init__(self, host, api_key, verify_ssl = False):
        self.host = host
        self.api_key = api_key
        self.data = {'api_key': api_key}
        self.VERIFY_SSL = verify_ssl
        self.access_token = None
        self.obtain_token()
        return

    def obtain_token(self):
        """
        Requests token and refresh token IDs that is mandatory for using RestAPI
        or refreshes token if there is one already
        """
        if self.access_token != None:
            url = self.URL_API.format(host=self.host, api_point=self.API_TOKEN_REFRESH)
            data = self.send(url, {'refresh': self.refresh_token}, 'post')
            self.access_token = data['access']
        else:
            url = self.URL_API.format(host=self.host, api_point=self.API_TOKEN_OBTAIN)
            data = self.send(url, {'api_key': self.api_key}, 'post')
            (self.access_token, self.refresh_token) = data['access'], data['refresh']


        if data != None:
            logger.info('Token recived: {0}'.format(data['access']))
            self.headers = {
                'Accept': self.HEADER_ACCEPT,
                'Authorization': self.HEADER_AUTHORIZATION.format(access_token=self.access_token)
            }

            return
        else: raise TokenInitializationError()


        # todo implement get_users
    def get_users(self):
        """
        List all users added to CPM sever
        :return:List of users in JSON format (list(dict))
        """
        data = self.send(
            self.URL_API.format(host=self.host, api_point=self.API_USERS),
            {'api_key': self.api_key}
        )
        logger.info('Executed get_users()')
        logger.debug('Executed get_users(): {0}'.format(data))

        return data

    def get_user(self, name):
        """
        gets user by name
        :param name: username how it set in CPM - should be exactly the same
        :return: JSON of user data (dict) or None if name is incorrect
        """
        users = self.get_users()
        for user in users:
            if user['username'] == name:
                return user

        logger.warning('Searching for user "{0}" failed. User not found.'.format(name))
        return None
    def get_accounts(self):
        """
        Lists AWS accounts added
        :return: JSON list of accounts (list(dict))
        """
        data = self.send(
            self.URL_API.format(host=self.host, api_point=self.API_ACCOUNTS),
            {'api_key': self.api_key}
        )
        logger.debug('Executed get_accounts(): {0}'.format(data))
        return data
    # todo implement get_accounts
    # todo implement get_schedules
    # todo implement get_polices
    # todo implement get_backups

    # todo implement create_policy
    # todo implement create_schedule
    # todo implement create_account
    # todo implement cleanup

    # todo implement send() update
    def send(self, url, data=None, method='get'):
        """
        Sends any type of data via get or post methods
        :param url: API point url, the whole line with https:// (string)
        :param data: JSON data for sending post request - (dict)
        :param method: POST or GET (if omitted)
        :return: JSON data response - (dict)
        """
        logger.debug('Opening {0}'.format(url))

        if method == 'post':
            response = requests.post(
            url=url,
            headers=self.headers,
            data=data,
            verify=self.VERIFY_SSL)
        else: response = requests.get(
            url=url,
            headers=self.headers,
            verify=self.VERIFY_SSL)

        if response.status_code != 200:
            logger.error(
                'Status code error: HTTP status code should be "200" OK instead of "{0}".\n{1}'.format(
                    str(response.status_code),
                    response.content)
            )
            return None
        return response.json()


def start_descrption():
    errors = list()
    return errors

#wk = CPMworker(os.environ.get('CPMAPIHOST'),os.environ.get('CPMAPIKEY'))
#print(wk.get_accounts())

