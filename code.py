# from googlesearch import search


# query="aws-certified-data-engineer-associate-dea-c01 discussion question {}"

# with open("examtopics_aws_deaC01_qs.txt","w") as file:
#     for i in range(1,153):
#         top_result=list(search(query.format(i),sleep_interval=200,num_results=1))[0]
#         if top_result:
#             print(i,top_result)
#             file.write(top_result+'\n')
#         else:
#             print(i,"No result")
#             continue

from googlesearch import search
import time
import random

query = "aws-certified-data-engineer-associate-dea-c01 discussion question {}"

with open("aws_dataEngineering_2.txt", "w") as file:
    for i in range(1, 192):
        try:
            # Perform Google search and retrieve the top result
            top_results = list(search(query.format(i), stop=1))
            if top_results:
                top_result = top_results[0]
                print(i, top_result)
                file.write(top_result + '\n')
            else:
                print(i, "No result")
            
            # Wait a random amount of time to avoid detection
            time.sleep(random.uniform(3, 6))  # Random sleep between 3 and 6 seconds
        except Exception as e:
            print(f"Error occurred for question {i}: {e}")
            continue


