***
CPT G
***
# <p style="text-align: center;">**Electromagnetic Spectrum Emissions Planning Tool for Large Scale Combat Operations**</p>
### <h2>**Table of Contents**</h2>
- [Problem](#Problem)
- [Domain](#Domain)
- [Software Solution](#Software-Solution)
- [The CIDM 6330 Domain Model Challenge](#6330-Challenge)
- [Diagram Sketches](#Diagram-Sketches)
- [TDD Approach Used](#TDD-Approach)
- [Exploring Tests and their Validity](#Exploring-Tests)
- [Coding Route Taken](#Coding-Route)
- [Encountered Pitfalls](#Encountered-Pitfalls)
- [Exciting Revelation](#Exciting-Revelation)
- [Problem Overview](#Problem-Overview)
- [References](#References)
### <h2 id="Problem">**Problem**</h2>

How do Battalion Main Command Posts evolve to be mobile, redundant, and survivable with existing equipment on hand while avoiding advanced enemy electromagnetic target acquisition?

### <h2 id="Domain">**Domain**</h2>
The domain is mission analysis and military decision-making process forecasting for survivability utilizing the Electromagnetic Spectrum detection avoidance measures.
### <h2 id="Software-Solution">**Software Solution**</h2>
Electromagnetic (EM) planning tool taking anticipated military electronics equipment to be utilized as input and provides EM signature output for planning purposes and course of action development.
 * Military Equipment EM Emissions - ***`Partially accomplished (database)`***
 * Satellite Imagery Overlay - ***`Not accomplished`***
 * Location Grid Input - ***`Accomplished`***
 * Equipment EM Emision Diameter - ***`Not accomplished`***
 * Enemy EM Emissions Detection Parameters - ***`Not accomplished`***

This module allows users to plot EM emissions Latitude and Longitude grids onto maps.
### <h2 id="6330-Challenge">**The CIDM 6330 Domain Model Challenge**</h2>
### <ins>**Django-Choices and Mods to the Model**</ins>
 1) Django Rest Framework for API
 2) Django Channels for the External Message Queue
 3) Django does its own bootstrapping and we'll partially forego DI
 4) Django Signals for the Internal Message Queue
 5) Django apps use views to provide these handlers
 6) Django ORM transactions handle this
 7) Don't fight the monolith, will not implement
 8) Redis
 9) Domain intact

 ![alt text](<outside_scope/png/9 steps.png>)

 Image 1: Dr. Babb's Workflow of Percival and Gregory's Domain Model
***
### <h2 id="Diagram-Sketches">**Diagram Sketches**</h2>
The notion of the EM Planning Software provided a baseline to conceptualize sketching Unified Modeling Language (UML) Diagrams.

#### **`Class Diagram`**
This diagram examines the relationships between the military commander, EM emission sensor data collection Soldier, data messaging, database writing/reading, and map point plotting.  Although rudimentary, the thought experiment created a foundation to build the real-life event sensory effect into a visualization tool for the commander to make informed decisions.

![alt text](<outside_scope/png/Class Diagram.drawio.png>)

Image 2: Assignment 3 Class Diagram UML
***
#### **`Activity Diagram`**
This diagram surveys the flow of commander's intent to Solder and equipment actions creating sensed data for analysis and digestion.  Ultimately driving visual data into the Common Operating Picture for decision making.

![alt text](<outside_scope/png/Activity Diagram.drawio.png>)

Image 3: Assignment 3 Activity Diagram UML
***
#### **`Sequence Diagram`**
This diagram outlines the progression of doctrine generating workflow and directing military decision-making process by organization's staff officers. The sequence of events triggers our EM Planning Tool's use for future operations planning.

![alt text](<outside_scope/png/Sequence Diagram.drawio.png>)

Image 4: Assignment 3 Sequence Diagram UML
***
#### **`Use Case Diagram`**
This diagram depicts equipment transmitting EM emissions being captured by EM sensor equipment, the Soldier responsible for that data processing and fighting product creation, and the commander who drives resource allocation.

![alt text](<outside_scope/png/Use Case Diagram.drawio.png>)

Image 5: Assignment 3 Use Class Diagram UML
***
### <h2 id="TDD-Approach">**Test Driven Development (TDD) Approach Used**</h2>
The UML diagrams provided context to perceive potential tests.  My initial list of testing ideas held throughout development with evolution and grouping occurring naturally. 

### <ins>Initial testing method ideas</ins>:
 * Latitude / Longitude grid point off map / outlier
 * Read CSV (EM Database)
 * Min/Max Latitudes Longitudes
 * The map file get path
 * Figure size, marker size, x/y limits
 * Matplolib alpha transparency, graph title/labels/legend

 ### <ins>Testing methods used</ins>:
  * <span style='color: 4EC8AE;'>User</span>

| `setUp` | `test_get_consumers_authenticated` |
|`test_get_consumers_un_authenticated` | `test_post_consumer_authenticated` |

  * <span style='color: 4EC8AE;'>EMData</span>

| `setUp` | `test_lat_long` |
  * <span style='color: 4EC8AE;'>LatLongPoints</span>

| `test_plot_figures_added` |
  * <span style='color: 4EC8AE;'>Colors</span>

| `setUp` | `test_get_hex_color` |
  * <span style='color: 4EC8AE;'>FrequencyDevice</span>

| `test_frequency` |
  * <span style='color: 4EC8AE;'>DataConversion</span>

| `test_filtering` | `test_aggregation` | `test_dataframe_dtypes` |
  * <span style='color: 4EC8AE;'>DateTime</span>

| `test_timestamp` |
  * <span style='color: 4EC8AE;'>FakePlotting</span>

| `test_plot_square1` | `test_module` | `test_curve_sqr_plot` |
  * <span style='color: 4EC8AE;'>Mapping</span>

| `test_plot_figures_added_map` |
  * <span style='color: 4EC8AE;'>Layout</span>

| `test_spines_axes_positions` |

### <h2 id="Exploring-Tests">**Exploring Tests and their Validity**</h2>
 With Percival and Gregory's examples of TDD architecture approach and the Domain Model, the Django Rest Framework was utilized to build the module outline and chosen "monolith" of Django. The TDD iterative cycle, `Fail - Pass - Refactor`, was not met across the board for all of my tests. Fail, fail, fail may be more accurate with my instances, but the concept of what should be tested holds merit.

<span style='color: 4EC8AE;'>User</span>: This testing is intended to verify user account creation and authentication.

<span style='color: 4EC8AE;'>EMData</span>: This testing is intended to validate data from an post to the em_data.csv with defined parameters. 

<span style='color: 4EC8AE;'>LatLongPoints, FakePlotting, Mapping</span>: This testing is intended to verify scatterplot points are populating on the graph/map with accuracy. In hindsight I would combine LatLongPoints, FakePlotting, and Mapping into one class. There ended up being superfluous redundancies between these classes.

<span style='color: 4EC8AE;'>Colors</span>: This testing is intended to verify RGB and Hex Colors are able to be accessed from the dictionary of available colors.  It also asserts false values to fail the test.

<span style='color: 4EC8AE;'>FrequencyDevice</span>: This testing is intended to validate based on a range of mHz frequencies a known type of device is identified. 30-90mHz = FM Radio, 225-512mHz = Tactical Satellite Radio, 950-2150mHz = Joint Capabilities Release (AKA Blue Force Tracker), 2150+mHz = WiFi puck.

<span style='color: 4EC8AE;'>DataConversion</span>: This testing is intended to verify the conversion of data from csv to json and vice versa.

<span style='color: 4EC8AE;'>DateTime</span>: This testing is intended to fail by asserting a timestamp in the past is equal to now. Date and time are such pure information and import accessors that testing in this area is probably unnecessary.

<span style='color: 4EC8AE;'>Layout</span>: This testing is intended to verify the plotting diagram layout parameters match the given range.

### <h2 id="Coding-Route">**Coding Route Taken**</h2>
I found the following pattern of coding by python module to be the most efficient; however, I acknowledge not every Unit of Work needs representation on all modules.

<ins>dj_em_planning</ins>: <br>`urls` &rarr; `settings` &rarr; `asgi` &rarr; `asgi`</br>

<ins>em_planning_arch</ins>: <br>`apps` &rarr; `domain/model` &rarr; `services/commands`</br>

<ins>em_planning_api</ins>: <br>`urls` &rarr; `models` &rarr; `serializers` &rarr; `views` &rarr; `admin` &rarr; `apps` &darr;</br>&darr; &nbsp; &nbsp; &nbsp; &larr; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &larr; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &larr; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &larr; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &larr; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &larr; <br>&rarr; `consumers` &rarr; `permissions` &rarr; `signals` &rarr; `tests`

I recognize TDD is meant to build tests first. I took this as build tests prior to diving in application development. I did not see a way forward to test building without running through the urls, models, serializers, and views modules. These core modules that the Django Rest Framework auto populates are interdependent and import sections of each other for testing.

<ins>For example</ins>:

<span style='color: 82516C;'>from</span> <span style='color: 4EC8AE;'>em_planning_arch.domain.model</span> <span style='color: 82516C;'>import <span style='color: 4EC8AE;'>DomainEMData</span>

<span style='color: 82516C;'>from</span> <span style='color: 4EC8AE;'>.models</span> <span style='color: 82516C;'>import</span> <span style='color: 4EC8AE;'>User, EMData, LatLongPoints</span>

These module classes were in place on models prior to being imported into serializers. In the workflow, I felt the need to follow this logic.

### <h2 id="Encountered-Pitfalls">**Encountered Pitfalls**</h2>

 * Scope creep
 * Writing too many tests at once
 * Writing unnecessary tests
    * Imported accessors
 * Coding &rarr; Problem encountered &rarr; 2 hours of researching documentation &rarr; Problem fixed &rarr; Forgot coding direction

When coding, I find the struggle to be real. I don't shy away from the challenge of learning this new language and best practices for architecture and design. The repetitions and what feels like blunt force trauma has a lasting effect on improvement.

![Coding Cycle](https://i.pinimg.com/originals/34/24/d5/3424d5afdedbed4812296777c8154ab6.jpg)

[Image 6][Cycle]: The Never Ending Cycle of Coding
***
### <h2 id="Exciting-Revelation">**Exciting Revelation**</h2>

The more code I created and problems I resolved the more my mind began to retain the coding language. Several times I went to bed after hours of struggling with a particular problem. My subconscious would work the issues and on a few instances the problems would enter my dreams. More often than not, I woke up with a solution (or another iteration of attempted solution). I can say with certainty I will never be on the level of Neo from the Matrix, but I recognize the progress.

![Coding Architecture](https://cdn.quotesgram.com/img/35/43/1470817928-matrix-hallway.jpg)

[Image 7][Matrix]: Matrix Code Architecture Hallway
***
### <h2 id="Problem-Overview">**Problem Overview**</h2>
The past twenty years of warfare has focused on Counterinsurgency (COIN) operations with adversaries that did not have the same capabilities.  The lessons learned and best practices from this asymmetric warfare serve as the foundation for the next phase of anticipated conflict.  The US Army has accepted Large Scale Combat Operations (LSCO) as the methodology of conflict with near-peer adversaries such as Russia or China.  As the world watches the on-going LSCO in Ukraine, warfighting lessons become apparent to all echelons of our servicemembers….and our adversaries.  The way we fought in Afghanistan and Iraq for COIN will not work for LSCO.

Near-peer adversaries have similar capabilities to the Department of Defense (DoD) across all five domains of warfare: land, sea, air, space, and cyberspace.  Large Scale Combat focuses on massing combat power to attrit enemy forces and acquire territory to deny enemy advantage.  In COIN, Tactical Operation Centers (TOC) were the means of controlling the fight.  TOCs had robust capabilities and encouraged warfighting functions to synchronize efforts against the enemy.  After twenty years of fighting, we fell victim to what all bureaucracies develop with time.  TOCs became too big and lack mobility, the term “TOC-mahals” is commonplace because of their complexity.  TOCs primary issue within the LSCO framework is the lack of mobility.

LSCO adversaries maintain indirect fire, air attack, and cyber and electronic warfare (EW) capabilities.  They have the means of discovering the location and destroying Main Command Posts (MCP).  TOC = static.  MCP = light and mobile.  Both TOCs and MCPs are types of command posts and provide a physical location for planners, combat systems, and the required IT network.

The process of military acquisitions is slow.  Years even.  If the threat of near-peer adversaries exists today, the military cannot wait for the acquisitions process to fill emerging requirements.  We need to figure out potential solutions to this problem set with the already appropriated equipment and capabilities.

![EM Example from NTC](https://www.thedrive.com/content/2020/05/electronic-warfare-top.jpg?quality=85&auto=webp&optimize=high&crop=16%3A9&auto=webp&optimize=high&quality=70&width=1920)

[Image 8][EM Image]: Battalion Main Command Post Large Electromagnetic Signature
***
### <h2 id="References">**References**</h2>
1. Image 1: Dr. Babb's Workflow of Percival and Gregory's Domain Model. CIDM 6330 Slides: <ins>CIDM6330-MessagesQueues</ins>. Slide 23.
2. Image 2: Assignment 3 Class Diagram UML.
3. Image 3: Assignment 3 Activity Diagram UML.
4. Image 4: Assignment 3 Sequence Diagram UML.
5. Image 5: Assignment 3 Use Case Diagram UML.
6. [Image 6][Cycle]: ["The Vicious Cycle of Coding"](https://i.pinimg.com/originals/34/24/d5/3424d5afdedbed4812296777c8154ab6.jpg)
7. [Image 7][Matrix]: ["Matrix Code Architecture Hallway"](https://cdn.quotesgram.com/img/35/43/1470817928-matrix-hallway.jpg)
8. [Image 8][EM Image]: ["This is What Ground Forces Look Like to an Electronic Warfare System and Why It's a Big Deal" by Joseph Trevithick](https://www.thedrive.com/the-war-zone/33401/this-is-what-ground-forces-look-like-to-an-electronic-warfare-system-and-why-its-a-big-deal)
9. ["Preparing for Large-Scale Combat Operations" by Center for Army Lessons Learned](https://api.army.mil/e2/c/downloads/2023/01/31/73b50bab/21-6-preparing-for-lsco-public.pdf)

[Cycle]: https://i.pinimg.com/originals/34/24/d5/3424d5afdedbed4812296777c8154ab6.jpg
[Matrix]: https://cdn.quotesgram.com/img/35/43/1470817928-matrix-hallway.jpg

[EM Image]: https://www.thedrive.com/the-war-zone/33401/this-is-what-ground-forces-look-like-to-an-electronic-warfare-system-and-why-its-a-big-deal