from pytube import Playlist
from queue import Queue
import bs4
import requests
import threading

playlist_url_list = []

playlist_titles_txt_file = []

def f_main(f_main_playlist, f_main_titles_list):

    playlist= Playlist(f_main_playlist)

    def f_threading_target(f1_link, f1_queue, f1_index):
        try:
            response = requests.get(f1_link)
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            title_tags = soup.find_all('title')
            f1_queue.put((f1_index, title_tags))
        except Exception as e:
            f1_queue.put((f1_index, e))

    def f_fetch(f2_links):
        f2_threads = []
        f2_queue = Queue()
        f2_results = [None] * len(f2_links)

        for _, __ in enumerate(f2_links):
            f2_thread = threading.Thread(target=f_threading_target, args=(__, f2_queue, _))
            f2_threads.append(f2_thread)
            f2_thread.start()

        for thread in f2_threads:
            thread.join()

        while not f2_queue.empty():
            f2_index, f2_title = f2_queue.get()
            f2_results[f2_index] = f2_title

        return f2_results

    titles = f_fetch(playlist)
    print(len(titles))

    with open(f"{f_main_titles_list}.txt", "w", encoding="utf-8") as f:
        for _ in range(len(titles)):
            try:
                f.write(f"{_+1})\nTitle: {titles[_][0].get_text().split(" - YouTube")[0]}\nLink:{playlist[_]}\n\n---\n\n")
            except ConnectionError:
                f.write(
                    f"{_ + 1})\nTitle: ''\nLink:{playlist[_]}\n\n---\n\n")

    print(f"Done {f_main_titles_list}")


for i in range(len(playlist_url_list)):
    f_main(playlist_url_list[i], playlist_titles_txt_file[i])
