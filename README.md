# Database-Ai-Agent-NexusRavenV2

In the world of data-driven decision-making, the ability to query and interact with databases efficiently can significantly streamline workflows. In this project, I developed a Database AI Assistant that allows users to interact with databases using natural language, making database queries more accessible, especially for non-technical users. The app leverages Streamlit for the frontend, Python for the backend, and NexusRavenV2-13B, a cutting-edge Large Language Model (LLM), to handle natural language processing (NLP) and SQL generation. By utilizing function calling and tools, I built a web app solution that transforms conversational input into SQL queries, all while maintaining a high degree of accuracy and performance.

<img width="1024" alt="appimage" src="https://github.com/user-attachments/assets/e9b8e7d5-86ea-4cba-8960-b4f72c1ec2e8">


### Why NexusRavenV2-13B?

I chose NexusRavenV2-13B because of its powerful natural language understanding and ability to generate high-quality responses based on context. NexusRavenV2-13B excels at understanding complex queries and interpreting user intent, making it ideal for translating user input into SQL queries.

What sets this version apart is its ability to handle function calling. Instead of generating SQL from scratch every time, which comes with its own cost and latency, the agent leverages predefined SQL functions that are optimized for common tasks. This ensures that queries are more efficient, especially when dealing with large databases or complex operations.

### Why Streamlit?

For the frontend, I used Streamlit, which is a fast, open-source framework for building web apps with minimal effort. Streamlit is perfect for projects like this, where you want to focus on functionality without spending much time on complex UI development. The UI is clean, interactive, and easy to extend, which made it ideal for this project.

With Streamlit, I was able to create:

1. A user-friendly interface to input natural language queries.
2. Real-time updates for displaying query results and insights.
3. Minimal overhead by handling most of the logic in Python, keeping the codebase concise.

### Key Features of the Database AI Agent

##### Natural Language Processing (NLP): 
The agent can understand a wide range of questions and queries in plain English, from simple requests like "Show me the sales data from last month" to more complex queries involving joins or aggregate functions.

##### Function Calling for SQL Optimization: 
By using function calls and predefined tools, the agent ensures that the generated SQL queries are not only syntactically correct but also optimized for the task at hand.

##### Real-time Query Execution: 
Once the SQL query is called based on the user input, the agent then generates the SQL query using the predefined function and executes it on the connected database and the results are displayed immediately with low latency. 

### Future Improvements

##### While the app is already functional, there are several areas for future enhancement:

1. Advanced Query Support: Adding more complex SQL functionality, like subqueries or window functions, to handle more sophisticated use cases.
2. User Personalization: Incorporating user-specific preferences or history to tailor SQL generation to different workflows or data models.
3. Security and Access Control: Implementing user authentication to ensure secure database access, especially when dealing with sensitive data.
4. Query Optimization Insights: Providing feedback on how to optimize queries for better performance or suggesting database indexing strategies.
5. Adding necessary guardrails to catch any errant behavior by the model.

### Limitations

1. A large number of functions will saturate the context window of NexusRaven-V2 .
2. The model can be prone to generate incorrect calls hence there is a need for proper guardrails to capture errant behavior is in place.

### Conclusion

The Database AI Agent App is a powerful tool that simplifies database interactions by allowing users to communicate with their databases in natural language. By combining Streamlit’s ease of use, NexusRavenV2-13B’s advanced NLP capabilities, and function calling for optimized SQL generation, this project demonstrates the potential of AI to enhance productivity and streamline complex tasks.

You can find the source code on GitHub and feel free to connect with me on LinkedIn to discuss improvements, feedback, or potential collaborations.

#### Feedback & Contributions: 
I welcome any suggestions, bug reports, or contributions to enhance this project. \
    GitHub: https://github.com/ola-sam/Database-Ai-Agent-NexusRavenV2 \
    LinkedIn: https://www.linkedin.com/in/samelegure/
