import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, original_url):
        hash_object = hashlib.sha256(original_url.encode())
        hex_dig = hash_object.hexdigest()[:8]
        self.url_map[hex_dig] = original_url
        return f"Your shortened URL: http://your-shortened-domain.com/{hex_dig}"

    def get_original_url(self, short_code):
        return self.url_map.get(short_code, "URL not found")

shortener = URLShortener()
original_url = "https://www.examplelongwebsiteurl.com/articles/how-to-build-a-url-shortener-with-python-and-flask-a-step-by-step-guide-for-beginners"
shortened_url = shortener.shorten_url(original_url)
print(shortened_url)
