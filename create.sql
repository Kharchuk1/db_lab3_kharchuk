
-------------------------
-- Create Team table
-------------------------
CREATE TABLE Team
(
  team_id      int       NOT NULL ,
  team_name    char(10)  NOT NULL 
);

--------------------------
-- Create Player table
--------------------------
CREATE TABLE Player
(
  player_id   char(20)     NOT NULL ,
  player_name char(50)     NOT NULL ,
  poss        char(10)     NOT NULL ,
  team_id     int          NOT NULL 
);

----------------------
-- Create Statistic table
----------------------
CREATE TABLE Statistic
(
  stat_id           int              NOT NULL ,
  player_id         char(20)         NOT NULL ,
  minutes_played    int              NOT NULL ,
  raptor_box_total  decimal(10,5)    NOT NULL 
);

----------------------
-- Define primary keys
----------------------
ALTER TABLE Team ADD CONSTRAINT PK_Team PRIMARY KEY (team_id);
ALTER TABLE Player ADD CONSTRAINT PK_Player PRIMARY KEY (player_id);
ALTER TABLE Statistic ADD CONSTRAINT PK_Statistic PRIMARY KEY (stat_id);

----------------------
-- Define foreign keys
----------------------
ALTER TABLE Player
ADD CONSTRAINT FK_Team_Player FOREIGN KEY (team_id) REFERENCES Team (team_id);
ALTER TABLE Statistic
ADD CONSTRAINT FK_Player_Statistic FOREIGN KEY (player_id) REFERENCES Player (player_id);