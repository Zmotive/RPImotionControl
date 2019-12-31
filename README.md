This is a small test file for checking the motion control hat that I am currently developing. 

The Data sheet for the A4988 board is here: https://www.pololu.com/file/0J450/a4988_DMOS_microstepping_driver_with_translator.pdf

The info on GPIO control can be found here: https://www.raspberrypi.org/documentation/usage/gpio/python/README.md

The devices used are:
24Vdc to 5Vdc Pi power supply: https://www.amazon.com/gp/product/B07PTYLP5W/ref=ppx_yo_dt_b_asin_title_o05_s02?ie=UTF8&psc=1
pi Prototype hat: https://www.amazon.com/gp/product/B07MCX54ZD/ref=ppx_yo_dt_b_asin_title_o05_s01?ie=UTF8&psc=1
Some headers: https://www.amazon.com/gp/product/B07CWSXY7P/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1
Some terminal blocks: https://www.amazon.com/gp/product/B01EUXLE8O/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1
1 50VDC 470uF electrolitic Capacitor: https://www.amazon.com/gp/product/B07SB1MZFG/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1
A4988 Stepper motor controller: https://www.amazon.com/gp/product/B01FFGAKK8/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
some Jumpers: https://www.amazon.com/gp/product/B01L5ULRUA/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
24VDC power Supply: https://www.amazon.com/gp/product/B01GC6VS8I/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1


The Capacitor is to keep a stable 24VDC at the motor controller and powersupply input. 

Future work is to:
	
	-Put EEPROM chip on hat and develop driver/interface
	-create board with up to 3 A4988 chips
	-create SuperSpeed USB3.0 Field Bus for chaining multiple controllers together

Second stage is to build for industrial servos (probably automation direct since they are the cheapest)

