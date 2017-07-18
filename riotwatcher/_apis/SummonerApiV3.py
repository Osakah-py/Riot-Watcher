
from . import NamedEndpoint


class SummonerApiV3(NamedEndpoint):
    """
    This class wraps the Summoner-v3 endpoint calls provided by the Riot API.
    See https://developer.riotgames.com/api-methods/#summoner-v3 for more detailed information
    """
    def __init__(self, base_api):
        """
        Initialize a new SummonerApiV3 which uses the provided base_api

        :param base_api BaseApi: the root API object to use for making all requests.
        """
        super(SummonerApiV3, self).__init__(base_api, SummonerApiV3.__name__)

    def by_account(self, region, account_id):
        """
        Get a summoner by account ID.

        :param region string:   The region to execute this request on
        :param account_id long: The account ID.

        :returns: SummonerDTO: represents a summoner
        """
        return self._request(
            self.by_account.__name__,
            region,
            '/lol/summoner/v3/summoners/by-account/{accountId}'.format(accountId=account_id)
        )

    def by_name(self, region, summoner_name):
        """
        Get a summoner by summoner name

        :param region string:           The region to execute this request on
        :param summoner_name string:    Summoner Name

        :returns: SummonerDTO: represents a summoner
        """
        return self._request(
            self.by_name.__name__,
            region,
            '/lol/summoner/v3/summoners/by-name/{summonerName}'.format(summonerName=summoner_name)
        )

    def by_id(self, region, summoner_id):
        """
        Get a summoner by summoner ID.

        :param region string:       The region to execute this request on
        :param summoner_id long:    Summoner ID

        :returns: SummonerDTO: represents a summoner
        """
        return self._request(
            self.by_id.__name__,
            region,
            '/lol/summoner/v3/summoners/{summonerId}'.format(summonerId=summoner_id)
        )
