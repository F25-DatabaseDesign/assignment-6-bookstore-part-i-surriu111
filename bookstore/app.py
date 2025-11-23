from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

categories = [
    [1, "Poem"],          
    [2, "Philosophy"],    
    [3, "Biography"],     
    [4, "Literature"]  
]


# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

books = [
    # (categoryId = 1)
    [1, 1, "Leaves of Grass", "Walt Whitman", "978-0142437347", 12.99, "leaves_of_grass", 1],
    [2, 1, "The Raven", "Edgar Allan Poe", "978-0486270505", 8.99, "the_raven", 0],
    [3, 1, "Divine Comedy", "Dante Alighieri", "978-0140448955", 14.50, "divine_comedy", 1],
    [4, 1, "The Sun and Her Flowers", "Rupi Kaur", "978-1449486792", 13.99, "sun_and_her_flowers", 0],

    # (categoryId = 2)
    [5, 2, "Meditations", "Marcus Aurelius", "978-0812968255", 9.99, "meditations", 1],
    [6, 2, "The Republic", "Plato", "978-0141442433", 11.50, "the_republic", 0],
    [7, 2, "Beyond Good and Evil", "Friedrich Nietzsche", "978-0140449235", 10.99, "beyond_good_and_evil", 1],
    [8, 2, "Critique of Pure Reason", "Immanuel Kant", "978-0486432540", 12.50, "critique_of_pure_reason", 0],

    # (categoryId = 3)
    [9, 3, "Steve Jobs", "Walter Isaacson", "978-1451648539", 15.99, "steve_jobs", 1],
    [10, 3, "Long Walk to Freedom", "Nelson Mandela", "978-0316548182", 14.99, "long_walk_to_freedom", 0],
    [11, 3, "The Diary of a Young Girl", "Anne Frank", "978-0553296983", 13.50, "diary_of_a_young_girl", 1],
    [12, 3, "Einstein: His Life and Universe", "Walter Isaacson", "978-0743264730", 16.50, "einstein_life_universe", 0],

    # categoryId = 4)
    [13, 4, "Pride and Prejudice", "Jane Austen", "978-1503290563", 9.50, "pride_and_prejudice", 1],
    [14, 4, "1984", "George Orwell", "978-0451524935", 8.99, "1984", 0],
    [15, 4, "To Kill a Mockingbird", "Harper Lee", "978-0061120084", 10.99, "to_kill_a_mockingbird", 1],
    [16, 4, "The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 9.99, "the_great_gatsby", 0]
]

# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable

    # Create a new list called selected_books containing a list of books that have the selected category

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    category_id = request.args.get('categoryId', type=int)
    
    selected_books = [book for book in books if book[1] == category_id]
    
    selected_category = next((cat[1] for cat in categories if cat[0] == category_id), "Unknown")
    
    return render_template('category.html', selected_category=selected_category, categories=categories, books=selected_books)


@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    
    search_results = [book for book in books if query in book[2].lower() or query in book[3].lower()]
    
    return render_template('search.html', query=query, categories=categories, books=search_results)


@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
    # the prot is 5000 as default
