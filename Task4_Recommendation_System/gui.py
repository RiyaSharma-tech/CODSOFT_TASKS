import tkinter as tk
from tkinter import messagebox
from recommandation import recommend_movies

# Window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("550x500")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="🎬 Movie Recommendation System",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

# Label
label = tk.Label(
    root,
    text="Enter Movie Name:",
    font=("Arial", 12)
)
label.pack()

# Entry Box
movie_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
movie_entry.pack(pady=10)

# Text Box
result_box = tk.Text(
    root,
    width=55,
    height=15,
    font=("Arial", 11)
)
result_box.pack(pady=10)
result_box.config(state=tk.DISABLED)

# Button Function
def recommend():

    # Get movie name entered by user
    movie_name = movie_entry.get().strip()

    # Check if entry box is empty
    if movie_name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a movie name before requesting recommendations."
        )
        return

    # Get recommended movies
    movies = recommend_movies(movie_name)

    # Enable text box for editing
    result_box.config(state=tk.NORMAL)

    # Clear previous results
    result_box.delete(1.0, tk.END)

    # If movie is not found
    if not movies:
        result_box.insert(
            tk.END,
            "❌ Movie not found!\n\n"
            "Please check the spelling and try again.\n\n"
            "Examples:\n"
            "• Avatar\n"
            "• Titanic\n"
            "• The Dark Knight"
        )

        result_box.config(state=tk.DISABLED)
        movie_entry.focus()
        return

    # Display heading
    result_box.insert(
        tk.END,
        "🎬 Top 10 Recommended Movies\n\n"
    )

    # Display recommendations
    for i, movie in enumerate(movies, start=1):
        result_box.insert(
            tk.END,
            f"{i}. {movie}\n"
        )

    # Make text box read-only
    result_box.config(state=tk.DISABLED)

    # Clear entry box
    movie_entry.delete(0, tk.END)

    # Put cursor back in entry box
    movie_entry.focus()

# Button
button = tk.Button(
    root,
    text="Recommend Movies",
    font=("Arial", 12, "bold"),
    command=recommend,
    bg="skyblue",
    cursor="hand2"
)

button.pack(pady=10)

# Press Enter to recommend movies
root.bind("<Return>", lambda event: recommend())

footer = tk.Label(
    root,
    text="Developed by Riya",
    font=("Arial", 9),
    fg="gray"
)
footer.pack(side="bottom", pady=8)

root.mainloop()