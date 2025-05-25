def get_valid_rating(min_rating: float = 0.0, max_rating: float = 5.0) -> float:
    while True:
        try:
            rating = float(input(f"What's the rating of the restaurant? ({min_rating}-{max_rating}): "))
            if min_rating <= rating <= max_rating:
                return max_rating
            else:
                print(f"Please, put a number between {min_rating} and {max_rating}.")
        except ValueError:
            print("Invalid input, please put a numeric value.")

def classify_rating(rating: float) -> str:
    
    if rating >= 4.5:
        return "Extraordinary"
    elif rating > 4:
        return "Excelent"
    elif rating > 3:
        return "Good"
    elif rating > 2:
        return "Fair"
    else:
        return "Poor"
    
def main():
    rating = get_valid_rating()
    category = classify_rating(rating)
    print(f"The restaurant is {category}.")

if __name__ == "__main__":
    main()