### Process
1. Create the folder structure
2. Create a new env
3. Install the req
4. Create 3 agents: Research, Summarize and Map
5. Get Euri Api and Surfer Api (https://serpapi.com/manage-api-key)
6. Define the functions of all the 3 tools
7. Build the work of "*researcher*" using wikipedia tool and serper tool
8. Build synthesizer (summariser) using EURI tool and the data received from reseracher
9. Finally, build the mapper which takes synthesized text and split it to prepare the node and edge
10. Now, combine all these 3 tasks at 1 place in langgraph_router inside workflow
11. Use GraphState (where nodes comminicate)
12. Also, download graphviz from https://graphviz.org/download/