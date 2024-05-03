***
Josh Ganatta
***
# <p style="text-align: center;">Electromagnetic Spectrum Emissions Planning Tool for Large Scale Combat Operations</p>
### **Problem**
How do Battalion Main Command Posts evolve to be mobile, redundant, and survivable with existing equipment on hand while avoiding advanced enemy electromagnetic target acquisition?
***
### **Software Solution**
Electromagnetic (EM) planning tool taking anticipated military electronics equipment to be utilized as input and provides EM signature output for planning purposes and course of action development.
 * Military Equipment EM Emissions - ***Partially accomplished (database)***
 * Satellite Imagery Overlay - ***Not accomplished***
 * Location Grid Input - ***Accomplished***
 * Equipment EM Emmision Diameter - ***Not accomplished***
 * Enemy EM Emissions Detection Parameters - ***Not accomplished***

This module allows users to plot EM emissions Latitude and Longitude grids onto maps.
***
### **Django-Choices and Mods to the Model**
 1) Django Rest Framework for API
 2) Django Channels for the External Message Queue
 3) Django does its own bootstrapping and we'll partially forego DI
 4) Django Signals for the Interal Message Queue
 5) Django apps use views to provide these handlers
 6) Django ORM transactions handle this
 7) Don't fight the monolith, will not implement
 8) Redis
 9) Domain intact

 ![alt text](<outside_scope/png/9 steps.png>)
 Image 1: Dr. Babb's Workflow of Percival and Gregory's Domain Model
 ***


### **Diagram Sketches**
The notion of the EM Planning Software provided a baseline to conceptualize sketching Unified Modeling Language (UML) Diagrams.

#### **Class Diagram**
This diagram examines the relationships between the military commander, EM emission sensor data collection Soldier, data messaging, database writing/reading, and map point plotting.  Although rudimentary, the thought experiment created a foundation to build the real life event sensory effect into a visualization tool for the commander to make informed decisions.
![alt text](<outside_scope/png/Class Diagram.drawio.png>)
 Image 2: Assignment 3 Class Diagram UML

#### **Activity Diagram**
This diagram surveys the flow of commander's intent to Solder and equipment actions creating sensed data for analysis and digestion.  Ultimately driving visual data into the Common Operating Picture for decision making.
![alt text](<outside_scope/png/Activity Diagram.drawio.png>)
 Image 3: Assignment 3 Activity Diagram UML

#### **Sequence Diagram**
This diagram outlines the progression of doctrine generating workflow and directing military decision-making process by organization's staff officers. The sequence of events triggers our EM Planning Tool's use for future operations planning.
![alt text](<outside_scope/png/Sequence Diagram.drawio.png>)
 Image 4: Assignment 3 Sequence Diagram UML

#### **Use Case Diagram**
This diagram depicts equipment transmitting EM emissions being captured by EM sensor equipment, the Soldier repsonsible for that data processing and fighting prouduct creation, and the commander who drives resource allocation.
![alt text](<outside_scope/png/Use Case Diagram.drawio.png>)
 Image 5: Assignment 3 Use Class Diagram UML
***
### **TDD Approach Used**
The UML diagrams provided context to perceive potential tests.  My intial list of testing ideas held throughout development with evolution and grouping occuring naturally. 

<ins>Initial testing ideas</ins>:
 * Latitude / Longitude grid point off map / outlier
 * Read CSV (EM Database)
 * Min/Max Latitudes Longitudes
 * The map file get path
 * Figure size, marker size, x/y limits
 * Matplolib alpha transparency, graph title/labels/legend

 <ins>Testing used</ins>:
  * User
  * EMData
  * LatLongPoints
  * Colors
  * FrequencyDevice
  * DataConversion
  * DateTime
  * FakePlotting
  * Mapping
  * Layout

 With Percival and Gregory's examples of Test Driven Design (TDD) architecture approach, I 
***
### **Problem Overview**
The past twenty years of warfare has focused on Counterinsurgency (COIN) operations with adversaries that did not have the same capabilities.  The lessons learned and best practices from this asymmetric warfare serve as the foundation for the next phase of anticipated conflict.  The US Army has accepted Large Scale Combat Operations (LSCO) as the methodology of conflict with near-peer adversaries such as Russia or China.  As the world watches the on-going LSCO in Ukraine, warfighting lessons become apparent to all echelons of our servicemembers….and our adversaries.  The way we fought in Afghanistan and Iraq for COIN will not work for LSCO.

Near-peer adversaries have similar capabilities to the Department of Defense (DoD) across all five domains of warfare: land, sea, air, space, and cyberspace.  Large Scale Combat focuses on massing combat power to attrit enemy forces and acquire territory to deny enemy advantage.  In COIN, Tactical Operation Centers (TOC) were the means of controlling the fight.  TOCs had robust capabilities and encouraged warfighting functions to synchronize efforts against the enemy.  After twenty years of fighting, we fell victim to what all bureaucracies develop with time.  TOCs became too big and lack mobility, the term “TOC-mahals” is commonplace because of their complexity.  TOCs primary issue within the LSCO framework is the lack of mobility.

LSCO adversaries maintain indirect fire, air attack, and cyber and electronic warfare (EW) capabilities.  They have the means of discovering the location and destroying Main Command Posts (MCP).  TOC = static.  MCP = light and mobile.  Both TOCs and MCPs are types of command posts and provide a physical location for planners, combat systems, and the required IT network.

The process of military acquisitions is slow.  Years even.  If the threat of near-peer adversaries exists today, the military cannot wait for the acquisitions process to fill emerging requirements.  We need to figure out potential solutions to this problem set with the already appropriated equipment and capabilities.

***
![EM Example from NTC](https://www.thedrive.com/content/2020/05/electronic-warfare-top.jpg?quality=85&auto=webp&optimize=high&crop=16%3A9&auto=webp&optimize=high&quality=70&width=1920)
[Image 6][EM Image]: Battalion Main Command Post Large Electromagnetic Signature
***
### **Domain**
The domain is mission analysis and military decision making process forecasting for survivability utilizing the Electromagnetic Spectrum detection avoidance measures.
### **Professional Interest**
I am a US Army Signal Officer (communications), and this proposed tool offers preventative risk to force acceptance.  I am in a position where I see a different Brigades in a tough and realistic LSCO training environment monthly.  EM detection and the enemy's ability to rapidly engage with indirect fires is a recurrent issue where feasible solutions do not align with acceptable solutions.
### **Prototype Proposal**
My proposed prototype will be a rudementary forecasting tool utilizing publicly accessable satellite imagery, overlay graphics input representing EM emissions, and reference data tables on EM emissions and detection capabilities.  The prototype is not meant to be a solution to the problem, rather a fundamental approach to propose development for existing military systems incorporation. 
***
### **References**
1. Image 1: Dr. Babb's Workflow of Percival and Gregory's Domain Model. CIDM 6330 Slides: <ins>CIDM6330-MessagesQueues</ins>. Slide 23.
2. Image 2: Assignment 3 Class Diagram UML.
3. Image 3: Assignment 3 Activity Diagram UML.
4. Image 4: Assignment 3 Sequence Diagram UML.
5. Image 5: Assignment 3 Use Case Diagram UML.
6. [Image 6][EM Image]: ["This is What Ground Forces Look Like to an Electronic Warfare System and Why It's a Big Deal" by Joseph Trevithick](https://www.thedrive.com/the-war-zone/33401/this-is-what-ground-forces-look-like-to-an-electronic-warfare-system-and-why-its-a-big-deal)
7. ["Preparing for Large-Scale Combat Operations" by Center for Army Lessons Learned](https://api.army.mil/e2/c/downloads/2023/01/31/73b50bab/21-6-preparing-for-lsco-public.pdf)

[EM Image]: https://www.thedrive.com/the-war-zone/33401/this-is-what-ground-forces-look-like-to-an-electronic-warfare-system-and-why-its-a-big-deal