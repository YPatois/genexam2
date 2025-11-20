import diskcache
import abc


class ChemCache():
    """
    Chemcache
    """

    def __init__(self, cache_dir: str="chemcache"):
        """
        Initialize the cache with a cache directory.

        Args:
            cache_dir (str): The directory where the cache will be stored.
         """

        self._cache = diskcache.Cache(cache_dir)

    def get(self, key: str):
        """
        Get an item from the cache.

        Args:
            key (str): The key of the item.

        Returns:
            The item from the cache, or None if it does not exist.
        """
        return self._cache.get(key)


    def set(self, key: str, value: any):
        """
        Set an item in the cache.

        Args:
            key (str): The key of the item.
            value (any): The value of the item.
        """
        self._cache.set(key, value)

 