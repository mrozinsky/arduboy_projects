/*
Hello, World! example
June 11, 2015
Copyright (C) 2015 David Martinez
All rights reserved.
This code is the most basic barebones code for writing a program for Arduboy.

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
*/

#include <Arduboy2.h>

// make an instance of arduboy used for many functions
Arduboy2 arduboy;

constexpr uint8_t smallRabbitImageWidth = 8;
constexpr uint8_t smallRabbitImageHeight = 8;
int frame;

const uint8_t smallRabbitImages[] PROGMEM =
{
	// Dimensions
	smallRabbitImageWidth, smallRabbitImageHeight,
	
	// Frame 0 (North)
	0x00, 0x78, 0x7E, 0x78, 0x78, 0x7E, 0x78, 0x00,
	
	// Frame 1 (East)
	0x00, 0x00, 0x78, 0x7E, 0x48, 0x78, 0x00, 0x00,
	
	// Frame 2 (South)
	0x00, 0x78, 0x4E, 0x78, 0x78, 0x4E, 0x78, 0x00,
	
	// Frame 3 (West)
	0x00, 0x00, 0x78, 0x48, 0x7E, 0x78, 0x00, 0x00,
};

// This function runs once in your game.
// use it for anything that needs to be set only once in your game.
void setup() {
  // initiate arduboy instance
  arduboy.begin();

  // here we set the framerate to 15, we do not need to run at
  // default 60 and it saves us battery life
  arduboy.setFrameRate(10);
}


// our main game loop, this runs once every cycle/frame.
// this is where our game logic goes.
void loop() {
  // pause render until it's time for the next frame
  if (!(arduboy.nextFrame()))
    return;

  frame++;
  if (frame == 4) frame = 0;

  // first we clear our screen to black
  arduboy.clear();

  // we set our cursor 5 pixels to the right and 10 down from the top
  // (positions start at 0, 0)
  arduboy.setCursor(4, 9);

  // then we print to screen what is in the Quotation marks ""
  arduboy.print(F("Hello, world!"));
  
  Sprites::drawOverwrite(30, 30, smallRabbitImages, frame);

  // then we finaly we tell the arduboy to display what we just wrote to the display
  arduboy.display();
}
