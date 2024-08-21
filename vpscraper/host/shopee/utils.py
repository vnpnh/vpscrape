import re


def extract_rating_info(rating: str) -> dict[str, str]:
    rating_list = re.findall(r'\(\d+\)', rating)
    key_list = ['5 Bintang', '4 Bintang', '3 Bintang', '2 Bintang', '1 Bintang', 'Dengan Komentar', 'Dengan Media',
                'Langganan']
    all_rating = dict()
    for i, rating in enumerate(rating_list):
        all_rating[key_list[i]] = re.findall(r'\b\d+\b', rating)[0]


def extract_url(url: str) -> str:
    return re.findall(r'(https?://\S+)', url)[0][:-3]


