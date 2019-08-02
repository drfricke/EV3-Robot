# EV3-Robot

Setup EV3/Motor Drive/DC motors.

In terminal (Mac, for windows putty can be used) create a ssh connection with deired EV3. (ssh robot@ - ip address, password 'maker')

Open desired file. File c.py is the most up-to-date file to use for experiments (06/19/19). (ex. 'python3 control.py')

To upload a file from your computer to the EV3. Create a sftp (sftp robot@...) connection with the EV3 and use the 'put' command.


# Using file control.py

'w' - Enter the selected PWM

'p' - Increases PWM by 5. 0 = Full Reverse. ~50 = stop. 100 = Full Forward.

'o' - Decreases PWM by 5.

'l' - Increases PWM by 5. 0 = Full Reverse. ~50 = stop. 100 = Full Forward.

'k' - Decreases PWM by 5.

' ' - stop

# Using file Remote_Drive.py

(use this program to control rover)

'w' - Enter the selected PWM to go forward (over 50 PWM)

'a' - Enter the selected PWM to turn left

'd' - Enter the selected PWM to turn right

'x' - Enter the selected PWM to reverse (over 50 PWM)

'p' - Increases PWM by 5. 0 = Full Reverse. ~50 = stop. 100 = Full Forward.

'o' - Decreases PWM by 5.

'l' - Increases PWM by 5. 0 = Full Reverse. ~50 = stop. 100 = Full Forward.

'k' - Decreases PWM by 5.

'm' - Give current RPS

' ' - stop

# Using file Drive.py

This program is controlled with the interface on the rover.

The steering wheel is supposed to control steering, however the motors aren't pwerful enough for this to work.

The lever controls speed. Make sure to have in upright position before program starts. The touch botton on top functions as a dead man switch, when released the rover will stop and when held down the rover will move according to the levers change in position from the starting location.

The second touch button will exit the program, brake the rover, and turn off the relay.
