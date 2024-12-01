from googlesearch import search
import time
import random

# Define the query template
query = "examtopics.com exam-az-500-topic-{}-question-{}-discussion"

# Enter the topic number manually
topic = int(input("Enter the topic number: "))
max_questions = int(input("Enter the maximum number of questions: "))

# Open a file to write results
with open("az-500-questions.txt", "w") as file:
    topic_has_results = False  # Flag to track if the topic has any results

    for question in range(1, max_questions + 1):  # Loop through the specified number of questions
        try:
            # Perform Google search for the current topic and question
            formatted_query = query.format(topic, question)
            top_results = list(search(formatted_query, num_results=1))

            if top_results:
                # If results are found, process the first result
                top_result = top_results[0]
                print(f"Topic {topic}, Question {question}: {top_result}")
                file.write(top_result + '\n')
                topic_has_results = True  # Indicate that this topic has results
            else:
                print(f"Topic {topic}, Question {question}: No result")
                # Stop the questions loop if no result is found for a question
                break

            # Wait a random amount of time to avoid detection
            time.sleep(random.uniform(3, 6))
        except Exception as e:
            print(f"Error occurred for Topic {topic}, Question {question}: {e}")
            continue

    if not topic_has_results:
        print(f"No results for Topic {topic}.")
    else:
        print(f"Search completed for Topic {topic}.")