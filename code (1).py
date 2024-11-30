from googlesearch import search
import time
import random

query = "inurl:examtopics.com inurl:exam-az-500-topic-{}-question-{}-discussion"

with open("az-500-questions.txt", "w") as file:
    topic = 1
    while True:  # Infinite loop for topics
        question = 1
        topic_has_results = False  # Flag to track if the topic has any results

        while True:  # Infinite loop for questions within a topic
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
                
                # Increment question and wait a random amount of time to avoid detection
                question += 1
                time.sleep(random.uniform(3, 10))
            except Exception as e:
                print(f"Error occurred for Topic {topic}, Question {question}: {e}")
                continue
        
        if not topic_has_results:
            # Stop the topics loop if no results for the first question of the topic
            print(f"No results for Topic {topic}. Stopping topic search.")
            break
        
        # Increment topic for the next iteration
        topic += 1