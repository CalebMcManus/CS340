Caleb McManus
10/19/2025
SNHU CS 340
Project 2 ReadMe
Overview and Requirements
The project is to deliver a functioning and interactive web dashboard that allows the client, Grazioso Salvare, to explore the Austin Animal Center outcomes dataset and quickly find dogs that are used in three different rescues: Water, Mountain/Wilderness, and Disaster/Individual. The dashboard can provide an unfiltered data table, with filtering controls, interactable data table, a pie chart of the top breeds for the filter, and a Geolocational map. Below are screenshots of the dashboard with each filter:
    
Architecture & Tools
MongoDB is the model layer to interact with the data. It stores and returns JSON documents efficiently, best for semi-structured data. It also has python driver PyMongo which allows for easy integration. 
A custom CRUD Module which can be found in the files. (This is assuming uploaded to a place like GitHub). This provides the create, read, update, and delete methods need for this project and further expansion and use case of the data. In this case, the read is the one that is used for this project.
We used the Dash, as we use the Dash DataTable to display the data with sorting and filtering features built into the dashboard. We also made use of dash callbacks to be able to do a refresh on the map, view, and table selection. 
Run
Ultimately, these steps assume you’ve followed along with the course work of CS 340 SNHU. The dataset AAC is already loaded in the environment. 
1.	Open JupyterLab in your Codio environment (or local Jupyter).
2.	 Verify dependencies (already present in Codio):
a.	pymongo, pandas, dash, dash_table, dash_leaflet, plotly, jupyter_dash
3.	Configure credentials
a.	The sample code uses the aacuser account you created earlier.
b.	For security, prefer environment variables if you are running outside Codio:
c.	Run: 
Import os 
Username = os.getenv(("AAC_USERNAME", "aacuser")
password = os.getenv("AAC_PASSWORD", "YOUR_PASSWORD_HERE")
4.	Open this projects completed file and run, click on the generated URL
5.	Operated the dash to your content.
Dev Summary
 We imported the AAC data into the MongoDB and created a user account. Built a CRUD class built around the AAC database. Created the web based dashboard that has multiple features.
Challenges
I had a deep challenge of getting the filters to properly display. There was an issue where the read wasn’t reading the breed correctly and as a result the dashboard was not updating the pie chart and table correctly. I ended up having to probe the database to figure out the why the filters were not working and get the exact reading of the breed that was needed. I also added in a functionality that dropped the “_id” since I ran into uses with it on return. I had to also add in a fix to keep the data to auto load when loading the url as it would show blankly if nothing was selected in the filters. At First, I ended up having way too many slices displayed in the pie chart of the dashboard, I had to end up going back into the code and adding in a limit to how many breeds are displayed on the chart based on the top breeds of the filter.
Maintenance
In the future or proper deployment, use a login portal to avoid security issues with hardcoding login, as well as allowing multiple different users with different levels of uses and jobs to access. If the filter does not end up showing future added animals, make sure the animals is inputted correctly, mainly the breed as the system is built around the already established breed of the provided dataset.


Additional Prompts:
How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
-I tend to break everything down into smaller bits to be able to read what I'm doing along with using very clear comments and plenty of white space to break up the code. 
Instead of trying to fit all the function in one long running statement, I tried to use easily call statements that can operate independently and together. By breaking it down, it made the project more manageable and not very overwhelming.

How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
-By breaking down the goal of the code, and by keeping in mind the requirements, I end up easily for the most part, was able to access the data base by passing the correct commands through my easily plug and play CRUD module that interacts well with the Mongo dash terminal and api. I wouldn't necessarily say it was different, rather it simply had us combine the knowledge and process from the previous assignments into just this project to help guide us. I often used my assignments as refrence for the main code anyway. Compared to other course, I believe this is the first where I built a module from scratch to be applied to another code base. In other classes, I simply had a provided codebase that I needed to fix every week. 

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer scientist analyze data to produce desired outcomes, along with building workable code that is built to be flexable and able to be plugged into future database pluggin. Overall, with this project, this project would end up allowing a company be able to quickly search through their database which can consist of thousands of entry documents and growing.
