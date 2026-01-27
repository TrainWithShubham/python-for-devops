#Thinking Before Coding (DevOps Mindset)
#Script => api_data_fetcher.py Day-02 PyScript

1. The Problem that this script solving is?
=>  
A.Automates data retrieval
=>Fetches Pokémon info instantly instead of manual searching.

B.Filters useful data
=>Extracts only needed fields (name, id, height, weight) from a large API response.

C.Stores data for reuse
=>Saves structured data into a JSON file for later use.

D.Handles real-world errors
=>Manages invalid input, API failures, and network issues safely.

E.Practices real API usage
=> Teaches how software communicates with external services.


2. What input does this script need?

1.Input this script needs

A. A Pokémon name as a string

B. Entered by the user via the keyboard

2.Invalid input

A. Empty input ("")

3. What output should this script give?

1. Console Output

A. If the Pokémon exists (e.g., pikachu), the script prints:

=> A success message:

B. A formatted JSON object with:

name
id
height
weight

eg.
{
    "name": "pikachu",
    "id": 25,
    "height": 4,
    "weight": 60
}

2.File Output

A.Creates (or overwrites) a file called output.json

B.Saves the same Pokémon data in JSON format

4.What are the main steps?

A. Take user input
=> Ask the user for a Pokémon name.

B. Build the API request
=> Create the API URL using the base URL + Pokémon name.

C. Call the API
=> Send an HTTP GET request to the PokéAPI.

D. Validate the response
=> Check if the request was successful.

E. Parse the JSON data
=> Convert the API response into a Python dictionary.

F.🎯 Extract required fields
=> Select name, id, height, and weight.

G.🖨️ Display the output
=> Print the formatted Pokémon data.

H.💾 Save to file
=> Write the data to output.json.

I. Handle errors
=> Manage invalid input, API errors, and network issues.
