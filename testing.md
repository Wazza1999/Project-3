# Testing

Once the portal was operational I set about testing it for errors and to ensure any possible errors that can be made were caught.

The deployed project live link is [HERE](https://project-3-heroku-8742cd432e6c.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

The following tests were carried out to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Name input | User is asked to enter their name | First & Last name input| Works as expected | 
| Name input | User inputs symbol or number | Error message appears | Works as expected | 
| Profession | User selects their profession | User selects a - f | Works as expected | 
| Profession | User selects invalid letter | Error message appears | Works as expected | 
| Information | User given contractor No & pay | Information confirmed as true | Works as expected |
| Information | Information entered incorrect | Notice appears to start again | Works as expected |
| Dates & hours | User adds dates, days and hours | Correct information confirmed | Works as expected |
| Dates & hours | Incorrect information added | Error message appears | Works as expected |
| "n" option  | User selects no to confirmation | Notice appears to start again | Works as expected |
| Confirmed Info | Everything entered presented | Pay amount minus tax & NI appears | Works as expected |
| Submit info | Everything entered ready to submit | Users clicks y to submit | Works as expected |
| Submit info | Ready to submit, n selected | Notice appears to start again | Works as expected |

## Testing Browsers
The portal was tested in the following browsers (based on my own testing and those of people who tested the portal):

- Chrome
- Edge
- Firefox
- Oprea
- Safari

It worked without issues in the above browsers.

## Testing Google Sheets

Once the Google sheets was attached and working I tested the system several times by including ficticious workers that were added as data to the Google sheets file.

When first added the data numerical value added extra numbers e.g. £897.4953 - to ensure the number was rounded to only two digits at the end the str(round) object was used. The idea to use str(round) decided after a session with Tutor support.

![round](assets/images/strround-testing.png)

Even though Google Sheets was added after the program was developed there were no other issues and it worked perfectly and integrated easily.

## CSS and HTML Validation

A small amount of CSS and HTML was used when creating the 404 error page. Both pages were run through the appropriate W3C validator and no errors were found.

## Future Updates

As a result of testing requests for future functionality include:

The ability to edit information already added if it is incorrect without having to start again.

Contractor can selection options for other payments that need to be removed from their pay e.g. student loan or pension to make their final pay amount more accurate.


### [BACK TO README](https://github.com/todiane/corri-construction-p3/blob/main/README.md)