import random

# Song recommendation database
song_recommendations = {
    "happy": [
        ("Senorita", "https://youtu.be/ow1QqW0jzTo"),
        ("Don't worry", "https://youtu.be/ksANu45I16U"),
        ("Love you zindagi", "https://youtu.be/rwn0Zs7ELzc")
    ],
    "sad": [
        ("Bisilu kudureyondu", "https://youtu.be/N4GFIkcp5Wo"),
        ("agar tum saath ho", "https://youtu.be/sK7riqg2mr4"),
        ("Ivanu geleyanalla", "https://youtu.be/0OMjQgxdxIE")
    ],
    "love": [
        ("Eno eno agide", "https://youtu.be/sWk9lpkGAfs"),
        ("Kaise Hua", "https://youtu.be/_P9YXESg5Es"),
        ("Jagave neenu gelatiye", "https://youtu.be/Y-yK6J9i95E")
    ],
    "party": [
        ("Party freak", "https://youtu.be/zJSP3I1lCco"),
        ("3 peg", "https://youtu.be/QdvLj9Wr8Q0"),
        ("mental hojava", "https://youtu.be/szSta8tt-3Y")
    ]
}

# Function to get a song recommendation based on the user's mood.
def get_song_recommendation(mood):
    if mood.lower() in song_recommendations:
        song, link = random.choice(song_recommendations[mood.lower()])
        return f"Song: {song}, Link: {link}"
    else:
        return "Sorry, I don't have any song recommendations for that mood."

# Function to add a new song to the song recommendation database
def add_song(mood, song):
    if mood.lower() in song_recommendations:
        song_recommendations[mood.lower()].append(song)
    else:
        song_recommendations[mood.lower()] = [song]

def main():
    print("Welcome to Song Recommender!")
    print("Available moods: happy, sad, love, party")

    while True:
        user_input = input("Enter your current mood (or 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        song = get_song_recommendation(user_input)
        print(f"Recommended song: {song}")

if __name__ == "__main__":
    main()
