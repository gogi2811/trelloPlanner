# trello-planner
Automation script to create Weekly/half-yearly/Yearly planner 

Forming a new habit is hard especially the good ones, if you don't agree with me then we can't be friends.

Many well known people have written books on how to create a new habit and stick to it , my favorite one is  [Atomic habits](https://jamesclear.com/atomic-habits) do read it will change the way you think.

Little introduction about myself , I am a Software Engineer working majorly in the Data Engineering domain. I enjoy doing some side projects for myself and sometimes indulge in freelancing , that :sushi: ain't getting cheap :stuck_out_tongue_winking_eye:.

---
# Motivation :fire: :fire:
I have struggled in the past with habit formation and following up with a daily constant routine, what worked for me most of the time was if I had my to-dos for any given day.
My productivity would increase and was able get more things done.
This led to my quest for a creating my daily/weekly/monthly todo list , but the tools that I used required manual entry of all the Tasks and I hated it when I had to it for months.
I am lazy

Here lies a problem and  [Trello ](https://trello.com/en) came as a savior with its magic API's.

## Trello  and Python to the rescue :snake:
Trello is task management tool used by startups and individuals to track the tasks and their progress, to be put up simply.
Trello exposes it  [API's](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)  to do CRUD operations on trello boards  and that's exactly what I did with a little help of Python

> Talk is cheap. Show me the code --  Linus Trovalds

---
### Pre-requisites
Both tech and non-tech audiences can use it with a lil bit of guidance.

-  [Python 3+ installed](https://www.python.org/downloads/)  on your machine

- Git clone or download the repository on to your machine
> git clone https://github.com/gogi2811/trello-planner.git

- **Obtain Trello token + Key + board_id**
      
     -  [SignIn/SignUp](https://trello.com/signup)  in trello
     
     -  [Create a Board in Trello](https://help.trello.com/article/707-creating-a-new-board) 
     - Post board creation obtain the board_id by going inside the board and modifying the URL to add **.json** at the end.
     Example > https://trello.com/b/PxEQPoMz/reports**.json**

     -  Obtain [API key](https://trello.com/app-key) 
   
     - Get [Token](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=f016002d1fa8b28249dbc01d89cb2324) based on API key


- Update the config file with your details.

### Configuration File Walk-through
------------
    ├── config.yaml     <- Config file to be updated
    │   ├── planner      <- tag not be messed up
    │       ├── trello:
    │                         token: abc123 <- trello token obtained in previous step
    │                         key: zyx123  <- trello API key obtained in previous step
    │                         board_id: zyx123  <- trello baord _id obtained in previous step
    │       ├── dates:
    │                        start_date: 2021-08-09 <- user specific start date from where the 
                                                                               planning is to be started
    │                        end_date: 2021-12-30 <- user specific end date from where the 
                                                                               planning is to end                                                 
 
--------

### Structure of the Daily Planner
Below file contains details about how the actual day-day to-do's can be configured for weekly/half-yearly basis as per our needs
File can be found inside the repo:  [week_planner.json](https://github.com/gogi2811/trello-planner/blob/main/week_planner.json) 

```{
  "LISTS": [
    {
      "MONDAY": {
        "CARDS": [
          {
            "name": "4:45 AM Wake UP",
            "desc": "To wake up everyday to exercise at 5 AM",
            "pos": "top",
            "due": "",
            "idList": ""
          },
		  {
            "name": "10:30 PM  SLEEP",
            "desc": "Wind off the day and sleep",
            "due": "",
            "idList": ""
          }
        ]
      }},{"TUESDAY": {
        "CARDS": [
          {
            "name": "4:45 AM Wake UP",
            "desc": "To wake up everyday to exercise at 5 AM",
            "pos": "top",
            "due": "",
            "idList": ""
          },
		  {
            "name": "7 AM - 8 AM household chores",
            "desc": "To do some household chores",
            "due": "",
            "idList": ""
          },
		  
        ]
      }},{"WEDNESDAY": {
        "CARDS": [
          {
            "name": "4:45 AM Wake UP",
            "desc": "To wake up everyday to exercise at 5 AM",
            "pos": "top",
            "due": "",
            "idList": ""
          }	  
	  ]}
    }
  ]
}
``` 
One needs to update the actual file with their respective tasks or habits that they want to build over time and have them as their day-to-day tasks on trello.
 
---
### Next steps

Lets get down to business of creating the trello dashboards for better life going forward.

- Open the clone or downloaded git repo in your fav IDE, mine is  [Pycharm](https://www.jetbrains.com/pycharm/)  [Visual Studio Code](https://code.visualstudio.com/download)  works too.

- Open terminal tab inside the IDE
     -  [PyCharm](https://www.jetbrains.com/help/pycharm/terminal-emulator.html) 
     -  [VSCode](https://code.visualstudio.com/docs/editor/integrated-terminal#:~:text=To%20open%20the%20terminal%3A,View%3A%20Toggle%20Integrated%20Terminal%20command.) 

Let the hacking begin :computer: :closed_lock_with_key:
![terminal.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1628403886685/SI6_e89PMm.gif)

Run below cmd in your respective terminal 
- Set up virtual env for your project
    - Linux/MacOS > python3 -m venv trelloPlanner
    - Windowd > python -m venv trelloPlanner

- Install all the required packages/dependencies
  - > pip install -r requirements.txt

- Start the newly created virtualenv
  - Linux/MacOS > source trelloPlanner/bin/activate
  - Windows > .\trelloPlanner\Scripts\activate

- Once started execute the below cmd and the let the magic unfold 
   > python main.py


![3da178af3ef521d9294ccf09d53ba754125b492b.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1628406680412/JgbtkSP6x.gif)

Now sit back and relax and watch your life get organized by day in front of you.

![chill-zen.gif](https://cdn.hashnode.com/res/hashnode/image/upload/v1628405610459/c5vgLjtLq.gif)

### Learnings & Benefits
 1. We saved __70%__ of our time that would have gone if done manually.
 2. We learnt about Trello API's + Python.
 3. What we learnt in the process is Automation helps a lot in accomplishing the desired goals faster, better and less error prone manner

### Going Forward
I would recommend all of you lovely folks reading this blog to go through  [Trello ](https://trello.com/en) boards and let me know what else would you like in your tasks
and create  [Issues/Feature Requests ](https://github.com/gogi2811/trello-planner/issues) in my github repo so that I can add them in next iteration.

---
 [GitHub Repo for the Code
](https://github.com/gogi2811/trello-planner) 
Share among your peeps
