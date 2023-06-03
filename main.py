import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import os


SEARCH_URLS = {
    # Existing social media platforms
}

# Additional social media platforms
ADDITIONAL_PLATFORMS = {
    'Twitter': 'https://twitter.com/{}',
    'Facebook': 'https://www.facebook.com/{}',
    'Instagram': 'https://www.instagram.com/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    'Pinterest': 'https://www.pinterest.com/{}',
    'Reddit': 'https://www.reddit.com/user/{}',
    'Tumblr': 'https://{}.tumblr.com',
    'Snapchat': 'https://www.snapchat.com/add/{}',
    'GitHub': 'https://github.com/{}',
    'YouTube': 'https://www.youtube.com/user/{}',
    'Twitch': 'https://www.twitch.tv/{}',
    'WhatsApp': 'https://api.whatsapp.com/send?phone={}',
    'WeChat': 'https://web.wechat.com/{}',
    'Line': 'https://line.me/ti/p/{}',
    'Viber': 'viber://chat?number={}',
    'Telegram': 'https://t.me/{}',
    'Discord': 'https://discord.com/users/{}',
    'Medium': 'https://medium.com/@{}',
    'SoundCloud': 'https://soundcloud.com/{}',
    'Vimeo': 'https://vimeo.com/{}',
    'Flickr': 'https://www.flickr.com/people/{}',
    'Slack': 'https://{}.slack.com',
    'Dribbble': 'https://dribbble.com/{}',
    'Behance': 'https://www.behance.net/{}',
    'DeviantArt': 'https://www.deviantart.com/{}',
    'Mixcloud': 'https://www.mixcloud.com/{}',
    'Goodreads': 'https://www.goodreads.com/user/show/{}',
    'Quora': 'https://www.quora.com/profile/{}',
}

# Combine the existing and additional platforms
SEARCH_URLS.update(ADDITIONAL_PLATFORMS)

class UsernetGUI:
    def __init__(self, master):
        self.master = master
        master.title("Usernet")
        master.geometry("1920x1080")

        self.logo_image = tk.PhotoImage(file="lg/Onionkey.png")

        self.logo_label = tk.Label(master, image=self.logo_image)
        self.logo_label.pack(pady=20)

        self.username_label = tk.Label(master, text="Username", font=("Arial", 24, "bold"))
        self.username_label.pack()

        self.username_entry = tk.Entry(master, font=("Arial", 18))
        self.username_entry.pack(pady=10)

        self.search_button = tk.Button(master, text="Check Availability", command=self.check_username_availability, font=("Arial", 16), bg="#4CAF50", fg="white", relief=tk.RAISED, bd=0, padx=20, pady=10)
        self.search_button.pack(pady=10)

        self.results_frame = tk.Frame(master)
        self.results_frame.pack(pady=20)

        self.columns = 7  # Number of columns to display the results
        self.column_frames = []  # Frames for each column
        self.column_labels = []  # Labels for each column

        # Create frames and labels for each column
        for _ in range(self.columns):
            column_frame = tk.Frame(self.results_frame)
            column_frame.pack(side=tk.LEFT, padx=10)
            self.column_frames.append(column_frame)

            column_label = tk.Label(column_frame, font=("Arial", 16, "bold"))
            column_label.pack()
            self.column_labels.append(column_label)

        self.ascii_art = tk.Label(master, text="Created by Hoso", font=("Courier", 14))
        self.ascii_art.pack(side=tk.LEFT, padx=10)
        self.ascii_art.bind("<Button-1>", lambda e: self.open_url('https://github.com/Onionkey'))
        self.ascii_art.config(fg="blue", cursor="hand2")

    def check_username_availability(self):
        username = self.username_entry.get()
        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return

        self.clear_results()

        column_index = 0  # Index of the current column

        for platform, search_url in SEARCH_URLS.items():
            url = search_url.format(username)
            exists = self.check_username_exists(url)

            result_label = tk.Label(self.column_frames[column_index], text=platform, font=("Arial", 14))
            result_label.pack()

            if exists:
                result_available = tk.Label(self.column_frames[column_index], text="Username exists", font=("Arial", 12, "italic"), fg="#4CAF50", cursor="hand2")
                result_available.pack()
                result_available.bind("<Button-1>", lambda e, u=url: self.open_url(u))
            else:
                result_not_available = tk.Label(self.column_frames[column_index], text="Username does not exist", font=("Arial", 12, "bold"), fg="red")
                result_not_available.pack()

            column_index = (column_index + 1) % self.columns

    def check_username_exists(self, url):
        try:
            with open(os.devnull, 'w') as devnull:
                subprocess.check_output(['curl', '-I', url], stderr=devnull)
            return True
        except subprocess.CalledProcessError:
            return False

    def open_url(self, url):
        webbrowser.open(url)

    def clear_results(self):
        for column_frame in self.column_frames:
            for widget in column_frame.winfo_children():
                widget.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    usernet_gui = UsernetGUI(root)
    root.mainloop()
