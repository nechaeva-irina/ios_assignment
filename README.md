# IOS Application assignment

This project is designed using page object and data driven approaches:
- All tests are separated by screens in the application: Sliders, Switches, etc.
- Test data for tests is stored separately in `data` folder as objects of corresponding classes. The classes can be found in `model` folder. 
- Desired simulator capabilities are stored in `target.json` file.

These approaches together with pytest framework provide high scalability, allow tests reusage with different input values and make adding new tests much easier.       

### To run the tests on your local machine
1. Clone the current repo
2. Install dependancies, listed in `requirements.txt`
3. Run Appium
4. In the command line open cloned repo directory and run `python -m py.test tests`
